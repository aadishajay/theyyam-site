// Custom blocks for blog and Theyyam Markdown, plus automatic links between Theyyam pages.
//
//   :::quote ... :::                     pull quote
//   :::caption ... :::   :::aside ... :::   :::sources ... :::
//   ::cta{title="" text="" label="" href="enquire.html" spaced}   call-to-action box
//   ::figure{src="" alt="" width=1000 height=563}                 wide image (src is under /assets/)
//   ::faq                                 "Quick answers" accordion from the front matter `faq`
//   ::gallery                             Theyyam photo gallery + photo credits (front matter `photos`)
//   ::gloss                               koladhari hint (only when front matter `koladhari: true`)
//   :::note ... :::                       Theyyam visitor note (adds the photography reminder)
//
// When front matter has `kind: theyyam`, the first mention of every other Theyyam in the text is linked
// to its page (term list: src/data/theyyam-terms.json).
import { visit, SKIP } from 'unist-util-visit';
import { readFileSync } from 'node:fs';
import { u } from '../lib/env.mjs';

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const html = (value) => ({ type: 'html', value });
const mdInline = (s) => esc(s).replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>').replace(/\*([^*]+)\*/g, '<i>$1</i>');

let terms;
function loadTerms() {
  if (terms) return terms;
  const map = JSON.parse(readFileSync(new URL('../data/theyyam-terms.json', import.meta.url), 'utf8')); // slug -> [terms]
  const list = [...new Set(Object.entries(map).flatMap(([slug, ts]) => ts.map((t) => [t, slug])).map(JSON.stringify))].map(JSON.parse).sort((a, b) => b[0].length - a[0].length);
  const byTerm = Object.fromEntries(list);
  const re = new RegExp('(?<![A-Za-z])(' + list.map(([t]) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![A-Za-z])', 'g');
  terms = { re, byTerm };
  return terms;
}

export default function remarkBlocks() {
  return (tree, file) => {
    const fm = file.data?.astro?.frontmatter ?? {};

    // 1) directives -> raw HTML / wrapped content
    visit(tree, (node, index, parent) => {
      if (!['containerDirective', 'leafDirective'].includes(node.type)) return;
      const a = node.attributes ?? {};
      let out;
      switch (node.name) {
        case 'quote': out = [html('<div class="q">'), ...node.children, html('</div>')]; break;
        case 'caption': out = [html('<div class="cap">'), ...node.children, html('</div>')]; break;
        case 'aside': out = [html('<div class="aside">'), ...node.children, html('</div>')]; break;
        case 'sources': out = [html('<div class="srcs">'), ...node.children, html('</div>')]; break;
        case 'note': {
          const last = node.children[node.children.length - 1];
          if (last?.type === 'paragraph') last.children.push({ type: 'text', value: ' Photography and video are not allowed at some rituals, so ask your guide first.' });
          out = [html('<div class="note"><b>A note for visitors</b>'), ...node.children, html('</div>')];
          break;
        }
        case 'cta':
          out = [html(`<div class="cta"${a.spaced !== undefined ? ' style="margin-top:32px"' : ''}><h3>${esc(a.title ?? 'See it with someone who knows the family')}</h3><p>${esc(a.text ?? 'Our guided trips arrange access and explain every step, so you can simply be present and listen.')}</p><a class="btn" href="${u(a.href ?? 'enquire.html')}">${esc(a.label ?? 'Enquire about a trip')}</a></div>`)];
          break;
        case 'figure':
          out = [html(`<img src="${u('assets/' + a.src)}" alt="${esc(a.alt)}" width="${a.width}" height="${a.height}" class="fig" />`)];
          break;
        case 'faq': {
          const items = fm.faq ?? [];
          out = [html(items.map((f) => `<details><summary><h3>${esc(f.q)}</h3></summary><p style="margin-top:0">${mdInline(f.a)}</p></details>`).join(''))];
          break;
        }
        case 'gallery': {
          const photos = fm.photos ?? [];
          const alts = [`${fm.name} Theyyam in ritual attire`, `Close view of the ${fm.name} Theyyam face and headdress`, `${fm.name} Theyyam during a ritual in North Malabar, Kerala`];
          let h = '';
          if (photos.length > 1)
            h += '<div class="gal">' + photos.slice(1, 3).map((c, i) => `<figure><img src="${u('assets/theyyam/' + c.file)}" alt="${esc(alts[i + 1])}" width="${c.w}" height="${c.h}" loading="lazy" /><figcaption>Photo: ${esc(c.artist)}, ${esc(c.lic)}, via Wikimedia Commons</figcaption></figure>`).join('') + '</div>';
          if (photos.length) h += `<p style="font-size:12px;opacity:.7;margin:-12px 0 20px">Hero photo: ${esc(photos[0].artist)}, ${esc(photos[0].lic)}, via Wikimedia Commons</p>`;
          out = h ? [html(h)] : [];
          break;
        }
        case 'gloss':
          out = fm.koladhari ? [html(`<p style="font-size:13px;opacity:.75;margin-top:-4px">Koladhari: the person who takes on the kolam, the deity’s form. See <a href="${u('theyyam-glossary.html#koladhari')}">Theyyam words explained</a>.</p>`)] : [];
          break;
        default: return;
      }
      parent.children.splice(index, 1, ...out);
      return [SKIP, index + out.length];
    });

    // 2) auto-link the first mention of each other Theyyam
    if (fm.kind === 'theyyam') {
      const { re, byTerm } = loadTerms();
      const used = new Set();
      visit(tree, (node, index, parent) => {
        if (['link', 'heading', 'html', 'code', 'inlineCode'].includes(node.type)) return SKIP;
        if (node.type !== 'text') return;
        const text = node.value; let pos = 0; const out = [];
        for (const m of text.matchAll(re)) {
          const slug = byTerm[m[1]];
          if (slug === fm.slug || used.has(slug)) continue;
          used.add(slug);
          if (m.index > pos) out.push({ type: 'text', value: text.slice(pos, m.index) });
          out.push({ type: 'link', url: `${slug}.html`, children: [{ type: 'text', value: m[1] }] });
          pos = m.index + m[1].length;
        }
        if (!out.length) return;
        if (pos < text.length) out.push({ type: 'text', value: text.slice(pos) });
        parent.children.splice(index, 1, ...out);
        return [SKIP, index + out.length];
      });
    }
  };
}
