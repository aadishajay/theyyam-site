import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { abs, LANGS, HOME_PATH } from '../lib/site';
import { landing } from '../i18n/landing';
import { heroSlides } from '../data/hero';

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// All pages; the four landing pages carry hreflang alternates and their carousel photos (image sitemap).
export const GET: APIRoute = async () => {
  const posts = await getCollection('journal');
  const theyyams = (await getCollection('theyyams')).sort((a, b) => a.data.order - b.data.order);
  const alts = LANGS.map((l) => `<xhtml:link rel="alternate" hreflang="${l}" href="${abs(HOME_PATH[l])}"/>`).join('') + `<xhtml:link rel="alternate" hreflang="x-default" href="${abs('')}"/>`;
  const homes = LANGS.map((l) => {
    const imgs = heroSlides.map((s) => `<image:image><image:loc>${abs(`assets/hero/${s.file}.jpg`)}</image:loc><image:caption>${esc(landing[l][s.alt])}</image:caption></image:image>`).join('');
    return `<url><loc>${abs(HOME_PATH[l])}</loc>${alts}${imgs}</url>`;
  });
  const paths = [
    'trips.html', 'enquire.html', 'privacy.html', 'about.html', 'contact.html', 'journal.html', ...posts.map((p) => `${p.id}.html`),
    'theyyam-glossary.html', 'theyyams/', ...theyyams.map((t) => `theyyams/${t.data.slug}.html`),
  ];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n` +
    [...homes, ...paths.map((p) => `<url><loc>${abs(p)}</loc></url>`)].join('\n') + '\n</urlset>\n';
  return new Response(xml, { headers: { 'Content-Type': 'application/xml' } });
};
