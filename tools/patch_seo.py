#!/usr/bin/env python3
"""SEO + meta layer for the four landing pages (index.html, de/, fr/, es/). Idempotent; run LAST:
   python3 tools/patch_home.py && python3 tools/build_langs.py && python3 tools/patch_seo.py
Adds: canonical, og:url/locale/image(+size, alt), Twitter card, a JSON-LD block (WebPage, BreadcrumbList,
ImageObject for each carousel photo, and for the translated pages Organization, WebSite and FAQPage),
and rebuilds the sitemap entries for the home pages with hreflang alternates and image entries."""
import re, json, html, os

B = 'https://aadishajay.github.io/theyyam-site/'
LANGS = {'en': ('index.html', '', 'en_GB', 'en'), 'de': ('de/index.html', 'de/', 'de_DE', 'de'),
         'fr': ('fr/index.html', 'fr/', 'fr_FR', 'fr'), 'es': ('es/index.html', 'es/', 'es_ES', 'es')}
OG = B + 'assets/lgfc-og.jpg'
OG_ALT = {'en': 'A Theyyam in a large red and silver headdress at a shrine in Kannur, Kerala',
          'de': 'Ein Theyyam in großem rotem und silbernem Kopfschmuck an einem Schrein in Kannur, Kerala',
          'fr': 'Un Theyyam coiffé d’un grand ornement rouge et argent dans un sanctuaire de Kannur, Kerala',
          'es': 'Un Theyyam con un gran tocado rojo y plateado en un santuario de Kannur, Kerala'}
CRUMB = {'en': 'Home', 'de': 'Startseite', 'fr': 'Accueil', 'es': 'Inicio'}
CREDIT = {'en': 'Photograph: LetsGoForACamp', 'de': 'Foto: LetsGoForACamp', 'fr': 'Photo : LetsGoForACamp', 'es': 'Foto: LetsGoForACamp'}
ORG_DESC = {
 'en': 'Guided Theyyam tours and cultural journeys in North Malabar, Kerala: small-group and private trips in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba and Kanhangad.',
 'de': 'Geführte Theyyam-Reisen und Kulturreisen in Nord-Malabar, Kerala: Kleingruppen- und Privatreisen in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba und Kanhangad.',
 'fr': 'Voyages Theyyam accompagnés et voyages culturels dans le Malabar du Nord, Kerala : petits groupes et voyages privés à Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba et Kanhangad.',
 'es': 'Viajes culturales para descubrir el Theyyam en el Malabar del Norte, Kerala: grupos reducidos y viajes privados en Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba y Kanhangad.'}
E = html.escape

def hero_images(s, prefix):
    out = []
    for m in re.finditer(r'<img src="(?:\.\./)?assets/hero/([a-z0-9-]+\.jpg)" alt="([^"]*)" width="(\d+)" height="(\d+)"', s):
        out.append((m.group(1), html.unescape(m.group(2)), int(m.group(3)), int(m.group(4))))
    return out

def faq(s):
    q = []
    for m in re.finditer(r'<details[^>]*><summary><h3>(.*?)</h3></summary><p[^>]*>(.*?)</p></details>', s, re.S):
        q.append((html.unescape(re.sub('<[^>]+>', '', m.group(1))), html.unescape(re.sub('<[^>]+>', '', m.group(2))).strip()))
    return q

