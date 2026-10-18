import { abs, HOME_PATH, type Lang } from './site';
import { landingMeta } from '../i18n/landing-meta';
import { landing } from '../i18n/landing';
import { heroSlides } from '../data/hero';
import { orgNode, websiteNode, breadcrumb, faqNode } from './schema';

const plain = (s: string) => s.replace(/<[^>]+>/g, '');

/** JSON-LD blocks for the landing page of a language */
export function landingLd(lang: Lang) {
  const m = landingMeta[lang];
  const t = landing[lang];
  const url = abs(HOME_PATH[lang]);
  const orgId = abs('') + '#org';
  const faq = faqNode([1, 2, 3, 4].map((n) => ({ q: t[`q${n}` as 'q1'], a: plain(t[`a${n}` as 'a1']) })));
  const imgs = heroSlides.map((s, i) => ({
    '@type': 'ImageObject', '@id': `${url}#img-${i}`, contentUrl: abs(`assets/hero/${s.file}.jpg`), url: abs(`assets/hero/${s.file}.jpg`),
    width: 800, height: 1000, caption: t[s.alt], description: t[s.alt], inLanguage: lang, creditText: m.credit, copyrightNotice: '© LetsGoForACamp',
    creator: { '@id': orgId }, representativeOfPage: i === 0,
  }));
  const page = {
    '@type': 'WebPage', '@id': url + '#webpage', url, name: m.title, description: m.description, inLanguage: lang,
    isPartOf: { '@id': lang === 'en' ? abs('') : url + '#website' }, about: { '@id': orgId },
    primaryImageOfPage: { '@id': url + '#img-0' }, breadcrumb: { '@id': url + '#crumbs' }, availableLanguage: ['en', 'de', 'fr', 'es'],
  };
  const crumbs = { ...breadcrumb([[m.crumb, HOME_PATH[lang]]]), '@id': url + '#crumbs' };
  if (lang === 'en') return [[orgNode(), websiteNode(), faq], [page, crumbs, ...imgs]];
  const org = orgNode(m.orgDescription, { inLanguage: lang });
  delete (org as any).slogan; org.knowsAbout = ['Theyyam', 'North Malabar', 'Kannur', 'Kasaragod'];
  const site = { '@type': 'WebSite', '@id': url + '#website', name: 'LGFC Theyyam', url, inLanguage: lang, publisher: { '@id': orgId } };
  return [[org, site, page, crumbs, ...imgs, { ...faq, '@id': url + '#faq', inLanguage: lang }]];
}
