import type { APIRoute } from 'astro';
import { abs } from '../lib/site';

export const GET: APIRoute = () =>
  new Response(`User-agent: *\nAllow: /\nSitemap: ${abs('sitemap.xml')}\n`, { headers: { 'Content-Type': 'text/plain' } });
