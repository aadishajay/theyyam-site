# LGFC Theyyam website

Culture-led, inquiry-only site for LGFC's guided Theyyam trips (Kannur and Kasaragod, Kerala). Built with
[Astro](https://astro.build) as a static site; review copy on GitHub Pages: https://aadishajay.github.io/theyyam-site/

Principles that apply to every page (see also the project `CLAUDE.md`):
- Theyyam is a ritual, not a performance. Never write dance, performance, performer, audience, show, costume (use ritual, koladhari, attire, those present).
- No event dates, venues or schedules. Only the season window (late Oct to May), base towns and trip types.
- Inquiry only: no checkout, no public prices ("On request").

## Run it
```bash
npm install
npm run dev          # http://localhost:4321/theyyam-site/
npm run build        # static output in dist/
```
Build settings come from environment variables (see `astro.config.mjs`, `src/lib/site.ts`):

| Variable | Default | Launch |
|---|---|---|
| `SITE` | `https://aadishajay.github.io` | `https://your-domain.com` |
| `BASE` | `/theyyam-site` | `/` |
| `INDEXABLE` | unset (pages are `noindex`) | `1` |

Launch build: `SITE=https://your-domain.com BASE=/ INDEXABLE=1 npm run build`.

## Where things live
```
src/
  content/journal/*.md      blog posts  (Markdown + front matter)
  content/theyyams/*.md     one file per Theyyam (Markdown + front matter)
  data/                     trips, journal index cards, categories, glossary, hero photos, Theyyam name list
  i18n/                     UI strings, landing page copy (en, de, fr, es), landing <head> copy
  components/               Header, Footer, TrustStrip, TwoWays, CtaBand, HeroCarousel, Landing, TheyyamCard ...
  layouts/Base.astro        <head> (SEO, Open Graph, JSON-LD), skip link, search script
  lib/                      URL helpers (site.ts), JSON-LD builders (schema.ts, landing-seo.ts), linkify, markdown
  pages/                    routes: home + de/fr/es, trips, enquire, journal, glossary, theyyams/, sitemap, robots, search index
  plugins/remark-blocks.mjs custom Markdown blocks (below)
  styles/                   base.css + one stylesheet per template
public/assets/              images (hero/, theyyam/), search.js
docs/BACKLOG.md             content still to add, review notes
```

## Write a blog post
Add `src/content/journal/<slug>.md` (the slug becomes `/<slug>.html`). Front matter: `title`, `h1`, `crumb`,
`description`, `category`, `readTime`, `author` (rotate between Sankeerth, Geethu, Abhina and Aadi), `date` (YYYY-MM-DD, shown as "Updated"; not put in the structured data), `hero` (image under `public/assets/`), `lead`, `ld` (structured-data
headline/description/about/image), `related` (3 cards), `faq` (question/answer list), and `toc: true` for an
"In this guide" list. Then add a card in `src/data/journal.ts`. Body is Markdown with these blocks:

```
## A heading
Normal paragraphs, **bold**, *italic*, [links](theyyam-etiquette.html).

:::quote
A pull quote.
:::
::figure{src="lgfc-headdress-shrine.jpg" alt="..." width=1000 height=563}
:::caption
Small caption.
:::
::cta{title="..." text="..." label="Enquire about a trip" spaced}
::faq
:::aside
A small note.
:::
:::sources
**Sources and further reading:** ...
:::
```

## Add a Theyyam
Add `src/content/theyyams/<slug>.md`. Front matter: `kind: theyyam`, `slug`, `order`, `name`, `ml` (Malayalam),
`category` (gods, goddesses, heroes, harmony), `tagline`, `alias`, `tags` (search keywords), `koladhari`,
`facts` (label/value list), `sources`, and `photos`. Each photo: `file` (in `public/assets/theyyam/`), `w`, `h`, `alt`, optional `caption`, `artist`, `lic`, and `page` (the source page the credit links to). The first photo is the hero; every other photo is shown by `::gallery`, so adding a photo is one more entry in `photos`.
Body sections, in order: `## Who is <name>?`, `## The story`, `::gallery`, `## What you will see`, `::gloss`,
`## In the tradition`, `:::note ... :::`. Add the name (and any spellings) to `src/data/theyyam-terms.json` so other
pages link to it automatically (the first mention of each other Theyyam is linked).

## Testimonials
`src/content/testimonials.md` is the single source. Published items (`published: true`, `theyyam: true`) rotate in a carousel
on every landing page, each with the cover photo of its trip (`trips:` map; images in `public/assets/testimonials/`).
The same items, after the first, appear in "What guests say" on the trips page. While none is published, the translated
placeholder shows. Quotes are anonymised: label them "Theyyam Trip <place>" and refer to staff as "the guide".

## Translations
Landing page copy for every language is in `src/i18n/landing.ts` (same keys per language). Only the landing page is
translated; the other pages are English with a note pointing to browser translation.

## Deploy
Build locally and push only the static output to the `gh-pages` branch (GitHub Pages serves that branch; source stays on `main`):
```bash
npm run deploy
```
For launch: `SITE=https://your-domain.com BASE=/ INDEXABLE=1 npm run deploy`.

## Before launch
`npm run check:placeholders` lists every `[PLACEHOLDER]` still on the site. A launch deploy (`INDEXABLE=1 npm run deploy`) stops until none are left.

Fill the placeholders (`[PHONE]`, `[EMAIL]`, `[INSTAGRAM]`, `[ADDRESS]`, registration no., rating, association,
testimonial, author and date), set `ENDPOINT` in `src/pages/enquire.astro`, pick a domain, and build with the launch
variables above. Have a knowledgeable person review the Theyyam content and the German, French and Spanish copy.

## Enquiry form

`src/pages/enquire.astro` posts with fetch (no-cors; the browser follows the worker's redirect but the response stays opaque) to the unchanged Cloudflare Worker `https://lgfc_custom_trip_form_handler.letsgoforacamp.workers.dev/submit`, which writes to Notion and emails the guest, then opens `enquiry-success.html?enquiryId=…`. The ID is computed like the worker does (first 4 letters of name / first 4 of the destination sent to the worker ("Theyyam- <town>") / arrival date, upper case). Bot check is a small on-page sum (a + b, checked in the browser) plus a hidden honeypot. No captcha widget is shown: the worker only checks that `g-recaptcha-response` is present, so the form sends a fixed placeholder (`not-used`). This only stops simple bots (a bot that reads the page can solve it); if spam appears, add real verification in the worker. Never commit the worker's secrets to this repo.
