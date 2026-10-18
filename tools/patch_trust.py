"""Adds Kannur-rooted trust signals to the landing page, trips and enquire pages, and the footer line everywhere. Idempotent."""
import re,glob
SEAL='''<svg viewBox="0 0 200 200" width="150" height="150" role="img" aria-label="Rooted in North Malabar" style="flex:none"><defs><path id="seal-c" d="M100,100 m-80,0 a80,80 0 1,1 160,0 a80,80 0 1,1 -160,0"/></defs><circle cx="100" cy="100" r="97" fill="#4A0E12" stroke="#FFB400" stroke-width="4"/><circle cx="100" cy="100" r="62" fill="none" stroke="#FFB400" stroke-width="1.5"/><text font-size="12.5" font-weight="700" letter-spacing="1.6" fill="#FFB400"><textPath href="#seal-c">ROOTED IN NORTH MALABAR · KANNUR · KASARAGOD · </textPath></text><text x="100" y="112" text-anchor="middle" font-size="28" font-weight="700" fill="#fff" lang="ml">മലബാർ</text></svg>'''
section=f'''<!--trust:start-->
<section class="sec" aria-label="Rooted in North Malabar" style="padding:48px 0 16px"><div class="w">
<div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
<div style="flex:0 0 auto;margin:0 auto">{SEAL}</div>
<div style="flex:1 1 340px"><p class="eyebrow" style="color:#D7261E;margin:0 0 12px">Rooted in North Malabar</p><h2 style="max-width:640px">Run by natives of North Malabar. Hosted like family.</h2><p style="font-size:18px;margin-top:16px;max-width:640px">We are a team of natives from Kannur and across North Malabar. After eight years of working with the families and villages of this region, we know who to ask, when to step back, and how to make a guest feel welcome.</p></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:32px">
<div class="card" style="padding:22px"><h3>Local, not outsourced</h3><p style="margin-top:8px">Your guide and driver are natives of North Malabar. Nobody reads you a script.</p></div>
<div class="card" style="padding:22px"><h3>Known to the families</h3><p style="margin-top:8px">Introductions come from people the families already trust, so you are welcomed, not merely allowed in.</p></div>
<div class="card" style="padding:22px"><h3>A real person replies</h3><p style="margin-top:8px">No checkout and no call centre. Our North Malabar team answers within two working days, and is on call 24x7 once you are booked.</p></div>
<div class="card" style="padding:22px"><h3>We protect the ritual</h3><p style="margin-top:8px">We never publish ritual dates or places, we brief every guest on etiquette, and we follow each shrine’s rules on photography.</p></div>
</div>
<ul style="list-style:none;margin:24px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px;font-size:14px"><li style="border:1.5px dashed #1a0a08;border-radius:999px;padding:6px 14px">LetsGoForACamp Travel and Innovation LLP</li><li style="border:1.5px dashed #1a0a08;border-radius:999px;padding:6px 14px">[TOURISM REGISTRATION NO.]</li><li style="border:1.5px dashed #1a0a08;border-radius:999px;padding:6px 14px">[GOOGLE RATING · REVIEW COUNT]</li><li style="border:1.5px dashed #1a0a08;border-radius:999px;padding:6px 14px">[MEMBER OF TOURISM ASSOCIATION]</li></ul>
</div></section>
<!--trust:end-->'''
# landing
s=open('index.html').read()
if '<!--trust:start-->' in s: s=re.sub(r'<!--trust:start-->.*?<!--trust:end-->',lambda m:section,s,flags=re.S)
else:
    a='<p style="font-size:13px;margin:14px 0 0;opacity:.75">Powered by letsgoforacamp</p></div></section>'
    assert a in s
    s=s.replace(a,a+section,1)
if '<span>Rooted in North Malabar</span>' not in s:
    s=s.replace('<span>Season: Oct to May</span>','<span>Rooted in North Malabar</span><span>Season: Oct to May</span>',1)
open('index.html','w').write(s)
# trips: one line under the trust strip
t=open('trips.html').read()
line='<p id="kannur-line" style="font-size:14px;margin:6px 0 0;font-weight:600">Run by natives of North Malabar · Hosted like family</p>'
if 'id="kannur-line"' not in t:
    a='<p style="font-size:13px;margin:14px 0 0;opacity:.75">Powered by letsgoforacamp</p>'
    if a in t: t=t.replace(a,line+a,1)
    open('trips.html','w').write(t)
# enquire: aside
e=open('enquire.html').read()
a='8+ years organising Theyyam tours · 500+ explorers hosted · 24x7 support on booked trips.'
if a in e and 'Replies come from our North Malabar team' not in e:
    e=e.replace(a,a+' Replies come from our North Malabar team, not a call centre.')
    open('enquire.html','w').write(e)
# footers everywhere
for f in glob.glob('*.html')+glob.glob('theyyams/*.html'):
    x=open(f).read()
    if 'Made with warmth in Kannur' in x: continue
    y=x.replace('>Powered by letsgoforacamp<','>Made with warmth in North Malabar, Kerala · Powered by letsgoforacamp<')
    if y!=x: open(f,'w').write(y)
print('ok')
