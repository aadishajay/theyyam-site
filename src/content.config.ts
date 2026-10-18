import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const journal = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/journal' }),
  schema: z.object({
    title: z.string(), // <title> / share title
    h1: z.string(),
    crumb: z.string(), // short name for breadcrumbs
    description: z.string(),
    category: z.string(),
    readTime: z.string(),
    toc: z.boolean().default(false), // show the "In this guide" list
    hero: z.object({ src: z.string(), alt: z.string(), width: z.number(), height: z.number() }),
    lead: z.string(),
    ld: z.object({ headline: z.string(), description: z.string(), about: z.string(), image: z.string() }),
    related: z.array(z.object({ slug: z.string(), img: z.string(), alt: z.string(), k: z.string(), title: z.string() })),
    faq: z.array(z.object({ q: z.string(), a: z.string() })),
  }),
});

const theyyams = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/theyyams' }),
  schema: z.object({
    kind: z.literal('theyyam'),
    slug: z.string(),
    order: z.number(), // position in the master list (drives "More Theyyams")
    name: z.string(),
    ml: z.string(), // Malayalam name
    category: z.enum(['gods', 'goddesses', 'heroes', 'harmony']),
    tagline: z.string(),
    alias: z.array(z.string()),
    tags: z.array(z.string()), // search keywords
    koladhari: z.boolean().default(false),
    facts: z.array(z.object({ label: z.string(), value: z.string() })),
    sources: z.array(z.object({ name: z.string(), url: z.string() })),
    photos: z.array(z.object({ file: z.string(), w: z.number(), h: z.number(), artist: z.string(), lic: z.string() })).default([]),
  }),
});

export const collections = { journal, theyyams };
