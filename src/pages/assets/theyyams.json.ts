import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import categories from '../../data/theyyam-categories.json';

// Search index for the header search and the /theyyams/ filter (assets/search.js reads this file).
export const GET: APIRoute = async () => {
  const all = (await getCollection('theyyams')).sort((a, b) => a.data.order - b.data.order);
  const unmd = (s: string) => s.replace(/\\([*_\[\]<>`{}\\])/g, '$1').trim();
  const idx = all.map(({ data: t, body }) => ({
    s: t.slug, n: t.name, m: t.ml, c: t.category, cl: categories.find((c) => c.key === t.category)!.label,
    t: t.tagline, a: t.alias, g: t.tags, f: t.photos[0]?.file ?? '',
    x: unmd(body!.match(/## Who is .*?\n\n([\s\S]*?)\n\n## The story/)?.[1] ?? '').slice(0, 240),
  }));
  return new Response(JSON.stringify(idx), { headers: { 'Content-Type': 'application/json' } });
};
