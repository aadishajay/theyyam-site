// After scripts/make-webp.sh: wrap each <img src="x.jpg|png"> in <picture> with a WebP <source> when x.jpg.webp exists.
// The page's own CSS is unaffected because <picture> is display:contents (set in Base.astro).
import { readdirSync, readFileSync, writeFileSync, statSync, unlinkSync } from 'node:fs';
import { join } from 'node:path';
import { base } from '../src/lib/env.mjs';

const dist = 'dist';
const manifest = JSON.parse(readFileSync(join(dist, '.webp-manifest.json'), 'utf8'));
let pages = 0, wrapped = 0;
const walk = (d) => {
  for (const f of readdirSync(d)) {
    const p = join(d, f);
    if (statSync(p).isDirectory()) walk(p);
    else if (f.endsWith('.html')) fix(p);
  }
};
function fix(file) {
  let html = readFileSync(file, 'utf8');
  let changed = false;
  let seen = 0;
  html = html.replace(/(<picture[^>]*>\s*(?:<source[^>]*>\s*)*)?(<img\b[^>]*>)/g, (m, pre, img0) => {
    let img = img0;
    if (pre) return m; // already inside a <picture>
    const src = /\ssrc="([^"]+)"/.exec(img)?.[1];
    if (!src || !/\.(jpe?g|png)$/i.test(src) || /^https?:/.test(src)) return m;
    const rel = src.startsWith(base + '/') ? src.slice(base.length) : src;
    const e = manifest[rel];
    if (!e) return m;
    const stem = `${src}.${e.hash}`;
    const srcset = e.variants.length
      ? e.variants.map((v) => `${stem}-${v}.webp ${v}w`).concat(`${stem}.webp ${e.w}w`).join(', ')
      : `${stem}.webp`;
    const sizes = e.variants.length ? ' sizes="(max-width: 700px) 92vw, 560px"' : '';
    // The first image on a page is the likely LCP image: keep it eager. Every later image waits until it is near the viewport.
    if (seen++ > 0 && !/\sloading=/.test(img)) img = img.replace(/<img\b/, '<img loading="lazy" decoding="async"');
    wrapped++; changed = true;
    return `<picture><source srcset="${srcset}"${sizes} type="image/webp">${img}</picture>`;
  });
  if (changed) { writeFileSync(file, html); pages++; }
}
walk(dist);
unlinkSync(join(dist, '.webp-manifest.json'));
console.log(`picture: ${wrapped} images wrapped on ${pages} pages`);
