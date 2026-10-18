import terms from '../data/theyyam-terms.json';

const list = [...new Set(Object.entries(terms as Record<string, string[]>).flatMap(([slug, ts]) => ts.map((t) => JSON.stringify([t, slug]))))]
  .map((x) => JSON.parse(x) as [string, string])
  .sort((a, b) => b[0].length - a[0].length);
const byTerm = Object.fromEntries(list);
const re = new RegExp('(?<![A-Za-z])(' + list.map(([t]) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![A-Za-z])', 'g');
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** escape plain text and link the first mention of each other Theyyam (used for the short fact lines) */
export function linkify(text: string, selfSlug: string, used = new Set<string>()): string {
  let out = '', pos = 0;
  for (const m of text.matchAll(re)) {
    const slug = byTerm[m[1]];
    if (slug === selfSlug || used.has(slug)) continue;
    used.add(slug);
    out += esc(text.slice(pos, m.index)) + `<a href="${slug}.html">${esc(m[1])}</a>`;
    pos = m.index! + m[1].length;
  }
  return out + esc(text.slice(pos));
}
