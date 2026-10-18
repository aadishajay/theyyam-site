"""Generates steps-of-a-theyyam.html from the etiquette post as a template. Run from the website folder, then run tools/build_theyyams.py to interlink."""
import re,json,html
B='https://aadishajay.github.io/theyyam-site/'
T=open('theyyam-etiquette.html').read()
E=lambda s:html.escape(s,quote=True)
title='The steps of a Theyyam: thottam, vellattam, purappadu and more explained'
desc='The stages of a Theyyam ritual in order, with meanings: aniyara, thottam, vellattam, mudi, purappadu, kalasham, kuri and more, in plain English.'
lead='A Theyyam is not one dance but a sequence of steps, each with its own name. Knowing them helps you follow what is happening and when to stay quietly at the edge. Names, order and length vary by shrine, family and deity, so please treat this as a general outline and ask your guide how it goes at the place you visit.'
S=[
('Before anything begins: preparation and the aniyara',[
 'The performer prepares by fasting and keeping to certain rules. How long this lasts varies, with sources giving anything from a few days to longer. On the day, the performer is made ready in the <i>aniyara</i>, the green room, which is often a simple thatched shelter near the grove. A lamp is kept there, and in one account the lamp is understood as the presence of God, to which the performer prays before performing.']),
('Permission and the opening bow',[
 'In the account we read, the performer walks to the centre of the grove, bows to the eight directions and receives a small offering from the priest, a banana leaf with rice, betel nut and sandal paste, which gives permission to perform. This is sometimes called <i>kodiyila vangal</i>.']),
('Thottam and vellattam: the invocation',[
 'The first public part is called <i>thottam</i> or <i>vellattam</i>. The performer wears only a small red headdress and no full make-up or costume. With the drummers, the performer sings or recites the deity’s story. The song itself is called <i>thottam pattu</i>, and it is sung before the Theyyam begins, often while the performer is being made up, to invoke the deity.',
 'Kerala Tourism describes vellattam as an invocative ritual held before the actual Theyyam, equivalent to the thottam chant but more vibrant and vigorous. Many sources use the two words together or interchangeably, and some use them for slightly different things, so you may hear them both.']),
('Mukhathezhuthu and vesham: face and costume',[
 'After a short break the performer returns to the green room, and specialists and other performers apply the face painting, <i>mukhathezhuthu</i>, and the costume, <i>vesham</i>. Each Theyyam has its own face pattern, made with natural colours. Named patterns include <i>kattaram</i>, <i>kozhipushpam</i> and <i>prakkezhuthu</i>. The costume is built from natural materials such as tender coconut leaf, wood and cloth. The whole process can take many hours.']),
('The mudi: the deity arrives',[
 'The most important moment is the placing of the <i>mudi</i>, the tall headdress. Sources describe it as the point at which the deity is understood to enter the performer. In several accounts, the performer sits on a pedestal while the drums begin, looks into a mirror and then the mudi is placed. After this, the performer is treated as the deity, and the priest and devotees welcome the god.']),
('Purappadu: coming forth',[
 '<i>Purappadu</i> means roughly “coming forth”, and it is the word used for the moment when the fully dressed deity sets out from the green room towards the shrine ground. We found this term only in a few popular sources and not in the scholarly ones we could read, so its use may differ between places.']),
('Kalasams: the dance',[
 'The deity then circles the shrine, runs through the courtyard and dances, to the sound of the chenda, kuzhal and other instruments. The dance is built from set footwork patterns called <i>kalasams</i>, repeated in order up to the eighth step. Many deities carry a sword and a shield.']),
('Offerings and the kalasham',[
 'In one account, offerings such as flowers, beaten rice, coconut and appam are laid out on a floor on the north side of the grove, with a vessel called a <i>kalasham</i> among them. Some shrines have additional rites there, which differ between deities and places. Be aware that the word is also used differently. In other sources <i>kalasam</i> means the closing stage, when the deity departs, and in the Wikipedia article on Theyyam the plural <i>kalaasams</i> means the dance steps above. Context tells you which is meant.']),
('Blessing and kuri',[
 'The part most visitors remember is the blessing. The deity speaks to devotees, listens to their troubles and may answer questions. In one account the deity gives a mark called <i>kuri</i>, a mixture of dried turmeric and rice powder. Some deities use sacred ash instead. Devotees receive it with respect.']),
('Shared food and the farewell',[
 'At some shrines devotees share food offered from the grove. Then comes the farewell. The deity departs, and the performer gradually sheds the divine role. Some traditions have a closing rite days afterwards, when the grounds are cleaned.']),
('A note on Mudiyettu',[
 'You may also hear of <i>Mudiyettu</i>. It is a different ritual theatre of Kerala telling the battle of the goddess Kali and the demon Darika. It is not a stage of a Theyyam.']),
]
faq=[('What is thottam in Theyyam?','Thottam is the invocation, a ritual song that tells the deity’s story, sung before the full Theyyam. The performer wears only a small red headdress while it is performed.'),
('What is vellattam?','Vellattam, also called vellattu, is an invocative ritual held before the actual Theyyam. Kerala Tourism describes it as equivalent to the thottam chant and more vibrant.'),
('What is purappadu in Theyyam?','The word means “coming forth”. It is used for the moment when the fully dressed deity comes out of the green room and sets out towards the shrine ground.'),
('How long does a Theyyam last?','A deity’s performance is described as lasting from twelve to twenty-four hours with intervals, and the preparation alone can take many hours. It varies with the deity and the shrine.')]
sources=[('Theyyam','https://en.wikipedia.org/wiki/Theyyam'),('Thottam Pattu','https://en.wikipedia.org/wiki/Thottam_Pattu'),('Kerala Tourism: Theyyam performance','https://www.keralatourism.org/bekal/theyyam-performance.php'),('Polika: Theyyam rituals','https://polika.co.in/en/article/kerala/culture/theyyam/theyyam-articles/theyyam-rituals/'),('Kerala Folklore: Theyyam','https://keralafolklore.com/kerala-theyyam.html')]
slug='steps-of-a-theyyam.html'
head,rest=T.split('<main id="main">',1)
tail=rest.split('</article>',1)[1]
h=re.sub(r'<title>.*?</title>',f'<title>{E(title)} | LGFC Theyyam</title>',head,1)
h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{E(desc)}">',h,1)
h=re.sub(r'<meta property="og:title" content="[^"]*"><meta property="og:description" content="[^"]*"><meta property="og:url" content="[^"]*">',f'<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{B}{slug}">',h,1)
m=re.search(r'<script type="application/ld\+json">(.*?)</script>',h,re.S)
j=json.loads(m.group(1));org=j['@graph'][:2]
ld=org+[{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":B+u} for i,(n,u) in enumerate([("Home",""),("Journal","journal.html"),("The steps of a Theyyam",slug)])]},
 {"@type":"Article","headline":title,"description":desc,"author":{"@id":B+"#org"},"publisher":{"@id":B+"#org"},"mainEntityOfPage":B+slug,"image":B+"assets/p-body-paint.jpg","about":{"@type":"Thing","name":"Theyyam ritual stages"}},
 {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
h=h[:m.start()]+'<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False)+'</script>'+h[m.end():]
art=f'''<main id="main"><article>
<div class="w" style="padding-top:32px">
<div class="art">
<nav aria-label="Breadcrumb" style="font-size:14px;margin-bottom:18px"><a href="index.html">Home</a> / <a href="journal.html">Journal</a> / Culture</nav>
<p class="k" style="margin-bottom:10px">Culture · 8 min read</p>
<h1>{E(title)}</h1>
<p style="margin:20px 0 0;font-size:15px;opacity:.75">By [AUTHOR NAME] · Updated [DATE] · LGFC local guides</p>
</div>
<img src="assets/p-body-paint.jpg" alt="A performer having face paint applied in the green room before a Theyyam" width="1200" height="675" style="width:100%;max-width:1100px;margin:28px auto 0;border-radius:28px;aspect-ratio:16/9;object-fit:cover">
</div>
<div class="w"><div class="art">
<p style="font-size:1.15em;margin-top:32px;font-weight:500">{lead}</p>
<div class="toc"><b>In this guide</b><ol>'''+''.join(f'<li><a href="{slug}#s{i}">{E(n)}</a></li>' for i,(n,_) in enumerate(S))+'<li><a href="'+slug+'#faq">Quick answers</a></li></ol></div>\n'
for i,(n,ps) in enumerate(S):
    art+=f'<h2 id="s{i}">{E(n)}</h2>\n'+''.join(f'<p>{p}</p>\n' for p in ps)
art+='<h2 id="faq">Quick answers</h2>\n'+''.join(f'<details><summary><h3>{E(q)}</h3></summary><p style="margin-top:0">{E(a)}</p></details>\n' for q,a in faq)
art+='<p style="font-size:14px;margin-top:28px">New to the words? See <a href="theyyam-glossary.html">Theyyam words explained</a>, and our guide to <a href="theyyam-etiquette.html">etiquette</a>. Photography and video are not allowed at some rituals, so ask your guide first.</p>\n'
art+='<div class="cta" style="margin-top:32px"><h3>See it with someone who knows the family</h3><p>Our guided trips explain each step as it happens, so you can simply watch and listen.</p><a class="btn" href="enquire.html">Enquire about a trip</a></div>\n'
art+='<p class="srcs" style="font-size:13px;opacity:.8;margin-top:28px"><b>Sources and further reading:</b> '+', '.join(f'<a href="{u}" rel="noopener">{E(n)}</a>' for n,u in sources)+'. Stage names and their order vary by shrine, family and deity. We also used Kerala Tourism’s “Dance of the Divine” ebook for the vellattam definition. Wikipedia and popular sources were used, and we could not open some scholarly articles, so please have a knowledgeable person review this before launch.</p>\n'
art+='</div></div>\n</article>'
kr='''<section style="padding:64px 0 72px"><div class="w">
<h2 style="margin:0 0 24px">Keep reading</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px">
<a class="pc" href="theyyam-etiquette.html"><img src="assets/p-portrait-dark.jpg" alt="Portrait of a Theyyam performer in red and gold face paint" width="600" height="400"><p class="k" style="margin:12px 0 0">Etiquette</p><h3>Theyyam etiquette: do’s and don’ts for visitors</h3></a>
<a class="pc" href="costume-and-craft.html"><img src="assets/p-gold-detail.jpg" alt="Gold and red ornaments of a handmade Theyyam costume" width="600" height="400"><p class="k" style="margin:12px 0 0">Culture</p><h3>Costume and craft: how a Theyyam is made</h3></a>
<a class="pc" href="theyyam-glossary.html"><img src="assets/p-drum-crowd.jpg" alt="A Theyyam performer dancing beside a drummer" width="600" height="400"><p class="k" style="margin:12px 0 0">Culture</p><h3>Theyyam words explained</h3></a>
</div></div></section>
</main>'''
t2=re.sub(r'\n<section style="padding:64px 0 72px">.*?</main>','\n'+kr,tail,flags=re.S)
open(slug,'w').write(h+art+t2)
print('ok',len(h+art+t2))
