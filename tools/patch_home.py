"""Replaces the homepage hero image with a slow crossfade of Theyyam faces (assets/faces/*.jpg). Idempotent."""
import re,json,sys,html
sys.path.insert(0,'tools')
import theyyams_data as d
names={t['slug']:t['name'] for t in d.T}
order=['vishnumoorthi','kundora-chamundi','gulikan','muchilot-bhagavathi']  # hand-built vector faces, see tools/build_face_svgs.py
import os
order=[s for s in order if os.path.exists(f'assets/faces-svg/{s}.svg')]
E=html.escape
slides=''
for i,s in enumerate(order):
    n=names[s]
    img=f'<img src="assets/faces-svg/{s}.svg" alt="Illustrated face of a Theyyam" width="400" height="500"'+('' if i==0 else ' loading="lazy"')+'>'
    slides+=f'<div class="fslide{" on" if i==0 else ""}"'+('' if i==0 else ' aria-hidden="true"')+f'>{img}</div>'
block=f'''<!--faces:start-->
<div class="faces" role="group" aria-label="Faces of the Theyyams in our guide"><div class="fstack">{slides}</div></div>
<!--faces:end-->'''
css='''.strip span{display:inline-block;padding-left:100%;animation:strip-run 20s linear infinite}.strip:hover span{animation-play-state:paused}@keyframes strip-run{to{transform:translateX(-100%)}}@media(prefers-reduced-motion:reduce){.strip{text-align:center;white-space:normal}.strip span{padding-left:0;animation:none}}
.fstack{position:relative;width:100%;max-width:460px;aspect-ratio:4/5;border-radius:999px 999px 24px 24px;border:6px solid #FFB400;margin:0 auto;overflow:hidden;background:#4A0E12}
.fslide{position:absolute;inset:0;display:block;opacity:0;transition:opacity 1.6s ease-in-out}
.fslide.on{opacity:1;z-index:1}
.fslide img{width:100%;height:100%;object-fit:cover;transform:scale(1.07);transition:transform 7s ease-out}
.fslide.on img{transform:scale(1)}
@media(prefers-reduced-motion:reduce){.fslide,.fslide img{transition:none}.fslide img{transform:none}}'''
js='''<script>
(function(){var st=document.querySelector('.fstack');if(!st)return;var s=[].slice.call(st.querySelectorAll('.fslide')),n=s.length,i=0,timer=null;
if(n<2||window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
function load(k){var im=s[k%n].querySelector('img');if(im&&im.loading==='lazy'){im.loading='eager';}}
function show(k){var o=s[i],c=s[k];o.classList.remove('on');o.setAttribute('aria-hidden','true');c.classList.add('on');c.removeAttribute('aria-hidden');i=k;load(k+1);}
function next(){show((i+1)%n);}
function start(){if(!timer&&!document.hidden)timer=setInterval(next,3800);}
function stop(){clearInterval(timer);timer=null;}
load(1);load(2);
st.parentNode.addEventListener('mouseenter',stop);st.parentNode.addEventListener('mouseleave',start);st.parentNode.addEventListener('focusin',stop);st.parentNode.addEventListener('focusout',start);
document.addEventListener('visibilitychange',function(){document.hidden?stop():start();});
if('IntersectionObserver' in window){new IntersectionObserver(function(e){e[0].isIntersecting?start():stop();},{threshold:.2}).observe(st);}else{start();}
})();
</script>'''
s=open('index.html').read()
if '<!--faces:start-->' in s:
    s=re.sub(r'<!--faces:start-->.*?<!--faces:end-->',block,s,flags=re.S)
    s=re.sub(r'<style id="faces-css">.*?</style>','<style id="faces-css">'+css+'</style>',s,flags=re.S)
    s=re.sub(r'<script id="faces-js">.*?</script>','',s,flags=re.S)
else:
    old=re.search(r'<div style="position:relative;width:100%"><img class="arch" src="assets/lgfc-headdress-portrait.jpg"[^>]*></div>',s)
    assert old
    s=s.replace(old.group(0),block,1)
    s=s.replace('</head>','<style id="faces-css">'+css+'</style>\n</head>',1)
js=js.replace('<script>','<script id="faces-js">',1)
s=re.sub(r'<script id="faces-js">.*?</script>','',s,flags=re.S)
s=s.replace('</body>',js+'\n</body>',1)
open('index.html','w').write(s)
print('patched',len(order),'faces')
