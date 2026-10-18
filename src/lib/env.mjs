// Shared by astro.config.mjs and the remark plugin (plain ESM so Node can load it before Astro starts).
export const site = (process.env.SITE || 'https://aadishajay.github.io').replace(/\/$/, '');
export const base = (process.env.BASE || '/theyyam-site').replace(/\/$/, '');
export const u = (p = '') => `${base}/${String(p).replace(/^\//, '')}`;
