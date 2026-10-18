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
    // The first photo is the hero; every other photo is shown in the gallery (::gallery in the body).
    photos: z.array(z.object({
      file: z.string(), // under public/assets/theyyam/
      w: z.number(), h: z.number(),
      alt: z.string().optional(), // description for screen readers and search
      caption: z.string().optional(), // shown above the credit in the gallery
      artist: z.string(), lic: z.string(),
      page: z.string().url().optional(), // source page (Wikimedia Commons) the credit links to
    })).default([]),
  }),
});

const testimonials = defineCollection({
  loader: glob({ pattern: 'testimonials.md', base: './src/content' }),
  schema: z.object({
    items: z.array(z.object({
      id: z.string(),
      quote: z.string(),
      name: z.string(),
      country: z.string(),
      trip: z.string(),
      source: z.enum(['google', 'email', 'whatsapp', 'other']),
      sourceUrl: z.string().url().optional(),
      date: z.string().optional(),
      published: z.boolean().default(false),
      theyyam: z.boolean().default(false), // about a Theyyam trip
    })),
  }),
});

export const collections = { journal, theyyams, testimonials };
