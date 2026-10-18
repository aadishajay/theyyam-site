"""Crops same-size face portraits (4:5, 480x600) for the homepage rotation into assets/faces/.
Reads tools/face_specs.json (centre as fractions of the source image, crop width as a fraction of source width).
Small faces are re-fetched at higher resolution from Wikimedia Commons (credits.json holds the file page)."""
import json,os,re,urllib.request,urllib.parse,time,io
from PIL import Image
UA={'User-Agent':'LGFCTheyyamResearch/1.0 (letsgoforacamp@gmail.com)'}
specs=json.load(open('tools/face_specs.json'));cred=json.load(open('tools/credits.json'))
os.makedirs('assets/faces',exist_ok=True);os.makedirs('/tmp/hires',exist_ok=True)
def page_of(fn):
    for L in cred.values():
        for c in L:
            if c['file']==fn: return c
def hires(fn):
    p='/tmp/hires/'+fn
    if os.path.exists(p): return p
    c=page_of(fn);title=urllib.parse.unquote(c['page'].split('/wiki/')[1])
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','titles':title,'prop':'imageinfo','iiprop':'url','iiurlwidth':2200,'format':'json'})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
    ii=list(d['query']['pages'].values())[0]['imageinfo'][0]
    for t in range(6):
        try: data=urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=UA)).read();break
        except Exception: time.sleep(5*(t+1))
    open(p,'wb').write(data);time.sleep(1.5);return p
out=[]
for s in specs:
    src=hires(s['file']) if s['hires'] else 'assets/theyyam/'+s['file']
    im=Image.open(src).convert('RGB');w,h=im.size
    cw=s['cw']*w;ch=cw*1.25
    if ch>h: ch=h;cw=ch/1.25
    l=min(max(0,s['cx']*w-cw/2),w-cw);t=min(max(0,s['cy']*h-ch/2),h-ch)
    im=im.crop((int(l),int(t),int(l+cw),int(t+ch))).resize((480,600),Image.LANCZOS)
    im.save(f'assets/faces/{s["slug"]}.jpg',quality=78,optimize=True,progressive=True)
    out.append(s['slug'])
print(len(out),'faces')
