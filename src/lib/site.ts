// Site-wide URL helpers. SITE and BASE come from astro.config.mjs (env-driven), so the same code
// builds the GitHub Pages review site and the launch domain.
export const SITE = (import.meta.env.SITE as string).replace(/\/$/, '');
export const BASE = ((import.meta.env.BASE_URL as string) || '/').replace(/\/$/, '');
/** true only when the site is ready to be indexed: INDEXABLE=1 npm run build */
export const INDEXABLE = process.env.INDEXABLE === '1';

/** site path (adds the base), e.g. u('trips.html') -> /theyyam-site/trips.html ; u() -> /theyyam-site/ */
export const u = (p = '') => `${BASE}/${p.replace(/^\//, '')}`;
/** absolute URL for a site path */
export const abs = (p = '') => `${SITE}${u(p)}`;

export const LANGS = ['en', 'de', 'fr', 'es'] as const;
export type Lang = (typeof LANGS)[number];
export const LOCALE: Record<Lang, string> = { en: 'en_GB', de: 'de_DE', fr: 'fr_FR', es: 'es_ES' };
export const HOME_PATH: Record<Lang, string> = { en: '', de: 'de/', fr: 'fr/', es: 'es/' };
