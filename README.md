# LGFC Theyyam website (review build)

Plain HTML, Design A "Vermilion". `build.py` regenerated these pages from the design canvas; edit the HTML directly from now on.
Placeholder photos are from Wikimedia Commons (credits in each footer). Pages are `noindex` until launch.

## Landing page build order
`python3 tools/patch_home.py && python3 tools/build_langs.py && python3 tools/patch_seo.py`
(patch_seo.py adds canonical, Open Graph, Twitter, JSON-LD and the home entries of sitemap.xml for the four landing pages; run it last.)