def build(code):
    path, folder, loc, lang = LANGS[code]
    s = open(path, encoding='utf-8').read()
    url = B + folder
    title = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    imgs = hero_images(s, folder)
    # strip anything this script (or earlier steps) already wrote
    s = re.sub(r'<!--seo:start-->.*?<!--seo:end-->', '', s, flags=re.S)
    s = re.sub(r'<link rel="canonical"[^>]*>', '', s)
    for p in ('og:url', 'og:image', 'og:type', 'og:site_name', 'og:locale', 'og:locale:alternate', 'og:image:width', 'og:image:height', 'og:image:alt'):
        s = re.sub(r'<meta property="%s"[^>]*>' % re.escape(p), '', s)
    s = re.sub(r'<meta name="twitter:[^"]*"[^>]*>', '', s)
    meta = (f'<link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="LGFC Theyyam">'
            f'<meta property="og:url" content="{url}"><meta property="og:locale" content="{loc}">'
            + ''.join(f'<meta property="og:locale:alternate" content="{v[2]}">' for k, v in LANGS.items() if k != code)
            + f'<meta property="og:image" content="{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:image:alt" content="{E(OG_ALT[code])}">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}">'
            f'<meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{OG}">'
            f'<meta name="twitter:image:alt" content="{E(OG_ALT[code])}">')
    # JSON-LD
    org_id = B + '#org'
    graph = []
    if code != 'en':
        graph.append({'@type': ['TravelAgency', 'Organization'], '@id': org_id, 'name': 'LGFC Theyyam',
                      'legalName': 'LetsGoForACamp Travel and Innovation LLP', 'alternateName': 'letsgoforacamp', 'url': B,
                      'description': ORG_DESC[code], 'inLanguage': lang,
                      'areaServed': [{'@type': 'AdministrativeArea', 'name': 'North Malabar, Kerala, India'}],
                      'knowsAbout': ['Theyyam', 'North Malabar', 'Kannur', 'Kasaragod']})
        graph.append({'@type': 'WebSite', '@id': url + '#website', 'name': 'LGFC Theyyam', 'url': url, 'inLanguage': lang, 'publisher': {'@id': org_id}})
    page_id = url + '#webpage'
    graph.append({'@type': 'WebPage', '@id': page_id, 'url': url, 'name': title, 'description': desc, 'inLanguage': lang,
                  'isPartOf': {'@id': (url + '#website') if code != 'en' else B}, 'about': {'@id': org_id},
                  'primaryImageOfPage': {'@id': url + '#img-0'} if imgs else None,
                  'breadcrumb': {'@id': url + '#crumbs'},
                  'availableLanguage': [v[3] for v in LANGS.values()]})
    graph[-1] = {k: v for k, v in graph[-1].items() if v is not None}
    graph.append({'@type': 'BreadcrumbList', '@id': url + '#crumbs',
                  'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': CRUMB[code], 'item': url}]})
    for i, (f, alt, w, h) in enumerate(imgs):
        graph.append({'@type': 'ImageObject', '@id': f'{url}#img-{i}', 'contentUrl': f'{B}assets/hero/{f}', 'url': f'{B}assets/hero/{f}',
                      'width': w, 'height': h, 'caption': alt, 'description': alt, 'inLanguage': lang,
                      'creditText': CREDIT[code], 'copyrightNotice': '© LetsGoForACamp',
                      'creator': {'@id': org_id}, 'representativeOfPage': i == 0})
    if code != 'en':
        qs = faq(s)
        if qs:
            graph.append({'@type': 'FAQPage', '@id': url + '#faq', 'inLanguage': lang, 'mainEntity': [
                {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qs]})
    ld = '<script type="application/ld+json" id="seo-ld">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False) + '</script>'
    s = s.replace('</head>', f'<!--seo:start-->{meta}{ld}<!--seo:end--></head>', 1)
    open(path, 'w', encoding='utf-8').write(s)
    return imgs, len(desc), len(title)

info = {c: build(c) for c in LANGS}

# ---- sitemap: home pages with hreflang alternates and image entries
sm = open('sitemap.xml', encoding='utf-8').read()
sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">')
sm = re.sub(r'<!--home:start-->.*?<!--home:end-->\n?', '', sm, flags=re.S)
sm = re.sub(r'<url><loc>%s(?:de/|fr/|es/)?</loc>.*?</url>\n?' % re.escape(B), '', sm, flags=re.S)
alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{B}{v[1]}"/>' for c, v in LANGS.items()) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{B}"/>'
block = '<!--home:start-->\n'
for c, v in LANGS.items():
    imgs = info[c][0]
    block += f'<url><loc>{B}{v[1]}</loc>{alts}' + ''.join(
        f'<image:image><image:loc>{B}assets/hero/{f}</image:loc><image:caption>{E(alt)}</image:caption></image:image>' for f, alt, w, h in imgs) + '</url>\n'
block += '<!--home:end-->\n'
sm = sm.replace('<url>', block + '<url>', 1)
open('sitemap.xml', 'w', encoding='utf-8').write(sm)
for c, (imgs, dl, tl) in info.items():
    print(c, 'images', len(imgs), 'desc', dl, 'title', tl)
