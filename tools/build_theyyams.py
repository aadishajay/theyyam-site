"""Builds theyyams/ pages, assets/theyyams.json and patches the shared header on root pages.
Run from the website folder: python3 tools/build_theyyams.py"""
import re,json,html,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from theyyams_data import T,CATS
B='https://aadishajay.github.io/theyyam-site/'
E=lambda s:html.escape(s,quote=True)
IMG={'muchilot-bhagavathi':'muchilot','kathivanoor-veeran':'kathivanoor','pulimaranja-thondachan':'pulimaranja','kadangot-makkam':'makkam'}
cred=json.load(open('tools/credits.json'))
catl={c[0]:c[1] for c in CATS}
src=open('what-is-theyyam.html').read()
css=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
css=re.sub(r'\n\.skip\{.*',"",css) if False else css
header=re.search(r'<header class="hd">.*?</header>',src,re.S).group(0)
footer=re.search(r'<footer.*?</footer>',src,re.S).group(0)
org=re.search(r'application/ld\+json">(.*?)</script>',src,re.S).group(1)
orgs=json.loads(org)['@graph'][:2]
fonts='\n'.join(re.findall(r'<link[^>]*>',src))
def up(h):  # make root-relative links work from theyyams/
    h=re.sub(r'(href|src)="(?!https?:|#|\.\./|mailto:)([^"]*)"',lambda m:f'{m.group(1)}="../{m.group(2)}"',h)
    return h
header_t=up(header).replace('href="../journal.html" aria-current="page" style="color:#D7261E"','href="../journal.html"')
footer_t=up(footer)
footer_t=re.sub(r'<p style="font-size:13px;opacity:.85;margin-top:32px">.*?</p>','<p style="font-size:13px;opacity:.85;margin-top:32px">Photographs: Wikimedia Commons contributors, credited on each page. Placeholders until we use our own.</p>',footer_t,1,flags=re.S)
def nav(h,cur=None):
    h=h.replace('<a href="../trips.html">Guided trips</a>','<a href="../trips.html">Guided trips</a><a href="../theyyams/"'+(' aria-current="page" style="color:#D7261E"' if cur else '')+'>Theyyams</a>') if '../theyyams/' not in h else h
    return h
