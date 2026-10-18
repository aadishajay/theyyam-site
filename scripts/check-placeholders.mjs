// Lists [PLACEHOLDER] text left in the built pages. In a launch build (INDEXABLE=1) any placeholder fails the deploy.
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const re = /\[(?:[A-Z][A-Z0-9 ·.,&'\/-]{2,}|Name|Country|Trip name and place|Month year)\]/g;
const hits = new Map();
const walk = (d) => {
  for (const f of readdirSync(d)) {
    const p = join(d, f);
    if (statSync(p).isDirectory()) walk(p);
    else if (f.endsWith('.html')) {
      const text = readFileSync(p, 'utf8').replace(/<script[\s\S]*?<\/script>/g, '');
      for (const m of text.matchAll(re)) hits.set(m[0], (hits.get(m[0]) ?? new Set()).add(p.replace('dist/', '')));
    }
  }
};
walk('dist');
if (!hits.size) { console.log('No placeholders left.'); process.exit(0); }
console.log('Placeholders still on the site:');
for (const [k, pages] of [...hits].sort()) console.log(`  ${k}  (${pages.size} pages)`);
if (process.env.INDEXABLE === '1') { console.error('\nLaunch build blocked: fill these first.'); process.exit(1); }
