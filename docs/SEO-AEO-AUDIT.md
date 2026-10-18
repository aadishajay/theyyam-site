# SEO and AEO audit (build of 2026-10-19, 65 pages)

Method: scripted checks on the built site (titles, descriptions, headings, canonical and hreflang, structured data,
links, images, content depth) plus a status check of every external link. Scores are my judgement, not tool output.
Not measured: real search rankings, Core Web Vitals (no Lighthouse run), crawl behaviour.

## Summary
| Area | Score | Headline |
|---|---|---|
| Technical SEO | 7 / 10 | solid base; title length, favicon, 404 and speed hints are the gaps |
| On-page SEO | 7 / 10 | clear titles and one H1 per page; several blog posts are thin |
| Structured data | 8 / 10 | Organization, WebSite, Article, FAQ, Breadcrumb, TouristTrip, DefinedTerm; no author pages |
| AEO (answer engines) | 7 / 10 | FAQ on every page and answer-first openings; no author entities, no llms.txt |
| Launch readiness | 3 / 10 | every page is noindex; placeholders still on the site |

## What passes
- 65 pages: every page has a canonical, `lang`, viewport, exactly one H1, no skipped heading levels, no duplicate titles or descriptions.
- hreflang on the four landing pages is reciprocal, with x-default.
- JSON-LD parses on every page. Coverage: Organization, WebSite and Breadcrumb on all 65; FAQPage on 60; Article on 56; TouristTrip list; DefinedTermSet for the glossary.
- All images have alt text. All 135 external links return 200. All 2,241 internal links and assets resolve.
- Sitemap lists all 65 pages, with hreflang alternates and the carousel images on the landing pages.
- Open Graph and Twitter cards present, with image size and alt text.

## Problems, in priority order
1. **Titles too long: 57 of 65 are over 60 characters** (longest 77, for the cameras post). Google truncates around 60. Shorten the pattern "<Name> Theyyam: Story, Meaning & What to Expect | LGFC Theyyam" and the blog titles.
2. **Trips description is 182 characters** (limit about 160).
3. **No favicon.** Browsers request one and get a 404; it also shows in search results.
4. **No custom 404 page.** GitHub Pages serves a generic one.
5. **Loading hints missing:** the first carousel image has no `fetchpriority="high"`; the font preconnect lacks the `crossorigin` host (`fonts.gstatic.com`). Largest images are about 480 KB (Theyyam pages), all JPEG; WebP or AVIF would cut weight.
6. **Thin pages.** Blog posts run 316 to 450 words (the two new ones, 815 and 915, are fine). Eight Theyyam pages are under 450 words: Bappuran, Cheerumba Bhagavathi, Marapuli, Pulikandan, Pulikarinkali, Pulimaruthan and two others.
7. **Weak internal links.** Five pages have fewer than two links pointing to them: the Kantara post, Bhairavan, Police Theyyam, Poomaruthan and one more. Link the Kantara post from the Panjuruli, Gulikan and what-is posts.
8. **Every page is noindex** (intended until launch), and the sitemap lists them anyway.
9. **Placeholders:** `[PHONE]`, `[EMAIL]`, `[INSTAGRAM]`, addresses, registration number, association and privacy policy. No search engine rewards them, and no real contact path hurts trust.
10. **Sitemap has no lastmod.**

## AEO (answer engines and AI search)
Good: FAQ questions with short answers on 60 pages; blog openings of 26 to 64 words that state the answer; question-style headings in every post; a glossary with defined terms; sources listed on posts and Theyyam pages; Theyyam pages open with a one-line definition.

To add:
1. **Author pages and Person entities** for Sankeerth, Geethu, Abhina and Aadi (short bio, role, link to their posts). Answer engines weigh who wrote it.
2. **`llms.txt`** with a short site summary and the key pages (an emerging convention, low cost).
3. **Answer-first openings on all posts**: the first 40 to 60 words should answer the headline question; four posts open longer.
4. **Question headings on Theyyam pages** ("Who is X?" exists; add "What does X look like?" and "Where is X worshipped?" as headings with one-paragraph answers).
5. **Entity links:** add Wikipedia and Wikidata `sameAs` for each Theyyam in its Article data; add the Instagram and any Kannur Business Profile to Organization `sameAs` once they exist.
6. **A "Facts at a glance" block** on the trips page (length, season, base towns, group size) in plain lists and a table, which answer engines quote easily.
7. **Real reviews** (the testimonials, plus Google reviews of a Kannur profile once it exists) with Review markup only if the guidelines allow.
8. **Freshness:** the visible "Updated" dates are not in the structured data by choice; keep a real update habit and a real `lastmod` in the sitemap.

## Next actions (suggested order)
1. Shorten titles and the trips description.
2. Add favicon, 404 page, `fetchpriority`, font `crossorigin`; convert images to WebP.
3. Add `llms.txt`, author pages, sitemap `lastmod`.
4. Expand the thin Theyyam and blog pages; add the internal links.
5. Write the two planned articles (Kannur and North Malabar guide; how to find Theyyam dates respectfully).
6. Fill the placeholders and launch with `INDEXABLE=1`; submit the sitemap in Search Console.
