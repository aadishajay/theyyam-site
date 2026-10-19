import { abs } from './site';
import contact from '../data/contact.json';

// offices with a real address (not a [PLACEHOLDER]) go into the structured data
const locations = contact.offices
  .filter((o) => !o.address.includes('['))
  .map((o) => ({ '@type': 'Place', name: o.label, address: { '@type': 'PostalAddress', streetAddress: o.address, addressLocality: o.locality, addressRegion: o.region, addressCountry: o.country } }));

export const orgNode = (description?: string, extra: Record<string, unknown> = {}) => ({
  '@type': ['TravelAgency', 'Organization'],
  '@id': abs('') + '#org',
  name: 'TheyyamTrips',
  legalName: 'LetsGoForACamp Travel and Innovation LLP',
  alternateName: 'letsgoforacamp',
  logo: abs('assets/logo-theyyamtrips.svg'),
  url: abs(''),
  description:
    description ??
    'Guided Theyyam tours and cultural journeys in North Malabar, Kerala: small-group and private trips in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba and Kanhangad.',
  areaServed: [{ '@type': 'AdministrativeArea', name: 'North Malabar, Kerala, India' }],
  knowsAbout: ['Theyyam', 'North Malabar', 'Kannur', 'Kasaragod', 'Kerala ritual tradition'],
  slogan: 'A living ritual, shared with respect.',
  image: abs('assets/lgfc-og.jpg'),
  ...(locations.length ? { location: locations } : {}),
  ...extra,
});

export const websiteNode = () => ({
  '@type': 'WebSite',
  name: 'TheyyamTrips',
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
