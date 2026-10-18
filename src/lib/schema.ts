import { abs } from './site';

export const orgNode = (description?: string, extra: Record<string, unknown> = {}) => ({
  '@type': ['TravelAgency', 'Organization'],
  '@id': abs('') + '#org',
  name: 'LGFC Theyyam',
  legalName: 'LetsGoForACamp Travel and Innovation LLP',
  alternateName: 'letsgoforacamp',
  url: abs(''),
  description:
    description ??
    'Guided Theyyam tours and cultural journeys in North Malabar, Kerala: small-group and private trips in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba and Kanhangad.',
  areaServed: [{ '@type': 'AdministrativeArea', name: 'North Malabar, Kerala, India' }],
  knowsAbout: ['Theyyam', 'North Malabar', 'Kannur', 'Kasaragod', 'Kerala ritual tradition'],
  slogan: 'A living ritual, shared with respect.',
  image: abs('assets/lgfc-og.jpg'),
  ...extra,
});

export const websiteNode = () => ({
  '@type': 'WebSite',
  name: 'LGFC Theyyam',
  url: abs(''),
  publisher: { '@id': abs('') + '#org' },
});

export const breadcrumb = (items: [string, string][]) => ({
  '@type': 'BreadcrumbList',
  itemListElement: items.map(([name, path], i) => ({ '@type': 'ListItem', position: i + 1, name, item: abs(path) })),
});

export const faqNode = (qa: { q: string; a: string }[]) => ({
  '@type': 'FAQPage',
  mainEntity: qa.map(({ q, a }) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })),
});