header_t=nav(header_t,True)
extra_css='''
.chip{display:inline-flex;align-items:center;min-height:32px;padding:0 14px;border-radius:999px;background:#FFB400;color:#1a0a08;font-weight:700;font-size:13px;letter-spacing:.04em;text-transform:uppercase;text-decoration:none}
.ml{font-size:1.1rem;font-weight:500;opacity:.85;margin-top:6px}
.hero{display:grid;gap:28px;padding:32px 0 8px}
.hero img.h{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;border-radius:28px;border:2px solid #1a0a08}
.facts{border:2px solid #1a0a08;border-radius:24px;padding:22px 24px;background:#fff}
.facts dl{margin:0;display:grid;gap:14px}.facts dt{font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:#D7261E}.facts dd{margin:2px 0 0;font-weight:500}
.gal{display:grid;gap:16px;margin:28px 0}.gal figure{margin:0}.gal img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:20px}.gal figcaption{font-size:12px;opacity:.7;margin-top:6px}
.note{background:#FFB400;border-radius:24px;padding:22px 24px;margin:28px 0}
.sec p{margin:12px 0}.sec h2{margin-top:36px}
.cardg{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.tc{display:block;text-decoration:none;color:#1a0a08}
.tc img{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;border-radius:20px;background:#eee}
.tc h3{margin:10px 0 0;font-size:1.05rem}.tc .m{font-size:13px;opacity:.7;margin:0}.tc p.t{font-size:13px;margin:4px 0 0;line-height:1.45}
.tc:hover h3{color:#D7261E}
.srcs{font-size:13px;opacity:.8;margin-top:32px}
.fchips{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 0}
.fchips button{font:inherit;font-weight:600;min-height:44px;padding:0 18px;border-radius:999px;border:2px solid #fff;background:transparent;color:#fff;cursor:pointer}
.fchips button[aria-pressed=true]{background:#FFB400;border-color:#FFB400;color:#1a0a08}
.hubsearch{position:relative;margin-top:22px;max-width:560px}
.hubsearch input{width:100%;min-height:56px;border-radius:999px;border:2px solid #fff;padding:0 24px;font:inherit;font-size:17px;background:#fff;color:#1a0a08}
.hubsearch input:focus{outline:4px solid #FFB400}
.empty{padding:28px;border:2px dashed #1a0a08;border-radius:20px;margin:24px 0}
@media(min-width:768px){.hero{grid-template-columns:5fr 6fr;align-items:start;gap:48px;padding-top:48px}.gal{grid-template-columns:repeat(2,1fr)}.cardg{grid-template-columns:repeat(4,1fr);gap:24px}}
'''
def head(title,desc,url,ld,extra=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="noindex,nofollow">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="article"><meta property="og:url" content="{B}{url}"><meta property="og:site_name" content="LGFC Theyyam"><meta property="og:image" content="{B}assets/theyyam/{extra}">
<meta name="theme-color" content="#4A0E12">
{fonts}
<style>
{css}
{extra_css}
</style>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":orgs+ld},ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''
def img(t): return IMG.get(t['slug'],t['slug'])
def tcard(t,pre=''):
    p=img(t)
    return f'<a class="tc" href="{pre}{t["slug"]}.html"><img src="../assets/theyyam/{p}-1.jpg" alt="{E(t["name"])} Theyyam performer in costume" width="400" height="500" loading="lazy"><h3>{E(t["name"])}</h3><p class="m">{E(t["ml"])} · {E(catl[t["cat"]])}</p><p class="t">{E(t["tag"])}</p></a>'
def bc(items): return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":B+u} for i,(n,u) in enumerate(items)]}
os.makedirs('theyyams',exist_ok=True)
# detail pages
for t in T:
    p=img(t); cr=cred[p]
    alts=[f'{t["name"]} Theyyam performer in costume',f'Close view of the {t["name"]} Theyyam face and headdress',f'{t["name"]} Theyyam during a ritual in North Malabar, Kerala']
    desc=f'{t["name"]} Theyyam: {t["tag"]} Story, meaning and what to expect.'
    if len(desc)>155: desc=f'{t["name"]} Theyyam of North Malabar: story, meaning, appearance and what to expect when you watch.'
    others=[x for x in T if x['cat']==t['cat'] and x is not t]+[x for x in T if x['cat']!=t['cat']]
    rel=others[:4]
    faq=[(f'Who is {t["name"]} in Theyyam?',t['who']),(f'What does {t["name"]} Theyyam look like?',t['look'])]
    ld=[bc([("Home",""),("Theyyams","theyyams/"),(t['name'],f'theyyams/{t["slug"]}.html')]),
        {"@type":"Article","headline":f'{t["name"]} Theyyam: story, meaning and what to expect',"description":desc,"author":{"@id":B+"#org"},"publisher":{"@id":B+"#org"},"mainEntityOfPage":f'{B}theyyams/{t["slug"]}.html',"image":f'{B}assets/theyyam/{p}-1.jpg',"about":{"@type":"Thing","name":f'{t["name"]} Theyyam',"alternateName":[t['ml']]+t['alias']}},
        {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    h=head(f'{t["name"]} Theyyam: Story, Meaning & What to Expect | LGFC Theyyam',desc,f'theyyams/{t["slug"]}.html',ld,f'{p}-1.jpg')
    h+=header_t+'\n<main id="main"><article>\n<div class="w">\n'
    h+=f'<nav aria-label="Breadcrumb" style="font-size:14px;padding-top:24px"><a href="../index.html">Home</a> / <a href="./">Theyyams</a> / {E(t["name"])}</nav>\n'
    h+=f'<div class="hero"><img class="h" src="../assets/theyyam/{p}-1.jpg" alt="{E(alts[0])}" width="760" height="950"><div><a class="chip" href="./#{t["cat"]}">{E(catl[t["cat"]])}</a><h1 style="margin-top:14px">{E(t["name"])}</h1><p class="ml" lang="ml">{E(t["ml"])}</p><p style="font-size:1.15em;font-weight:500;margin:18px 0 22px">{E(t["tag"])}</p><div class="facts"><dl>'+''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a,b in t['facts'])+'</dl></div></div></div>\n'
    h+='<div class="art sec" style="padding-bottom:8px">\n'
    h+=f'<h2>Who is {E(t["name"])}?</h2><p>{E(t["who"])}</p>\n<h2>The story</h2>'+''.join(f'<p>{E(x)}</p>' for x in t['story'])+'\n'
    if len(cr)>1:
        h+='<div class="gal">'+''.join(f'<figure><img src="../assets/theyyam/{c["file"]}" alt="{E(alts[i+1])}" width="{c["w"]}" height="{c["h"]}" loading="lazy"><figcaption>Photo: {E(c["artist"])}, {E(c["lic"])}, via Wikimedia Commons</figcaption></figure>' for i,c in enumerate(cr[1:3]))+'</div>\n'
    h+=f'<h2>What you will see</h2><p>{E(t["look"])}</p>\n<h2>In the tradition</h2><p>{E(t["trad"])}</p>\n<div class="note"><b>A note for visitors</b><p style="margin:8px 0 0">{E(t["note"])} Photography and video are not allowed at some rituals, so ask your guide first.</p></div>\n'
    h+='<h2>Quick answers</h2>'+''.join(f'<details><summary><h3>{E(q)}</h3></summary><p style="margin-top:0">{E(a)}</p></details>' for q,a in faq)
    h+='\n<div class="cta" style="margin-top:36px"><h3>Learn about the Theyyams with a local guide</h3><p>Our guided trips explain each deity’s story as you see it, and are planned with you on enquiry. We never publish ritual dates or venues, and confirm the right nights with you closer to travel.</p><a class="btn" href="../enquire.html">Enquire about a trip</a></div>\n'
    h+='<p class="srcs"><b>Sources and further reading:</b> '+', '.join(f'<a href="{u}" rel="noopener">{E(n)}{" (Wikipedia)" if "wikipedia" in u else ""}</a>' for n,u in t['src'])+'. Stories vary by shrine, family and teller; this is a general summary, not a definitive version.</p>\n'
    h+='</div></div>\n'
    h+='<section style="padding:48px 0 72px"><div class="w"><h2 style="margin:0 0 20px">More Theyyams</h2><div class="cardg">'+''.join(tcard(x) for x in rel)+'</div><p style="margin-top:24px"><a class="btn red" href="./" style="background:#D7261E;color:#fff">Browse all Theyyams</a></p></div></section>\n'
    h+='</article></main>\n'+footer_t+'\n<script src="../assets/search.js" defer></script>\n</body>\n</html>\n'
    open(f'theyyams/{t["slug"]}.html','w').write(h)
# hub
hubdesc='Browse the Theyyams of North Malabar: gods, goddesses, heroes and shared traditions. Search by name, story or meaning, with images and history for each.'
ld=[bc([("Home",""),("Theyyams","theyyams/")]),{"@type":"CollectionPage","name":"The Theyyams of North Malabar","description":hubdesc,"url":B+"theyyams/"},
 {"@type":"ItemList","name":"Theyyams","itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{B}theyyams/{t["slug"]}.html',"name":t['name']} for i,t in enumerate(T)]}]
h=head('The Theyyams of North Malabar: A Guide to Each Deity | LGFC Theyyam',hubdesc,'theyyams/',ld,'muthappan-1.jpg')
h+=header_t+'\n<main id="main">\n'
h+='<section style="background:#4A0E12;color:#fff"><div class="w" style="padding-top:36px;padding-bottom:44px"><nav aria-label="Breadcrumb" style="font-size:14px;margin-bottom:18px;opacity:.85"><a href="../index.html" style="color:#fff">Home</a> / Theyyams</nav><h1>The Theyyams of North Malabar</h1><p style="font-size:18px;margin-top:18px;max-width:640px;opacity:.92">Hundreds of forms are recorded, each with its own story, face and song. Start here to meet some of them. Search by name, by what they stand for, or in Malayalam.</p>'
h+='<form class="hubsearch" role="search" onsubmit="return false"><label for="hubq" style="position:absolute;left:-999px">Search Theyyams</label><input id="hubq" type="search" placeholder="Try “Muthappan”, “fierce goddess” or “harmony”" autocomplete="off" aria-controls="hubgrid"></form>'
h+='<div class="fchips" role="group" aria-label="Filter by category"><button type="button" aria-pressed="true" data-c="">All</button>'+''.join(f'<button type="button" aria-pressed="false" data-c="{c[0]}">{E(c[1])}</button>' for c in CATS)+'</div></div><div class="kal"></div></section>\n'
h+='<section style="padding:36px 0 64px"><div class="w"><p id="hubstatus" aria-live="polite" style="font-size:14px;opacity:.8;margin:0 0 8px"></p><div id="hubgrid">'
for c in CATS:
    items=[t for t in T if t['cat']==c[0]]
    h+=f'<section class="cg" id="{c[0]}" data-c="{c[0]}" style="margin-top:36px"><h2>{E(c[1])}</h2><p style="margin:8px 0 20px;max-width:640px">{E(c[2])}</p><div class="cardg">'+''.join(tcard(t).replace('<a class="tc"',f'<a class="tc" data-s="{t["slug"]}"') for t in items)+'</div></section>'
h+='</div><div id="hubempty" class="empty" hidden><b>No match yet.</b><p style="margin:8px 0 0" id="hubdym"></p><p style="margin:8px 0 0">This list is growing. <a href="../enquire.html">Ask us</a> about a Theyyam you have heard of.</p></div>'
h+='<div style="margin-top:56px;max-width:720px"><h2>How we group them</h2><p style="margin-top:12px">This grouping is ours, to help readers. Scholars use other divisions, and many Theyyams fit more than one. Stories also differ from shrine to shrine and teller to teller. We have not included dates or places of performance, and the rituals are worship, not shows. See our <a href="../theyyam-etiquette.html">etiquette guide</a> before you go.</p></div>'
h+='</div></section>\n</main>\n'+footer_t+'\n<script src="../assets/search.js" defer></script>\n</body>\n</html>\n'
open('theyyams/index.html','w').write(h)
# search index
idx=[dict(s=t['slug'],n=t['name'],m=t['ml'],c=t['cat'],cl=catl[t['cat']],t=t['tag'],a=t['alias'],g=t['tags'],i=img(t),x=t['who'][:240]) for t in T]
json.dump(idx,open('assets/theyyams.json','w'),ensure_ascii=False)
# patch root pages
for f in ['index.html','trips.html','enquire.html','journal.html','what-is-theyyam.html','theyyam-etiquette.html','theyyam-season.html','planning-theyyam-on-your-own.html','main-theyyams.html','costume-and-craft.html','cameras-and-ritual.html']:
    s=open(f).read()
    if 'href="theyyams/"' not in s:
        s=s.replace('<a href="trips.html">Guided trips</a>','<a href="trips.html">Guided trips</a><a href="theyyams/">Theyyams</a>')
    if 'assets/search.js' not in s: s=s.replace('</body>','<script src="assets/search.js" defer></script>\n</body>',1)
    open(f,'w').write(s)
sm=open('sitemap.xml').read()
for u in ['theyyams/']+[f'theyyams/{t["slug"]}.html' for t in T]:
    if B+u not in sm: sm=sm.replace('</urlset>',f'<url><loc>{B}{u}</loc></url>\n</urlset>')
open('sitemap.xml','w').write(sm)
print('built',len(T))
