// Replacement for the lgfc_custom_trip_form_handler worker (Cloudflare Workers, module syntax).
// Changes from the old worker:
//  - Cloudflare Turnstile is verified server-side (the old check only tested that a reCAPTCHA field existed).
//  - Secrets come from Worker secrets (env.*), never from source code.
//  - CORS limited to our own origins; returns JSON so the website can show its own thank-you page.
//  - Input validated; bad dates no longer crash the worker.
// Set secrets:  wrangler secret put NOTION_TOKEN | SENDGRID_KEY | TURNSTILE_SECRET
// Set a plain var ALLOWED_ORIGINS, e.g. "https://aadishajay.github.io,https://<your-domain>".

const NOTION_DB = '76fe248f7c864d04acd6c1cf9eb38a01';
const SENDGRID_TEMPLATE = 'd-c138c441e91445e3844e6dad3cbbf938';

const rt = (v) => ({ rich_text: [{ type: 'text', text: { content: String(v ?? '').slice(0, 1900) } }] });
const num = (v) => ({ number: Number.isFinite(parseInt(v, 10)) ? parseInt(v, 10) : null });
const day = (v) => ({ date: { start: new Date(v).toISOString() } });

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const allowed = (env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim());
    const cors = {
      'Access-Control-Allow-Origin': allowed.includes(origin) ? origin : allowed[0] || '',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      Vary: 'Origin',
    };
    const json = (obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: { ...cors, 'Content-Type': 'application/json' } });

    const url = new URL(request.url);
    if (url.pathname !== '/submit') return new Response('Not found', { status: 404 });
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    if (request.method !== 'POST') return json({ error: 'Method Not Allowed' }, 405);
    if (!allowed.includes(origin)) return json({ error: 'Forbidden' }, 403);

    let d;
    try { d = await request.json(); } catch { return json({ error: 'Invalid body' }, 400); }
    if (d.company) return json({ ok: true }); // honeypot: pretend success

    // 1. Turnstile, verified with Cloudflare
    const ts = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      body: new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: d.turnstile || '', remoteip: request.headers.get('CF-Connecting-IP') || '' }),
    }).then((r) => r.json()).catch(() => ({ success: false }));
    if (!ts.success) return json({ error: 'Verification failed' }, 400);

    // 2. Validate
    const name = String(d.name || '').trim(), email = String(d.email || '').trim();
    const arr = new Date(d.arrivaldate), dep = new Date(d.departuredate);
    if (!name || !/^\S+@\S+\.\S+$/.test(email) || isNaN(arr) || isNaN(dep) || dep < arr) return json({ error: 'Invalid details' }, 400);

    const destination = d.destination || 'Theyyam, North Malabar';
    const enquiryId = `${name.slice(0, 4)}/${destination.slice(0, 4)}/${d.arrivaldate}`.toUpperCase();
    const uuid = crypto.randomUUID();

    // 3. Notion
    const notion = await fetch('https://api.notion.com/v1/pages', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.NOTION_TOKEN}`, 'Content-Type': 'application/json', 'Notion-Version': '2022-02-22' },
      body: JSON.stringify({
        parent: { database_id: NOTION_DB },
        properties: {
          'Enquiry ID': { title: [{ type: 'text', text: { content: enquiryId } }] },
          Name: rt(name), Email: { email }, Phone: { phone_number: d.phone || null },
          Destination: rt(destination), 'Kids Age': rt(d.kidsage), Budget: num(d.budget),
          Intent: { select: { name: d.intent || 'estimate_first' } },
          'Arrival Date': day(d.arrivaldate), 'Departure Date': day(d.departuredate),
          'Total Pax': num(d.totalpax), Adults: num(d.adultpax), Rooms: num(d.rooms),
          'Places Planned': rt(d.planplaces), 'Stay Type': rt(d.stayType), 'Special Requests': rt(d.specialreq),
          'Is Date Fixed ?': rt(d.datefixed), Status: { select: { name: 'New' } }, UUID: rt(uuid),
        },
      }),
    });
    if (!notion.ok) return json({ error: 'Could not save enquiry' }, 502);

    // 4. Confirmation email (failure here must not lose the lead)
    await fetch('https://api.sendgrid.com/v3/mail/send', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.SENDGRID_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        personalizations: [{ to: [{ email }], cc: [{ email: 'alerts@letsgoforacamp.com' }], dynamic_template_data: { name, email, enquiry_id: enquiryId, phone: d.phone, destination, totalpax: d.totalpax, adultpax: d.adultpax, stayType: d.stayType, datefixed: d.datefixed, arrivaldate: d.arrivaldate, departuredate: d.departuredate, planplaces: d.planplaces, specialreq: d.specialreq } }],
        from: { email: 'alerts@letsgoforacamp.com' },
        template_id: SENDGRID_TEMPLATE,
      }),
    }).catch(() => {});

    return json({ ok: true, enquiryId });
  },
};
