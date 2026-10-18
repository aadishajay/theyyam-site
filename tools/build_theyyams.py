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
.ph{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;background:#4A0E12;color:#FFB400;border-radius:20px;text-align:center;aspect-ratio:4/5}.ph span{font-size:1.6rem;font-weight:700;padding:0 12px}.ph small{color:#fff;opacity:.8;font-size:12px}.ph.h{border:2px solid #1a0a08;border-radius:28px;width:100%}
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
def first(t):
    c=cred.get(img(t)) or []
    return c[0]['file'] if c else None
def ph(t,cls):
    return f'<div class="ph {cls}" role="img" aria-label="{E(t["name"])}: photograph to come"><span lang="ml">{E(t["ml"])}</span><small>Photo to come</small></div>'
def tcard(t,pre=''):
    p=img(t);f1=first(t)
    pic=f'<img src="../assets/theyyam/{f1}" alt="{E(t["name"])} Theyyam in ritual attire" width="400" height="500" loading="lazy">' if f1 else ph(t,'tcp')
    return f'<a class="tc" href="{pre}{t["slug"]}.html">{pic}<h3>{E(t["name"])}</h3><p class="m">{E(t["ml"])} · {E(catl[t["cat"]])}</p><p class="t">{E(t["tag"])}</p></a>'
def bc(items): return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":B+u} for i,(n,u) in enumerate(items)]}

LINKS={'muthappan':['Muthappan'],'vishnumoorthi':['Vishnumoorthi','Vishnumurthy','Narasimhamoorthi'],'pottan':['Pottan'],'gulikan':['Gulikan','Guliga'],'kuttichathan':['Kuttichathan'],'poomaruthan':['Poomaruthan'],'muchilot-bhagavathi':['Muchilot Bhagavathi'],'uchitta':['Uchitta Bhagavathy','Uchitta'],'vasoorimala':['Vasoorimala'],'arya-poonkani':['Arya Poonkani'],'chamundi':['Chamundi'],'kathivanoor-veeran':['Kathivanoor Veeran'],'pulimaranja-thondachan':['Pulimaranja Thondachan'],'kadangot-makkam':['Kadangot Makkam'],'bappiriyan':['Bappiriyan'],'theechamundi':['Theechamundi'],'karimchamundi':['Karimchamundi','Karinchamundi'],'kurathi':['Kurathi Amma','Kurathi'],'kandanar-kelan':['Kandanar Kelan'],'vayanattu-kulavan':['Vayanattu Kulavan'],'bhairavan':['Bhairavan'],'puli-daivam':['Puli Daivam'],'vishakandan':['Vishakandan'],'puthiya-bhagavathi':['Puthiya Bhagavathi'],'mappila-theyyam':['Mappila Theyyams','Mappila Theyyam'],'ummachi':['Ummachi'],'police-theyyam':['Police Theyyam'],'panjuruli':['Panjuruli'],'angakkaran':['Angakkaran'],'daivathar':['Daivathar'],'bappuran':['Bappuran'],'madayil-chamundi':['Madayil Chamundi'],'kundora-chamundi':['Kundora Chamundi'],'padarkulangara-bhagavathy':['Padarkulangara Bhagavathy','Padarkulangara','Padakulangara Veeran'],'puliyoor-kali':['Puliyoor Kali'],'pulikandan':['Pulikandan'],'pulikarinkali':['Pulikarinkali'],'veerakali':['Veerakali'],'cheerumba-bhagavathi':['Cheerumba Bhagavathi','Cheerumba','Cheerumbas'],'aali-theyyam':['Aali Theyyam'],'kalanthan-mukri':['Kalanthan Mukri','Kalanthan'],'yogyar-akampadi':['Yogyar Akampadi'],'rakta-chamundi':['Rakta Chamundi'],'puliyoor-kannan':['Puliyoor Kannan'],'pulimaruthan':['Pulimaruthan'],'marapuli':['Marapuli']}
_terms=sorted({(t,s) for s,L in LINKS.items() for t in L},key=lambda x:-len(x[0]))
_tmap={t:s for t,s in _terms}
_re=re.compile(r'(?<![A-Za-z])('+'|'.join(re.escape(t) for t,_ in _terms)+r')(?![A-Za-z])')
def linkify(text,self_slug,used,pre=''):
    """escape text and link the first mention of each other Theyyam"""
    out=[];pos=0
    for m in _re.finditer(text):
        t=m.group(1);s=_tmap[t]
        if s==self_slug or s in used: continue
        used.add(s)
        out.append(E(text[pos:m.start()]));out.append(f'<a href="{pre}{s}.html">{E(t)}</a>');pos=m.end()
    out.append(E(text[pos:]));return ''.join(out)

os.makedirs('theyyams',exist_ok=True)
# detail pages
for t in T:
    p=img(t); cr=cred.get(p) or []
    alts=[f'{t["name"]} Theyyam in ritual attire',f'Close view of the {t["name"]} Theyyam face and headdress',f'{t["name"]} Theyyam during a ritual in North Malabar, Kerala']
    desc=f'{t["name"]} Theyyam: {t["tag"]} Story, meaning and what to expect.'
    if len(desc)>155: desc=f'{t["name"]} Theyyam of North Malabar: story, meaning, appearance and what to expect when you attend.'
    others=[x for x in T if x['cat']==t['cat'] and x is not t]+[x for x in T if x['cat']!=t['cat']]
    rel=others[:4]
    faq=[(f'Who is {t["name"]} in Theyyam?',t['who']),(f'What does {t["name"]} Theyyam look like?',t['look'])]
    ld=[bc([("Home",""),("Theyyams","theyyams/"),(t['name'],f'theyyams/{t["slug"]}.html')]),
        {"@type":"Article","headline":f'{t["name"]} Theyyam: story, meaning and what to expect',"description":desc,"author":{"@id":B+"#org"},"publisher":{"@id":B+"#org"},"mainEntityOfPage":f'{B}theyyams/{t["slug"]}.html',"image":(f'{B}assets/theyyam/{first(t)}' if first(t) else B+'assets/p-headdress-tall.jpg'),"about":{"@type":"Thing","name":f'{t["name"]} Theyyam',"alternateName":[t['ml']]+t['alias']}},
        {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    h=head(f'{t["name"]} Theyyam: Story, Meaning & What to Expect | LGFC Theyyam',desc,f'theyyams/{t["slug"]}.html',ld,first(t) or '../p-headdress-tall.jpg')
    h+=header_t+'\n<main id="main"><article>\n<div class="w">\n'
    h+=f'<nav aria-label="Breadcrumb" style="font-size:14px;padding-top:24px"><a href="../index.html">Home</a> / <a href="./">Theyyams</a> / {E(t["name"])}</nav>\n'
    h+=f'<div class="hero">{(f'<img class="h" src="../assets/theyyam/{first(t)}" alt="{E(alts[0])}" width="760" height="950">' if first(t) else ph(t,'h'))}<div><a class="chip" href="./#{t["cat"]}">{E(catl[t["cat"]])}</a><h1 style="margin-top:14px">{E(t["name"])}</h1><p class="ml" lang="ml">{E(t["ml"])}</p><p style="font-size:1.15em;font-weight:500;margin:18px 0 22px">{E(t["tag"])}</p><div class="facts"><dl>'+''.join(f'<div><dt>{E(a)}</dt><dd>{linkify(b,t["slug"],set())}</dd></div>' for a,b in t['facts'])+'</dl></div></div></div>\n'
    h+='<div class="art sec" style="padding-bottom:8px">\n'
    used=set()
    h+=f'<h2>Who is {E(t["name"])}?</h2><p>{linkify(t["who"],t["slug"],used)}</p>\n<h2>The story</h2>'+''.join(f'<p>{linkify(x,t["slug"],used)}</p>' for x in t['story'])+'\n'
    if len(cr)>1:
        h+='<div class="gal">'+''.join(f'<figure><img src="../assets/theyyam/{c["file"]}" alt="{E(alts[i+1])}" width="{c["w"]}" height="{c["h"]}" loading="lazy"><figcaption>Photo: {E(c["artist"])}, {E(c["lic"])}, via Wikimedia Commons</figcaption></figure>' for i,c in enumerate(cr[1:3]))+'</div>\n'
    if cr:
        h+=f'<p style="font-size:12px;opacity:.7;margin:-12px 0 20px">Hero photo: {E(cr[0]["artist"])}, {E(cr[0]["lic"])}, via Wikimedia Commons</p>\n'
    h+=f'<h2>What you will see</h2><p>{linkify(t["look"],t["slug"],used)}</p>\n'
    if 'koladhari' in (t['look']+t['trad']+t['note']+t['who']+' '.join(t['story'])+' '.join(v for _,v in t['facts'])): h+='<p style="font-size:13px;opacity:.75;margin-top:-4px">Koladhari: the person who takes on the kolam, the deity’s form. See <a href="../theyyam-glossary.html#koladhari">Theyyam words explained</a>.</p>\n'
    h+=f'<h2>In the tradition</h2><p>{linkify(t["trad"],t["slug"],used)}</p>\n<div class="note"><b>A note for visitors</b><p style="margin:8px 0 0">{linkify(t["note"],t["slug"],used)} Photography and video are not allowed at some rituals, so ask your guide first.</p></div>\n'
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
h+='<div style="margin-top:56px;max-width:720px"><h2>How we group them</h2><p style="margin-top:12px">This grouping is ours, to help readers. Scholars use other divisions, and many Theyyams fit more than one. Stories also differ from shrine to shrine and teller to teller. We do not publish dates or places, because Theyyam is worship kept by families and communities. See our <a href="../theyyam-etiquette.html">etiquette guide</a> before you go. Unsure of a word such as ottakolam or kaliyattam? See <a href="../theyyam-glossary.html">Theyyam words explained</a>.</p></div>'
h+='</div></section>\n</main>\n'+footer_t+'\n<script src="../assets/search.js" defer></script>\n</body>\n</html>\n'
open('theyyams/index.html','w').write(h)
# search index
idx=[dict(s=t['slug'],n=t['name'],m=t['ml'],c=t['cat'],cl=catl[t['cat']],t=t['tag'],a=t['alias'],g=t['tags'],f=first(t) or '',x=t['who'][:240]) for t in T]
json.dump(idx,open('assets/theyyams.json','w'),ensure_ascii=False)
# patch root pages
for f in ['index.html','trips.html','enquire.html','journal.html','what-is-theyyam.html','theyyam-etiquette.html','theyyam-season.html','planning-theyyam-on-your-own.html','main-theyyams.html','attire-and-craft.html','cameras-and-ritual.html']:
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

# ---- glossary page (root level) ----
GL=[
('Theyyam','From the word <i>daivam</i>, god. The ritual in which the koladhari, after hours of preparation, is believed to become the deity. Also called Kaliyattam, which is more often used for the festival.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Kolam','The form of the deity that a Theyyam takes, as in <i>Theyyakkolam</i>. People speak of someone “taking the kolam”, which means bearing the deity’s form.',None,None),
('Kaliyattam','The yearly festival at a family shrine or grove in which Theyyams are held. The word is also used for Theyyam itself. Several sources note that the season runs from about late October to May.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Perumkaliyattam','A very large festival, held at long intervals, in which many Theyyams are held. Sources give different intervals; Kerala Tourism says twelve years or more.','Kerala Tourism','https://keralatourism.org/bekal/theyyam-various-types.php'),
('Ottakolam','A Theyyam that appears on its own, commonly explained as “a single kolam”, rather than together with other Theyyams. The word is often used for fire-linked forms such as Theechamundi and Vishnumoorthi, where the koladhari goes through a rite with embers. We found this meaning in a Wikipedia article and in general usage, not in a scholarly source, so please check it with a local guide.','Vishnumoorthy Theyyam','https://en.wikipedia.org/wiki/Vishnumoorthy_Theyyam'),
('Thottam and Vellattam','The first part of a Theyyam, held without full make-up or attire, with only a small red headdress. The koladhari sings or recites the story of the deity with the drummers.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Mudi','The sacred headdress. Placing it on the koladhari is described as the moment the deity enters. Night rituals may use a smaller mudi than the day ritual.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Mukhathezhuthu','Face painting, done by specialists in patterns that belong to each Theyyam, using natural colours.','Kerala Folklore: Bhairavan Theyyam','https://keralafolklore.com/bhairavan-theyyam.html'),
('Aniyara','The green room, a simple shelter near the grove where the koladhari is made up and dressed. A lamp is kept there, and in one account it is understood as the presence of God.','Polika: Theyyam rituals','https://polika.co.in/en/article/kerala/culture/theyyam/theyyam-articles/theyyam-rituals/'),
('Purappadu','Roughly “coming forth”: the moment the fully dressed deity sets out from the green room towards the shrine ground. We found this word only in a few popular sources, so its use may vary.',None,None),
('Kalasam / kalasham','A word with more than one use. In some sources it is the closing stage, when the deity departs. In another it is a vessel with offerings placed on one side of the grove. In Wikipedia’s article, <i>kalaasams</i> are the eight sets of ritual footwork.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Kuri','A mark of blessing given by the deity, described in one account as dried turmeric and rice powder. Some deities use sacred ash instead.','Polika: Theyyam rituals','https://polika.co.in/en/article/kerala/culture/theyyam/theyyam-articles/theyyam-rituals/'),
('Koladhari','The person who wears the kolam: the one through whom the deity is understood to appear.','Polika: Theyyam rituals','https://polika.co.in/en/article/kerala/culture/theyyam/theyyam-articles/theyyam-rituals/'),
('Kavu','A sacred grove or small shrine, often the setting for a Theyyam.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Tharavad','An ancestral family home. Many Theyyams are kept by a tharavad as its family deity.','Theyyam','https://en.wikipedia.org/wiki/Theyyam'),
('Madappura','A shrine of Muthappan. It has no idol or flagstaff and is open to people of all communities.','Muthappan','https://en.wikipedia.org/wiki/Muthappan'),
('Banku','The Muslim call to prayer. Some Mappila Theyyams begin with it.','Mappila Theyyam','https://en.wikipedia.org/wiki/Mappila_Theyyam'),
]
gdesc='Plain-English meanings of Theyyam words you will hear in North Malabar: kaliyattam, perumkaliyattam, ottakolam, thottam, mudi, kavu and more.'
ld=[bc([("Home",""),("Theyyam words explained","theyyam-glossary.html")]),{"@type":"DefinedTermSet","name":"Theyyam words explained","hasDefinedTerm":[{"@type":"DefinedTerm","name":n,"description":re.sub('<[^>]+>','',d)} for n,d,_,_ in GL]}]
g=head('Theyyam Words Explained: Kaliyattam, Ottakolam, Mudi & More | LGFC Theyyam',gdesc,'theyyam-glossary.html',ld,'p-headdress-tall.jpg')
# root-level page: undo the ../ prefixes used by theyyams/ pages
g=g.replace('{B}assets/theyyam/','')  # no-op safety
g=g.replace(B+'assets/theyyam/p-headdress-tall.jpg',B+'assets/p-headdress-tall.jpg')
g+=header.replace(' aria-current="page" style="color:#D7261E"','')+'\n<main id="main"><article><div class="w"><div class="art sec">\n<nav aria-label="Breadcrumb" style="font-size:14px;margin:24px 0 18px"><a href="index.html">Home</a> / Theyyam words explained</nav>\n<h1>Theyyam words explained</h1><p style="font-size:1.15em;font-weight:500;margin-top:18px">The words you will hear around a ritual in North Malabar, in plain English. Meanings can vary by shrine and family, so treat these as a starting point and ask your guide.</p>\n'
for n,d,sn,su in GL:
    g+=f'<h2 id="{re.sub("[^a-z]","-",n.lower())}">{n}</h2><p>{d}'+(f' <span style="font-size:13px;opacity:.75">Source: <a href="{su}" rel="noopener">{E(sn)}{" (Wikipedia)" if "wikipedia" in su else ""}</a>.</span>' if sn else '')+'</p>\n'
g+='<div class="cta" style="margin-top:36px"><h3>Hear the stories in person</h3><p>Our guided trips explain each word and each deity as you see it. <a href="theyyams/">Browse the Theyyams</a> or enquire about a trip.</p><a class="btn" href="enquire.html">Enquire about a trip</a></div>\n</div></div></article></main>\n'+footer+'\n<script src="assets/search.js" defer></script>\n</body>\n</html>\n'
open('theyyam-glossary.html','w').write(g)
sm=open('sitemap.xml').read()
if B+'theyyam-glossary.html' not in sm: sm=sm.replace('</urlset>',f'<url><loc>{B}theyyam-glossary.html</loc></url>\n</urlset>')
open('sitemap.xml','w').write(sm)

# ---- link Theyyam names inside journal posts (root pages) ----
POSTS=['steps-of-a-theyyam.html','what-is-theyyam.html','theyyam-etiquette.html','theyyam-season.html','planning-theyyam-on-your-own.html','main-theyyams.html','attire-and-craft.html','cameras-and-ritual.html']
for f in POSTS:
    s=open(f).read();used=set(re.findall(r'href="theyyams/([a-z-]+)\.html"',s))
    def fix(m):
        tokens=re.split(r'(<[^>]+>)',m.group(2));depth=0;res=[]
        for tok in tokens:
            if tok.startswith('<'):
                if re.match(r'<a[\s>]',tok): depth+=1
                elif tok=='</a>': depth=max(0,depth-1)
                res.append(tok);continue
            if depth or not tok.strip(): res.append(tok);continue
            pos=0;out=[]
            for mm in _re.finditer(tok):
                sl=_tmap[mm.group(1)]
                if sl in used: continue
                used.add(sl);out.append(tok[pos:mm.start()]);out.append(f'<a href="theyyams/{sl}.html">{mm.group(1)}</a>');pos=mm.end()
            out.append(tok[pos:]);res.append(''.join(out))
        return m.group(1)+''.join(res)+m.group(3)
    head_,sep,body_=s.partition('<main id="main">')
    body_=re.sub(r'(<(?:p|li)(?:\s[^>]*)?>)(.*?)(</(?:p|li)>)',fix,body_,flags=re.S)
    open(f,'w').write(head_+sep+body_)
