#!/usr/bin/env python3
"""Write WebP versions of every .jpg/.png under dist/ and a manifest for scripts/picturefy.mjs.

  name.jpg  ->  name.jpg.<hash>.webp          main size (capped at 720 px wide for images up to 900 px, else full size)
             ->  name.jpg.<hash>-480.webp      small variant (images wider than 600 px)
             ->  name.jpg.<hash>-800.webp      medium variant (images wider than 900 px)
<hash> is taken from the original file, so replacing an image gives it a new URL and the one-year cache can never serve a stale copy.
A WebP is kept only if it is smaller than the original. (Hostinger's CDN converts images on its own, but its files are often larger.)"""
import hashlib, json, subprocess
from pathlib import Path
from PIL import Image

dist = Path(__file__).resolve().parent.parent / 'dist'
manifest, saved, n = {}, 0, 0

def enc(src: Path, out: Path, q: int, width: int | None = None) -> bool:
    cmd = ['cwebp', '-quiet', '-q', str(q), '-m', '6', '-mt', str(src), '-o', str(out)]
    if width: cmd[1:1] = ['-resize', str(width), '0']
    return subprocess.run(cmd, capture_output=True).returncode == 0 and out.exists()

for f in sorted(dist.rglob('*')):
    if f.suffix.lower() not in ('.jpg', '.jpeg', '.png') or not f.is_file(): continue
    rel = '/' + f.relative_to(dist).as_posix()
    with Image.open(f) as im: w, h = im.size
    h8 = hashlib.sha1(f.read_bytes()).hexdigest()[:8]
    base = f'{f}.{h8}'
    main_w = min(w, 720) if w <= 900 else w
    full = Path(base + '.webp')
    if not enc(f, full, 70 if w <= 900 else 72, main_w if main_w < w else None) or full.stat().st_size >= f.stat().st_size:
        full.unlink(missing_ok=True); continue
    saved += f.stat().st_size - full.stat().st_size; n += 1
    entry = {'hash': h8, 'w': main_w, 'variants': []}
    for v in ([480, 800] if w > 900 else [480] if w > 600 else []):
        if v >= main_w: continue
        small = Path(f'{base}-{v}.webp')
        if enc(f, small, 68, v) and small.stat().st_size < full.stat().st_size: entry['variants'].append(v)
        else: small.unlink(missing_ok=True)
    manifest[rel] = entry

(dist / '.webp-manifest.json').write_text(json.dumps(manifest))
print(f'webp: {n} files, saved {saved // 1024} KB')
