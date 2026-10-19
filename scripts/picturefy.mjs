// After scripts/make-webp.sh: wrap each <img src="x.jpg|png"> in <picture> with a WebP <source> when x.jpg.webp exists.
// The page's own CSS is unaffected because <picture> is display:contents (set in Base.astro).
import { readdirSync, readFileSync, writeFileSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { base } from '../src/lib/env.mjs';

const dist = 'dist';
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
  html = html.replace(/(<picture[^>]*>\s*(?:<source[^>]*>\s*)*)?(<img\b[^>]*>)/g, (m, pre, img) => {
    if (pre) return m; // already inside a <picture>
    const src = /\ssrc="([^"]+)"/.exec(img)?.[1];
    if (!src || !/\.(jpe?g|png)$/i.test(src) || /^https?:/.test(src)) return m;
    const rel = src.startsWith(base + '/') ? src.slice(base.length) : src;
    if (!existsSync(join(dist, rel + '.webp'))) return m;
    wrapped++; changed = true;
    return `<picture><source srcset="${src}.webp" type="image/webp">${img}</picture>`;
  });
  if (changed) { writeFileSync(file, html); pages++; }
}
walk(dist);
console.log(`picture: ${wrapped} images wrapped on ${pages} pages`);
