# Theyyams still to add

Names only. Do not add dates or venues (see CLAUDE.md). Check against sources in `theyyams_data.py` style before adding.

## Named in our sheet, not yet on the site
Azhikkode Gurunathan, Ellethu Bhagavathi, Ganapathi, Kakkara Bhagavathi, Karinkutty Chathan, Karuvalamma, Kulangara Bhagavathi, Muthabhagavathi, Paradevata (a generic term), Shasthavu, Vellar, Vellatta Bhootham, Uchakutty Chathan. Variants already covered under another page via aliases: Raktha, Patten and Moovalamkuzhi Chamundi (Chamundi), Karingulikan (Gulikan). "Vellattu" is a ritual stage, not a deity.

## Named by Kerala Tourism (keralatourism.org/bekal/theyyam-various-types.php), not yet on the site
With a short description there: Padikutti Amma, Muthappan Anthithira, Agni Kandakarnan, Padamadakki Bhagavathy, Manakkott Amma.
Names only: Padarkulangara Bhagavathy, Karinthiri Nair, Kuttikol Thamburatti, Chuzhali Bhagavathy, Kannangat Bhagavathy, Kodoth Chamundi, Palot Daivam, Dandinganath Bhagavathy, Narambil Bhagavathy, Vettakorumakan, Mavila Chamundi, Urpazhassi, Kudiveeran, Veerabadran, Kunhiraman Gurukkal, Munnayareeshwaran, Manavalan, Manjalamma, Thoovakkari Muthappan, Madayil Chamundi, Pethalan, Pullon, Pallivettakkorumakan and others.

## Sources to check next
K.K.N. Kurup, The Cult of Teyyam and Hero Worship in Kerala (1973); Kurup, Teyyam of Kerala (Sangeet Natak Akademi, 1979); Kerala Folklore Academy publications; Kerala Tourism brochures.

## Added later / still open
- Mentioned on the site but no page yet: Koyi Mammad, Naithiyar, Beevi (Mappila Theyyams named in Wikipedia; too little found). Poomala Bhagavathi has no Theyyam form per Wikipedia.
- "Kudidaivam": no source found. Closest is Kudiveeran (listed by Kerala Tourism; only an NFT listing describes it). Need the user's source or spelling.
- Kallurti (Bhuta Kola, Tulu Nadu) deliberately left out for now.
- Pages with no photo yet: Angakkaran, Bappuran, Police Theyyam, Rakta Chamundi, Veerakali, Cheerumba Bhagavathi, Aali Theyyam, Kalanthan Mukri, Yogyar Akampadi, Pulimaruthan, Marapuli.

## Languages
- de/, fr/, es/ landing pages are built by src/i18n/landing.ts (re-run after any change to index.html). Other pages stay English; footer note points to browser translate.
- Needs native-speaker review before launch (ritual wording: no dance/show/performance).
- Add the three pages to sitemap.xml and drop noindex at launch.

## Photos
- Placeholder Wikimedia photos on landing/trips/journal pages were replaced with LGFC trip photos (assets/lgfc-*.jpg), taken from the Theyyam trip Google Photos albums linked in the Notion "Trip Calendar" database (Feb 2026, Mar 2025 and Feb 2025 albums). Ritual photos only; guest faces and fire-led shots avoided. Still to check: consent for any devotees visible in frame, and per-shrine photo rules.
- Unused strong candidates: orig a1_09/a1_17 (tall striped cone headdress), a4_226, a2_161.

## Hero carousel
- Homepage carousel: eight LGFC trip photos (assets/hero/, 800x1000, 4:5) cropped from the Theyyam trip Google Photos albums linked in Notion (Feb 2026, Mar 2025, Feb 2025). Two are the Kandanar Kelan fire frames (assumed from the trip notes: Kadanarkelan appears at night on those trips) - confirm the identification. Culture shots come first; fire frames never lead. No caption or links. Slide list and alt text: src/data/hero.ts (then run build_langs.py).
- Earlier SVG / traced / hand-drawn face experiments were dropped.
- Check consent for devotees visible in frame, and shrine photo rules, before launch.
