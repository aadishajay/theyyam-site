#!/usr/bin/env python3
"""Build German, French and Spanish landing pages (de/, fr/, es/) from index.html.
Run from the website folder. Only the landing page is translated; other links point to the English pages.
Also adds a language switcher and hreflang links to index.html (idempotent)."""
import re, os

SRC = open('index.html', encoding='utf-8').read()
# strip any previous switcher/hreflang from the English page before using it as a template
SW_RE = re.compile(r'<!--lang:start-->.*?<!--lang:end-->', re.S)
HL_RE = re.compile(r'<!--hl:start-->.*?<!--hl:end-->', re.S)
BASE = HL_RE.sub('', SW_RE.sub('', SRC))

LANGS = ['en', 'de', 'fr', 'es']
SITE = 'https://aadishajay.github.io/theyyam-site/'
def hreflang():
    out = '<!--hl:start-->'
    for l in LANGS:
        out += f'<link rel="alternate" hreflang="{l}" href="{SITE}{"" if l=="en" else l+"/"}">'
    out += f'<link rel="alternate" hreflang="x-default" href="{SITE}"><!--hl:end-->'
    return out
def switcher(cur, prefix):
    # prefix is '' on the English page and '../' on a language page
    names = {'en': 'EN', 'de': 'DE', 'fr': 'FR', 'es': 'ES'}
    full = {'en': 'English', 'de': 'Deutsch', 'fr': 'Fran\u00e7ais', 'es': 'Espa\u00f1ol'}
    a = ''
    for l in LANGS:
        href = prefix + ('index.html' if l == 'en' else l + '/')
        if l == cur: a += f'<span aria-current="true" style="font-weight:800">{names[l]}</span>'
        else: a += f'<a href="{href}" hreflang="{l}" lang="{l}" title="{full[l]}" style="color:#1a0a08;text-decoration:none">{names[l]}</a>'
    return ('<!--lang:start--><div class="lang" role="navigation" aria-label="Language" style="display:flex;gap:10px;font-size:13px;'
            'font-weight:600;margin:0 24px 0 auto">' + a + '</div><!--lang:end-->')

T = {}
T['de'] = {
 'lang': 'de', 'title': 'LGFC Theyyam | Geführte Theyyam-Reisen in Nord-Kerala',
 'desc': 'Erleben Sie Keralas ältestes lebendiges Ritual auf Kleingruppen- oder Individualreisen in Kannur und Kasaragod. Unterkunft und Transfers, auf Wunsch mit lokalem Guide. Jetzt anfragen.',
 'switchnote': 'Weitere Seiten sind derzeit auf Englisch. Nutzen Sie die Übersetzungsfunktion Ihres Browsers.',
 'pairs': [
 ('Skip to content','Zum Inhalt springen'),
 ('Guided trips','Geführte Reisen'),('>Journal<','>Journal<'),('>Menu<','>Menü<'),
 ('>Enquire<','>Anfragen<'),('See trips','Reisen ansehen'),
 ('Guided Theyyam tours · North Malabar, Kerala','Geführte Theyyam-Reisen · Nord-Malabar, Kerala'),
 ('A living ritual,','Ein lebendiges Ritual,'),('shared with respect','mit Respekt geteilt'),
 ('Small-group journeys to Kerala’s oldest living ritual, planned around you, with a local guide if you want one to open doors, explain every step and keep you welcome.','Kleingruppenreisen zu Keralas ältestem lebendigen Ritual, ganz nach Ihren Wünschen geplant. Auf Wunsch mit lokalem Guide, der Türen öffnet, jeden Schritt erklärt und dafür sorgt, dass Sie willkommen sind.'),
 ('Enquire about a trip','Reise anfragen'),('See guided trips','Geführte Reisen ansehen'),
 ('Season: Oct to May','Saison: Okt bis Mai'),('Group or private','Gruppe oder privat'),('Stay + transfers','Unterkunft + Transfers'),
 ('Rooted in North Malabar','Verwurzelt in Nord-Malabar'),
 ('Heritage · Family · Faith · Craft · Music · Story','Erbe · Familie · Glaube · Handwerk · Musik · Geschichte'),
 ('years organising Theyyam tours','Jahre Erfahrung mit Theyyam-Reisen'),
 ('explorers hosted on Theyyam trips','Reisende auf Theyyam-Reisen betreut'),
 ('support for booked trips','Betreuung auf gebuchten Reisen'),
 ('Made with warmth in North Malabar, Kerala · Powered by letsgoforacamp','Mit Herz gemacht in Nord-Malabar, Kerala · Powered by letsgoforacamp'),
 ('Run by natives of North Malabar. Hosted like family.','Geführt von Einheimischen aus Nord-Malabar. Gastfreundschaft wie in der Familie.'),
 ('We are a team of natives from Kannur and across North Malabar. After eight years of working with the families and villages of this region, we know who to ask, when to step back, and how to make a guest feel welcome.','Wir sind ein Team von Einheimischen aus Kannur und ganz Nord-Malabar. Nach acht Jahren Zusammenarbeit mit den Familien und Dörfern dieser Region wissen wir, wen man fragt, wann man zurücktritt und wie sich Gäste willkommen fühlen.'),
 ('Local, not outsourced','Lokal, nicht ausgelagert'),
 ('Our team, and any guide or driver we arrange, are natives of North Malabar. Nobody reads you a script.','Unser Team und jeder Guide oder Fahrer, den wir vermitteln, stammen aus Nord-Malabar. Niemand liest Ihnen einen Text vor.'),
 ('Known to the families','Den Familien bekannt'),
 ('Introductions come from people the families already trust, so you are welcomed, not merely allowed in.','Vorstellungen laufen über Menschen, denen die Familien vertrauen. So sind Sie willkommen und nicht nur geduldet.'),
 ('A real person replies','Ein echter Mensch antwortet'),
 ('No checkout and no call centre. Our North Malabar team answers within two working days, and is on call 24x7 once you are booked.','Kein Online-Checkout und kein Callcenter. Unser Team in Nord-Malabar antwortet innerhalb von zwei Werktagen und ist nach der Buchung rund um die Uhr erreichbar.'),
 ('We protect the ritual','Wir schützen das Ritual'),
 ('We never publish ritual dates or places, we brief every guest on etiquette, and we follow each shrine’s rules on photography.','Wir veröffentlichen nie Termine oder Orte von Ritualen, weisen jeden Gast in die Etikette ein und befolgen die Fotoregeln jedes Schreins.'),
 ('Two ways to travel','Zwei Arten zu reisen'),('Join a group or make it yours','Gruppe anschließen oder ganz individuell'),
 ('Small group departures','Kleingruppen-Termine'),
 ('Share the journey with up to 8 like-minded travellers. Departure windows are shared when you enquire.','Teilen Sie die Reise mit bis zu 8 Gleichgesinnten. Reisezeiträume nennen wir Ihnen auf Anfrage.'),
 ('Enquire about a group trip','Gruppenreise anfragen'),
 ('Private and customised','Privat und individuell'),
 ('Your own dates, pace and interests, for family, friends, a special-interest group or a solo explorer. We design it with you.','Eigene Termine, eigenes Tempo, eigene Interessen, für Familie, Freunde, eine Interessengruppe oder Einzelreisende. Wir planen gemeinsam mit Ihnen.'),
 ('Enquire about a custom trip','Individuelle Reise anfragen'),
 ('Why go with us: the ritual is worship, and we help you be a good guest','Warum mit uns: Das Ritual ist Gottesdienst, und wir helfen Ihnen, ein guter Gast zu sein'),
 ('>Why go with us<','>Warum mit uns<'),
 ('Access, arranged','Zugang, vermittelt'),
 ('Rituals happen in family shrines and village grounds. We handle introductions and timing so you are welcome, not in the way.','Rituale finden in Familienschreinen und auf Dorfplätzen statt. Wir kümmern uns um Vorstellung und Zeitpunkt, damit Sie willkommen sind und nicht im Weg stehen.'),
 ('A local guide, if you want one','Ein lokaler Guide, wenn Sie möchten'),
 ('Optional. Know who the deity is, what the story means, and when to step forward or hold back.','Optional. Erfahren Sie, wer die Gottheit ist, was die Geschichte bedeutet und wann man nähertritt oder sich zurückhält.'),
 ('Everything handled','Alles organisiert'),
 ('Night rituals and rural roads are hard alone. We run stays, transfers, meals and the late drive home.','Nächtliche Rituale und Landstraßen sind allein schwierig. Wir kümmern uns um Unterkunft, Transfers, Mahlzeiten und die späte Heimfahrt.'),
 ('New here?','Neu hier?'),('What is Theyyam?','Was ist Theyyam?'),
 ('A living ritual of north Kerala where the person who takes the kolam, after hours of painting and dressing, is believed to become the deity. Hundreds of forms exist, each with its own attire, song and story, kept by the same families for generations.','Ein lebendiges Ritual in Nord-Kerala, bei dem der Mensch, der das Kolam annimmt, nach Stunden des Bemalens und Ankleidens als Gottheit gilt. Es gibt Hunderte von Formen, jede mit eigener Tracht, eigenem Gesang und eigener Geschichte, seit Generationen von denselben Familien bewahrt.'),
 ('Read the first-timer’s guide','Leitfaden für Erstbesucher lesen'),('Meet the Theyyams','Die Theyyams kennenlernen'),
 ('Guided Theyyam trips: choose how deep you want to go','Geführte Theyyam-Reisen: Sie bestimmen, wie tief Sie eintauchen'),
 ('Exact rituals are confirmed with you before you pay, because they depend on the day.','Die genauen Rituale bestätigen wir vor der Zahlung mit Ihnen, denn sie hängen vom jeweiligen Tag ab.'),
 ('3 nights · Beginners','3 Nächte · Einsteiger'),('The Heritage Journey','Die Heritage-Reise'),
 ('Your first Theyyam, with the story behind it.','Ihr erstes Theyyam, mit der Geschichte dahinter.'),
 ('5 nights · Enthusiasts','5 Nächte · Kenner'),('North Malabar Deep Dive','Nord-Malabar intensiv'),
 ('Two bases, more nights, time with the families.','Zwei Standorte, mehr Nächte, Zeit mit den Familien.'),
 ('4 nights · Craft lovers','4 Nächte · Handwerksfreunde'),('Craft &amp; Attire Journey','Handwerk- &amp; Trachtenreise'),
 ('Time with the maker of the attire, a musician and a weaver.','Zeit mit dem Hersteller der Tracht, einem Musiker und einer Weberin.'),
 ('Five base towns. One ritual coast.','Fünf Standorte. Eine Küste der Rituale.'),
 ('We stay in comfortable towns and travel out to the rituals each night, so you sleep well and see more.','Wir wohnen in komfortablen Städten und fahren abends zu den Ritualen, damit Sie gut schlafen und mehr erleben.'),
 ('· weavers, beaches, easy transfers','· Weber, Strände, einfache Transfers'),('· fort town, food and cricket','· Festungsstadt, Essen und Cricket'),
 ('· the heartland of the ritual','· das Kernland des Rituals'),('· the northern gateway','· das Tor zum Norden'),
 ('How it works','So funktioniert es'),
 ('Tell us your plan','Erzählen Sie uns Ihren Plan'),('Month, group size, interests. Two minutes.','Monat, Gruppengröße, Interessen. Zwei Minuten.'),
 ('We shape the trip','Wir gestalten die Reise'),('A proposal in two working days.','Ein Vorschlag in zwei Werktagen.'),
 ('We confirm rituals','Wir bestätigen die Rituale'),('Closer to travel, we lock the best nights.','Kurz vor der Reise legen wir die besten Nächte fest.'),
 ('You arrive, we host','Sie kommen an, wir kümmern uns'),('Stay and transfers are ready, and a guide if you chose one.','Unterkunft und Transfers stehen bereit, auf Wunsch auch ein Guide.'),
 ('“[TRAVELLER TESTIMONIAL: one sentence on what the guide made possible]”','“[REISEBERICHT: ein Satz darüber, was der Guide möglich gemacht hat]”'),
 ('[Name], [Country] · The Heritage Journey','[Name], [Land] · Die Heritage-Reise'),
 ('Questions, answered','Fragen und Antworten'),
 ('When is the Theyyam season?','Wann ist die Theyyam-Saison?'),
 ('The main season runs from late October to May. We suggest the best weeks when you enquire.','Die Hauptsaison dauert von Ende Oktober bis Mai. Die besten Wochen nennen wir Ihnen bei Ihrer Anfrage.'),
 ('Can I just turn up on my own?','Kann ich einfach allein hingehen?'),
 ('Some rituals are open, but many are family occasions and timings are hard to know. A local guide or a host who knows the family helps you in respectfully.','Manche Rituale sind offen, viele sind aber Familienanlässe, und die Zeiten sind schwer zu erfahren. Ein lokaler Guide oder Gastgeber, der die Familie kennt, hilft Ihnen, respektvoll dabei zu sein.'),
 ('Is it suitable for children and elders?','Ist es für Kinder und ältere Menschen geeignet?'),
 ('Yes, with planning. Rituals run late and involve standing, so we adjust pace and seating.','Ja, mit Planung. Rituale dauern bis spät in die Nacht und man steht viel, daher passen wir Tempo und Sitzplätze an.'),
 ('Can I take photos or video?','Darf ich fotografieren oder filmen?'),
 ('Not always. Many shrines ban photography and video, some during the whole ritual. Your guide tells you the rules at each place, and we suggest you simply be present.','Nicht immer. Viele Schreine verbieten Foto und Video, manche während des gesamten Rituals. Die Regeln vor Ort erfahren Sie von uns oder Ihrem Guide, und wir empfehlen, einfach dabei zu sein.'),
 ('Ready to meet the gods of Malabar?','Bereit, den Göttern Malabars zu begegnen?'),
 ('Tell us when you can travel. We reply within two working days.','Sagen Sie uns, wann Sie reisen können. Wir antworten innerhalb von zwei Werktagen.'),
 ('Guided Theyyam journeys across Kannur, Thalassery, Payyannur, Thaliparamba and Kanhangad.','Geführte Theyyam-Reisen in Kannur, Thalassery, Payyannur, Thaliparamba und Kanhangad.'),
 ('Placeholder photos from','Platzhalterfotos von'),
 # attributes
 ('aria-label="Main"','aria-label="Hauptmenü"'),('aria-label="Footer"','aria-label="Fußbereich"'),
 ('Faces of the Theyyams in our guide','Gesichter der Theyyams aus unserem Führer'),
 ('Illustrated face of a Theyyam','Gezeichnetes Gesicht eines Theyyam'),
 ('Kandanar Kelan Theyyam leaping across the fire at a shrine in Kannur','Das Kandanar-Kelan-Theyyam springt an einem Schrein in Kannur über das Feuer'),
 ('The Kandanar Kelan ritual: the Theyyam crosses the burning pit with devotees close by','Das Kandanar-Kelan-Ritual: Das Theyyam überquert die Glutgrube, Gläubige stehen nah dabei'),
 ('A Theyyam in a red and gold circular headdress among devotees','Ein Theyyam mit rotem und goldenem, kreisrundem Kopfschmuck unter Gläubigen'),
 ('Photographs from our Theyyam trips','Fotos von unseren Theyyam-Reisen'),
 ('A North Malabar shrine at night, decorated with marigold garlands and lamps','Ein Schrein in Nord-Malabar bei Nacht, mit Ringelblumengirlanden und Lampen geschmückt'),
 ('A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur','Ein Theyyam in einem großen roten und silbernen Kopfschmuck mit Blumen, an einem Schrein in Kannur'),
 ('A Theyyam in a red cone headdress at a family shrine by day in Kannur','Ein Theyyam mit rotem Kegel-Kopfschmuck an einem Familienschrein bei Tag in Kannur'),
 ('Close portrait of a Theyyam with orange face, silver ornaments and a white fringe','Nahaufnahme eines Theyyam mit orangefarbenem Gesicht, Silberschmuck und weißen Fransen'),
 ('Close view of a Theyyam face with red and silver ornaments','Nahaufnahme eines Theyyam-Gesichts mit roten und silbernen Verzierungen'),
 ('Portrait of a Theyyam in a red headdress during the ritual','Porträt eines Theyyam mit rotem Kopfschmuck während des Rituals'),
 ('Profile of a Theyyam in a red and gold headdress','Profil eines Theyyam mit rot-goldenem Kopfschmuck'),
 ('Photographs: LetsGoForACamp trips. Some Theyyam pages use Wikimedia Commons images (CC BY / BY-SA), credited on each page.','Fotos: Reisen von LetsGoForACamp. Manche Theyyam-Seiten nutzen Bilder von Wikimedia Commons (CC BY / BY-SA), die auf jeder Seite genannt sind.'),
 ('Why travellers trust us','Warum Reisende uns vertrauen'),
 ('aria-label="Rooted in North Malabar"','aria-label="Verwurzelt in Nord-Malabar"'),
 ('Close portrait of a Theyyam with intricate orange face paint','Nahaufnahme eines Theyyam mit kunstvoller orangefarbener Gesichtsbemalung'),
 ('Gold and red ornaments of a handmade Theyyam attire, North Kerala','Gold- und rote Verzierungen einer handgefertigten Theyyam-Tracht, Nord-Kerala'),
 ('A Theyyam appearing beside a drummer and devotees','Ein Theyyam erscheint neben einem Trommler und Gläubigen'),
 ('A person having body paint applied before a Theyyam','Körperbemalung vor einem Theyyam'),
 ('Illustrated map of the base towns on the North Malabar coast','Illustrierte Karte der Standorte an der Küste Nord-Malabars'),
 ('A Theyyam in red and gold face paint, shadowed','Ein Theyyam mit roter und goldener Gesichtsbemalung, im Schatten'),
 ('A Theyyam in a skirt of palm leaf strips at night','Ein Theyyam in einem Rock aus Palmblattstreifen bei Nacht'),
 ('A Theyyam in a red headdress among coconut palms','Ein Theyyam mit rotem Kopfschmuck zwischen Kokospalmen'),
 ]}
T['fr'] = {
 'lang': 'fr', 'title': 'LGFC Theyyam | Voyages accompagnés autour du Theyyam, Kerala du Nord',
 'desc': 'Découvrez le plus ancien rituel vivant du Kerala lors de voyages en petit groupe ou sur mesure à Kannur et Kasaragod. Hébergement et transferts, avec un guide local si vous le souhaitez. Contactez-nous.',
 'switchnote': 'Les autres pages sont pour l’instant en anglais. Utilisez la fonction de traduction de votre navigateur.',
 'pairs': [
 ('Skip to content','Aller au contenu'),
 ('Guided trips','Voyages accompagnés'),('>Journal<','>Journal<'),('>Menu<','>Menu<'),
 ('>Enquire<','>Nous contacter<'),('See trips','Voir les voyages'),
 ('Guided Theyyam tours · North Malabar, Kerala','Voyages Theyyam accompagnés · Malabar du Nord, Kerala'),
 ('A living ritual,','Un rituel vivant,'),('shared with respect','partagé avec respect'),
 ('Small-group journeys to Kerala’s oldest living ritual, planned around you, with a local guide if you want one to open doors, explain every step and keep you welcome.','Des voyages en petit groupe vers le plus ancien rituel vivant du Kerala, pensés autour de vous. Avec, si vous le souhaitez, un guide local qui ouvre les portes, explique chaque étape et veille à ce que vous soyez bien accueilli.'),
 ('Enquire about a trip','Demander un voyage'),('See guided trips','Voir les voyages accompagnés'),
 ('Season: Oct to May','Saison : oct. à mai'),('Group or private','Groupe ou privé'),('Stay + transfers','Séjour + transferts'),
 ('Rooted in North Malabar','Enracinés dans le Malabar du Nord'),
 ('Heritage · Family · Faith · Craft · Music · Story','Héritage · Famille · Foi · Savoir-faire · Musique · Récit'),
 ('years organising Theyyam tours','ans à organiser des voyages Theyyam'),
 ('explorers hosted on Theyyam trips','voyageurs accueillis sur nos voyages Theyyam'),
 ('support for booked trips','assistance pour les voyages réservés'),
 ('Made with warmth in North Malabar, Kerala · Powered by letsgoforacamp','Fait avec chaleur dans le Malabar du Nord, Kerala · Powered by letsgoforacamp'),
 ('Run by natives of North Malabar. Hosted like family.','Gérés par des natifs du Malabar du Nord. Accueillis comme en famille.'),
 ('We are a team of natives from Kannur and across North Malabar. After eight years of working with the families and villages of this region, we know who to ask, when to step back, and how to make a guest feel welcome.','Nous sommes une équipe originaire de Kannur et de tout le Malabar du Nord. Après huit ans de travail avec les familles et les villages de cette région, nous savons à qui demander, quand nous effacer et comment mettre un invité à l’aise.'),
 ('Local, not outsourced','Local, pas sous-traité'),
 ('Our team, and any guide or driver we arrange, are natives of North Malabar. Nobody reads you a script.','Notre équipe, ainsi que tout guide ou chauffeur que nous organisons, sont originaires du Malabar du Nord. Personne ne vous récite un texte.'),
 ('Known to the families','Connus des familles'),
 ('Introductions come from people the families already trust, so you are welcomed, not merely allowed in.','Les présentations passent par des personnes en qui les familles ont déjà confiance : vous êtes accueilli, pas simplement toléré.'),
 ('A real person replies','Une vraie personne vous répond'),
 ('No checkout and no call centre. Our North Malabar team answers within two working days, and is on call 24x7 once you are booked.','Pas de paiement en ligne ni de centre d’appels. Notre équipe du Malabar du Nord répond sous deux jours ouvrés et reste joignable 24 h/24 une fois votre voyage réservé.'),
 ('We protect the ritual','Nous protégeons le rituel'),
 ('We never publish ritual dates or places, we brief every guest on etiquette, and we follow each shrine’s rules on photography.','Nous ne publions jamais les dates ni les lieux des rituels, nous informons chaque voyageur des usages à respecter et nous suivons les règles de chaque sanctuaire en matière de photographie.'),
 ('Two ways to travel','Deux façons de voyager'),('Join a group or make it yours','Rejoindre un groupe ou créer le vôtre'),
 ('Small group departures','Départs en petit groupe'),
 ('Share the journey with up to 8 like-minded travellers. Departure windows are shared when you enquire.','Partagez le voyage avec jusqu’à 8 voyageurs partageant vos centres d’intérêt. Les périodes de départ vous sont communiquées sur demande.'),
 ('Enquire about a group trip','Demander un voyage en groupe'),
 ('Private and customised','Privé et sur mesure'),
 ('Your own dates, pace and interests, for family, friends, a special-interest group or a solo explorer. We design it with you.','Vos dates, votre rythme, vos centres d’intérêt, en famille, entre amis, en groupe thématique ou en solo. Nous le concevons avec vous.'),
 ('Enquire about a custom trip','Demander un voyage sur mesure'),
 ('Why go with us: the ritual is worship, and we help you be a good guest','Pourquoi voyager avec nous : le rituel est un acte de culte, et nous vous aidons à être un bon invité'),
 ('>Why go with us<','>Pourquoi nous<'),
 ('Access, arranged','Un accès organisé'),
 ('Rituals happen in family shrines and village grounds. We handle introductions and timing so you are welcome, not in the way.','Les rituels ont lieu dans des sanctuaires familiaux et sur les places des villages. Nous nous occupons des présentations et du moment, pour que vous soyez le bienvenu sans gêner.'),
 ('A local guide, if you want one','Un guide local, si vous le souhaitez'),
 ('Optional. Know who the deity is, what the story means, and when to step forward or hold back.','En option. Sachez qui est la divinité, ce que signifie son histoire, et quand s’approcher ou rester en retrait.'),
 ('Everything handled','Tout est pris en charge'),
 ('Night rituals and rural roads are hard alone. We run stays, transfers, meals and the late drive home.','Les rituels de nuit et les routes de campagne sont difficiles seul. Nous gérons hébergements, transferts, repas et le retour tardif.'),
 ('New here?','Première fois ?'),('What is Theyyam?','Qu’est-ce que le Theyyam ?'),
 ('A living ritual of north Kerala where the person who takes the kolam, after hours of painting and dressing, is believed to become the deity. Hundreds of forms exist, each with its own attire, song and story, kept by the same families for generations.','Un rituel vivant du nord du Kerala où la personne qui prend le kolam, après des heures de maquillage et d’habillage, est considérée comme devenant la divinité. Il en existe des centaines de formes, chacune avec sa parure, son chant et son histoire, gardées par les mêmes familles depuis des générations.'),
 ('Read the first-timer’s guide','Lire le guide du premier voyage'),('Meet the Theyyams','Découvrir les Theyyams'),
 ('Guided Theyyam trips: choose how deep you want to go','Voyages Theyyam accompagnés : choisissez jusqu’où aller'),
 ('Exact rituals are confirmed with you before you pay, because they depend on the day.','Les rituels exacts sont confirmés avec vous avant le paiement, car ils dépendent du jour.'),
 ('3 nights · Beginners','3 nuits · Débutants'),('The Heritage Journey','Le voyage Patrimoine'),
 ('Your first Theyyam, with the story behind it.','Votre premier Theyyam, avec l’histoire qui l’accompagne.'),
 ('5 nights · Enthusiasts','5 nuits · Passionnés'),('North Malabar Deep Dive','Plongée dans le Malabar du Nord'),
 ('Two bases, more nights, time with the families.','Deux bases, plus de nuits, du temps avec les familles.'),
 ('4 nights · Craft lovers','4 nuits · Amoureux de l’artisanat'),('Craft &amp; Attire Journey','Voyage Artisanat &amp; Parures'),
 ('Time with the maker of the attire, a musician and a weaver.','Du temps avec le fabricant de la parure, un musicien et un tisserand.'),
 ('Five base towns. One ritual coast.','Cinq villes-étapes. Une côte de rituels.'),
 ('We stay in comfortable towns and travel out to the rituals each night, so you sleep well and see more.','Nous séjournons dans des villes confortables et rejoignons les rituels chaque soir, pour que vous dormiez bien et voyiez davantage.'),
 ('· weavers, beaches, easy transfers','· tisserands, plages, transferts faciles'),('· fort town, food and cricket','· ville fortifiée, cuisine et cricket'),
 ('· the heartland of the ritual','· le cœur du rituel'),('· the northern gateway','· la porte du nord'),
 ('How it works','Comment ça marche'),
 ('Tell us your plan','Dites-nous votre projet'),('Month, group size, interests. Two minutes.','Mois, taille du groupe, centres d’intérêt. Deux minutes.'),
 ('We shape the trip','Nous composons le voyage'),('A proposal in two working days.','Une proposition sous deux jours ouvrés.'),
 ('We confirm rituals','Nous confirmons les rituels'),('Closer to travel, we lock the best nights.','Plus près du départ, nous arrêtons les meilleures nuits.'),
 ('You arrive, we host','Vous arrivez, nous accueillons'),('Stay and transfers are ready, and a guide if you chose one.','Hébergement et transferts sont prêts, et un guide si vous en avez choisi un.'),
 ('“[TRAVELLER TESTIMONIAL: one sentence on what the guide made possible]”','“[TÉMOIGNAGE DE VOYAGEUR : une phrase sur ce que le guide a rendu possible]”'),
 ('[Name], [Country] · The Heritage Journey','[Nom], [Pays] · Le voyage Patrimoine'),
 ('Questions, answered','Vos questions, nos réponses'),
 ('When is the Theyyam season?','Quand a lieu la saison du Theyyam ?'),
 ('The main season runs from late October to May. We suggest the best weeks when you enquire.','La saison principale va de fin octobre à mai. Nous vous indiquons les meilleures semaines lors de votre demande.'),
 ('Can I just turn up on my own?','Puis-je y aller seul ?'),
 ('Some rituals are open, but many are family occasions and timings are hard to know. A local guide or a host who knows the family helps you in respectfully.','Certains rituels sont ouverts, mais beaucoup sont des occasions familiales et les horaires sont difficiles à connaître. Un guide local ou un hôte qui connaît la famille vous aide à y assister avec respect.'),
 ('Is it suitable for children and elders?','Convient-il aux enfants et aux personnes âgées ?'),
 ('Yes, with planning. Rituals run late and involve standing, so we adjust pace and seating.','Oui, avec une bonne préparation. Les rituels se prolongent tard et se vivent debout, nous adaptons donc le rythme et les places assises.'),
 ('Can I take photos or video?','Puis-je prendre des photos ou filmer ?'),
 ('Not always. Many shrines ban photography and video, some during the whole ritual. Your guide tells you the rules at each place, and we suggest you simply be present.','Pas toujours. De nombreux sanctuaires interdisent photos et vidéos, certains pendant tout le rituel. Nous vous indiquons les règles de chaque lieu, et nous vous conseillons simplement d’être présent.'),
 ('Ready to meet the gods of Malabar?','Prêt à rencontrer les dieux du Malabar ?'),
 ('Tell us when you can travel. We reply within two working days.','Dites-nous quand vous pouvez partir. Nous répondons sous deux jours ouvrés.'),
 ('Guided Theyyam journeys across Kannur, Thalassery, Payyannur, Thaliparamba and Kanhangad.','Voyages Theyyam accompagnés à Kannur, Thalassery, Payyannur, Thaliparamba et Kanhangad.'),
 ('Placeholder photos from','Photos provisoires de'),
 ('aria-label="Main"','aria-label="Principal"'),('aria-label="Footer"','aria-label="Pied de page"'),
 ('Faces of the Theyyams in our guide','Visages des Theyyams de notre guide'),
 ('Illustrated face of a Theyyam','Visage illustré d’un Theyyam'),
 ('Kandanar Kelan Theyyam leaping across the fire at a shrine in Kannur','Le Theyyam Kandanar Kelan franchit le feu dans un sanctuaire de Kannur'),
 ('The Kandanar Kelan ritual: the Theyyam crosses the burning pit with devotees close by','Le rituel de Kandanar Kelan : le Theyyam traverse la fosse ardente, les fidèles tout proches'),
 ('A Theyyam in a red and gold circular headdress among devotees','Un Theyyam à la coiffe circulaire rouge et or parmi les fidèles'),
 ('Photographs from our Theyyam trips','Photographies de nos voyages Theyyam'),
 ('A North Malabar shrine at night, decorated with marigold garlands and lamps','Un sanctuaire du Malabar du Nord la nuit, orné de guirlandes d’œillets d’Inde et de lampes'),
 ('A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur','Un Theyyam coiffé d’un grand ornement rouge et argent fleuri, dans un sanctuaire de Kannur'),
 ('A Theyyam in a red cone headdress at a family shrine by day in Kannur','Un Theyyam à coiffe conique rouge dans un sanctuaire familial en plein jour, à Kannur'),
 ('Close portrait of a Theyyam with orange face, silver ornaments and a white fringe','Portrait rapproché d’un Theyyam au visage orange, avec ornements d’argent et franges blanches'),
 ('Close view of a Theyyam face with red and silver ornaments','Vue rapprochée d’un visage de Theyyam avec ornements rouges et argent'),
 ('Portrait of a Theyyam in a red headdress during the ritual','Portrait d’un Theyyam à coiffe rouge pendant le rituel'),
 ('Profile of a Theyyam in a red and gold headdress','Profil d’un Theyyam à coiffe rouge et or'),
 ('Photographs: LetsGoForACamp trips. Some Theyyam pages use Wikimedia Commons images (CC BY / BY-SA), credited on each page.','Photos : voyages de LetsGoForACamp. Certaines pages Theyyam utilisent des images de Wikimedia Commons (CC BY / BY-SA), créditées sur chaque page.'),
 ('Why travellers trust us','Pourquoi les voyageurs nous font confiance'),
 ('aria-label="Rooted in North Malabar"','aria-label="Enracinés dans le Malabar du Nord"'),
 ('Close portrait of a Theyyam with intricate orange face paint','Portrait rapproché d’un Theyyam au maquillage orange très travaillé'),
 ('Gold and red ornaments of a handmade Theyyam attire, North Kerala','Ornements dorés et rouges d’une parure Theyyam faite main, Kerala du Nord'),
 ('A Theyyam appearing beside a drummer and devotees','Un Theyyam apparaît près d’un tambourinaire et de fidèles'),
 ('A person having body paint applied before a Theyyam','Application du maquillage corporel avant un Theyyam'),
 ('Illustrated map of the base towns on the North Malabar coast','Carte illustrée des villes-étapes sur la côte du Malabar du Nord'),
 ('A Theyyam in red and gold face paint, shadowed','Un Theyyam au maquillage rouge et or, dans l’ombre'),
 ('A Theyyam in a skirt of palm leaf strips at night','Un Theyyam en jupe de lanières de feuilles de palmier, de nuit'),
 ('A Theyyam in a red headdress among coconut palms','Un Theyyam coiffé de rouge parmi les cocotiers'),
 ]}
T['es'] = {
 'lang': 'es', 'title': 'LGFC Theyyam | Viajes guiados al Theyyam en el norte de Kerala',
 'desc': 'Conozca el ritual vivo más antiguo de Kerala en viajes en grupo reducido o a medida por Kannur y Kasaragod. Alojamiento y traslados, con guía local si lo desea. Consúltenos.',
 'switchnote': 'Las demás páginas están por ahora en inglés. Use la función de traducción de su navegador.',
 'pairs': [
 ('Skip to content','Saltar al contenido'),
 ('Guided trips','Viajes guiados'),('>Journal<','>Diario<'),('>Menu<','>Menú<'),
 ('>Enquire<','>Consultar<'),('See trips','Ver viajes'),
 ('Guided Theyyam tours · North Malabar, Kerala','Viajes guiados al Theyyam · Malabar del Norte, Kerala'),
 ('A living ritual,','Un ritual vivo,'),('shared with respect','compartido con respeto'),
 ('Small-group journeys to Kerala’s oldest living ritual, planned around you, with a local guide if you want one to open doors, explain every step and keep you welcome.','Viajes en grupo reducido al ritual vivo más antiguo de Kerala, planificados a su medida. Si lo desea, con un guía local que abre puertas, explica cada paso y cuida de que sea bienvenido.'),
 ('Enquire about a trip','Consultar un viaje'),('See guided trips','Ver viajes guiados'),
 ('Season: Oct to May','Temporada: oct. a mayo'),('Group or private','Grupo o privado'),('Stay + transfers','Alojamiento + traslados'),
 ('Rooted in North Malabar','Arraigados en el Malabar del Norte'),
 ('Heritage · Family · Faith · Craft · Music · Story','Herencia · Familia · Fe · Artesanía · Música · Relato'),
 ('years organising Theyyam tours','años organizando viajes al Theyyam'),
 ('explorers hosted on Theyyam trips','viajeros acogidos en viajes al Theyyam'),
 ('support for booked trips','atención en viajes reservados'),
 ('Made with warmth in North Malabar, Kerala · Powered by letsgoforacamp','Hecho con cariño en el Malabar del Norte, Kerala · Powered by letsgoforacamp'),
 ('Run by natives of North Malabar. Hosted like family.','Dirigido por gente del Malabar del Norte. Le acogemos como en familia.'),
 ('We are a team of natives from Kannur and across North Malabar. After eight years of working with the families and villages of this region, we know who to ask, when to step back, and how to make a guest feel welcome.','Somos un equipo de gente de Kannur y de todo el Malabar del Norte. Tras ocho años trabajando con las familias y los pueblos de esta región, sabemos a quién preguntar, cuándo dar un paso atrás y cómo hacer que un invitado se sienta bienvenido.'),
 ('Local, not outsourced','Local, no subcontratado'),
 ('Our team, and any guide or driver we arrange, are natives of North Malabar. Nobody reads you a script.','Nuestro equipo, y cualquier guía o conductor que organicemos, son del Malabar del Norte. Nadie le lee un guion.'),
 ('Known to the families','Conocidos por las familias'),
 ('Introductions come from people the families already trust, so you are welcomed, not merely allowed in.','Las presentaciones llegan de personas en quienes las familias ya confían, así que le reciben con gusto, no solo le dejan entrar.'),
 ('A real person replies','Le responde una persona real'),
 ('No checkout and no call centre. Our North Malabar team answers within two working days, and is on call 24x7 once you are booked.','Sin pago en línea y sin centro de llamadas. Nuestro equipo del Malabar del Norte responde en dos días laborables y está disponible las 24 horas una vez reservado el viaje.'),
 ('We protect the ritual','Protegemos el ritual'),
 ('We never publish ritual dates or places, we brief every guest on etiquette, and we follow each shrine’s rules on photography.','Nunca publicamos fechas ni lugares de rituales, informamos a cada viajero sobre la etiqueta y seguimos las normas de fotografía de cada santuario.'),
 ('Two ways to travel','Dos formas de viajar'),('Join a group or make it yours','Súmese a un grupo o hágalo suyo'),
 ('Small group departures','Salidas en grupo reducido'),
 ('Share the journey with up to 8 like-minded travellers. Departure windows are shared when you enquire.','Comparta el viaje con hasta 8 viajeros con intereses afines. Las fechas de salida se las indicamos al consultar.'),
 ('Enquire about a group trip','Consultar un viaje en grupo'),
 ('Private and customised','Privado y a medida'),
 ('Your own dates, pace and interests, for family, friends, a special-interest group or a solo explorer. We design it with you.','Sus fechas, su ritmo y sus intereses, para familia, amigos, un grupo de interés especial o viajeros en solitario. Lo diseñamos con usted.'),
 ('Enquire about a custom trip','Consultar un viaje a medida'),
 ('Why go with us: the ritual is worship, and we help you be a good guest','Por qué viajar con nosotros: el ritual es un acto de culto, y le ayudamos a ser un buen invitado'),
 ('>Why go with us<','>Por qué nosotros<'),
 ('Access, arranged','Acceso, gestionado'),
 ('Rituals happen in family shrines and village grounds. We handle introductions and timing so you are welcome, not in the way.','Los rituales tienen lugar en santuarios familiares y plazas de los pueblos. Nos ocupamos de las presentaciones y del momento para que sea bienvenido y no estorbe.'),
 ('A local guide, if you want one','Un guía local, si lo desea'),
 ('Optional. Know who the deity is, what the story means, and when to step forward or hold back.','Opcional. Sepa quién es la deidad, qué significa su historia y cuándo acercarse o mantenerse al margen.'),
 ('Everything handled','Todo resuelto'),
 ('Night rituals and rural roads are hard alone. We run stays, transfers, meals and the late drive home.','Los rituales nocturnos y las carreteras rurales son difíciles por cuenta propia. Nos ocupamos de alojamientos, traslados, comidas y el regreso tardío.'),
 ('New here?','¿Primera vez?'),('What is Theyyam?','¿Qué es el Theyyam?'),
 ('A living ritual of north Kerala where the person who takes the kolam, after hours of painting and dressing, is believed to become the deity. Hundreds of forms exist, each with its own attire, song and story, kept by the same families for generations.','Un ritual vivo del norte de Kerala en el que la persona que toma el kolam, tras horas de pintura y vestimenta, se considera que se convierte en la deidad. Existen cientos de formas, cada una con su atuendo, su canto y su historia, conservadas por las mismas familias durante generaciones.'),
 ('Read the first-timer’s guide','Leer la guía para quien llega por primera vez'),('Meet the Theyyams','Conocer los Theyyams'),
 ('Guided Theyyam trips: choose how deep you want to go','Viajes guiados al Theyyam: elija hasta dónde profundizar'),
 ('Exact rituals are confirmed with you before you pay, because they depend on the day.','Los rituales exactos se confirman con usted antes del pago, porque dependen del día.'),
 ('3 nights · Beginners','3 noches · Principiantes'),('The Heritage Journey','El viaje Patrimonio'),
 ('Your first Theyyam, with the story behind it.','Su primer Theyyam, con la historia que lo acompaña.'),
 ('5 nights · Enthusiasts','5 noches · Aficionados'),('North Malabar Deep Dive','Inmersión en el Malabar del Norte'),
 ('Two bases, more nights, time with the families.','Dos bases, más noches, tiempo con las familias.'),
 ('4 nights · Craft lovers','4 noches · Amantes de la artesanía'),('Craft &amp; Attire Journey','Viaje de Artesanía &amp; Atuendo'),
 ('Time with the maker of the attire, a musician and a weaver.','Tiempo con quien confecciona el atuendo, un músico y un tejedor.'),
 ('Five base towns. One ritual coast.','Cinco ciudades base. Una costa de rituales.'),
 ('We stay in comfortable towns and travel out to the rituals each night, so you sleep well and see more.','Nos alojamos en ciudades cómodas y nos desplazamos a los rituales cada noche, para que duerma bien y vea más.'),
 ('· weavers, beaches, easy transfers','· tejedores, playas, traslados fáciles'),('· fort town, food and cricket','· ciudad fortificada, comida y cricket'),
 ('· the heartland of the ritual','· el corazón del ritual'),('· the northern gateway','· la puerta del norte'),
 ('How it works','Cómo funciona'),
 ('Tell us your plan','Cuéntenos su plan'),('Month, group size, interests. Two minutes.','Mes, tamaño del grupo, intereses. Dos minutos.'),
 ('We shape the trip','Diseñamos el viaje'),('A proposal in two working days.','Una propuesta en dos días laborables.'),
 ('We confirm rituals','Confirmamos los rituales'),('Closer to travel, we lock the best nights.','Cerca de la fecha del viaje, fijamos las mejores noches.'),
 ('You arrive, we host','Usted llega, nosotros acogemos'),('Stay and transfers are ready, and a guide if you chose one.','El alojamiento y los traslados están listos, y un guía si lo ha elegido.'),
 ('“[TRAVELLER TESTIMONIAL: one sentence on what the guide made possible]”','“[TESTIMONIO DE VIAJERO: una frase sobre lo que el guía hizo posible]”'),
 ('[Name], [Country] · The Heritage Journey','[Nombre], [País] · El viaje Patrimonio'),
 ('Questions, answered','Preguntas y respuestas'),
 ('When is the Theyyam season?','¿Cuándo es la temporada del Theyyam?'),
 ('The main season runs from late October to May. We suggest the best weeks when you enquire.','La temporada principal va de finales de octubre a mayo. Le sugerimos las mejores semanas cuando nos consulte.'),
 ('Can I just turn up on my own?','¿Puedo ir por mi cuenta?'),
 ('Some rituals are open, but many are family occasions and timings are hard to know. A local guide or a host who knows the family helps you in respectfully.','Algunos rituales son abiertos, pero muchos son ocasiones familiares y los horarios son difíciles de conocer. Un guía local o un anfitrión que conoce a la familia le ayuda a estar presente con respeto.'),
 ('Is it suitable for children and elders?','¿Es adecuado para niños y personas mayores?'),
 ('Yes, with planning. Rituals run late and involve standing, so we adjust pace and seating.','Sí, con planificación. Los rituales se alargan hasta tarde y se viven de pie, así que ajustamos el ritmo y los asientos.'),
 ('Can I take photos or video?','¿Puedo hacer fotos o vídeos?'),
 ('Not always. Many shrines ban photography and video, some during the whole ritual. Your guide tells you the rules at each place, and we suggest you simply be present.','No siempre. Muchos santuarios prohíben fotos y vídeo, algunos durante todo el ritual. Le indicamos las normas de cada lugar y le sugerimos simplemente estar presente.'),
 ('Ready to meet the gods of Malabar?','¿Listo para conocer a los dioses del Malabar?'),
 ('Tell us when you can travel. We reply within two working days.','Díganos cuándo puede viajar. Respondemos en dos días laborables.'),
 ('Guided Theyyam journeys across Kannur, Thalassery, Payyannur, Thaliparamba and Kanhangad.','Viajes guiados al Theyyam por Kannur, Thalassery, Payyannur, Thaliparamba y Kanhangad.'),
 ('Placeholder photos from','Fotos provisionales de'),
 ('aria-label="Main"','aria-label="Principal"'),('aria-label="Footer"','aria-label="Pie de página"'),
 ('Faces of the Theyyams in our guide','Rostros de los Theyyams de nuestra guía'),
 ('Illustrated face of a Theyyam','Rostro ilustrado de un Theyyam'),
 ('Kandanar Kelan Theyyam leaping across the fire at a shrine in Kannur','El Theyyam Kandanar Kelan salta sobre el fuego en un santuario de Kannur'),
 ('The Kandanar Kelan ritual: the Theyyam crosses the burning pit with devotees close by','El ritual de Kandanar Kelan: el Theyyam cruza el foso de brasas con los devotos cerca'),
 ('A Theyyam in a red and gold circular headdress among devotees','Un Theyyam con tocado circular rojo y dorado entre los devotos'),
 ('Photographs from our Theyyam trips','Fotografías de nuestros viajes Theyyam'),
 ('A North Malabar shrine at night, decorated with marigold garlands and lamps','Un santuario del Malabar del Norte de noche, adornado con guirnaldas de caléndulas y lámparas'),
 ('A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur','Un Theyyam con un gran tocado rojo y plateado con flores, en un santuario de Kannur'),
 ('A Theyyam in a red cone headdress at a family shrine by day in Kannur','Un Theyyam con tocado cónico rojo en un santuario familiar de día, en Kannur'),
 ('Close portrait of a Theyyam with orange face, silver ornaments and a white fringe','Retrato de cerca de un Theyyam con el rostro naranja, adornos de plata y flecos blancos'),
 ('Close view of a Theyyam face with red and silver ornaments','Vista cercana del rostro de un Theyyam con adornos rojos y plateados'),
 ('Portrait of a Theyyam in a red headdress during the ritual','Retrato de un Theyyam con tocado rojo durante el ritual'),
 ('Profile of a Theyyam in a red and gold headdress','Perfil de un Theyyam con tocado rojo y dorado'),
 ('Photographs: LetsGoForACamp trips. Some Theyyam pages use Wikimedia Commons images (CC BY / BY-SA), credited on each page.','Fotos: viajes de LetsGoForACamp. Algunas páginas de Theyyam usan imágenes de Wikimedia Commons (CC BY / BY-SA), con crédito en cada página.'),
 ('Why travellers trust us','Por qué los viajeros confían en nosotros'),
 ('aria-label="Rooted in North Malabar"','aria-label="Arraigados en el Malabar del Norte"'),
 ('Close portrait of a Theyyam with intricate orange face paint','Retrato de cerca de un Theyyam con elaborada pintura facial naranja'),
 ('Gold and red ornaments of a handmade Theyyam attire, North Kerala','Adornos dorados y rojos de un atuendo de Theyyam hecho a mano, norte de Kerala'),
 ('A Theyyam appearing beside a drummer and devotees','Un Theyyam aparece junto a un tamborilero y los devotos'),
 ('A person having body paint applied before a Theyyam','Aplicación de pintura corporal antes de un Theyyam'),
 ('Illustrated map of the base towns on the North Malabar coast','Mapa ilustrado de las ciudades base en la costa del Malabar del Norte'),
 ('A Theyyam in red and gold face paint, shadowed','Un Theyyam con pintura facial roja y dorada, en sombra'),
 ('A Theyyam in a skirt of palm leaf strips at night','Un Theyyam con falda de tiras de hoja de palma, de noche'),
 ('A Theyyam in a red headdress among coconut palms','Un Theyyam con tocado rojo entre cocoteros'),
 ]}

def build(code):
    t = T[code]
    s = BASE
    # protect the (unchanged) English marquee words before the generic pairs run on shorter strings
    for a, b in sorted(t['pairs'], key=lambda p: -len(p[0])):
        if a not in s:
            print('  MISSING in', code, ':', a[:60])
        s = s.replace(a, b)
    s = s.replace('<html lang="en">', f'<html lang="{t["lang"]}">')
    s = re.sub(r'<title>.*?</title>', f'<title>{t["title"]}</title>', s, count=1)
    s = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + t['desc'], s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + t['title'], s, count=1)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + t['desc'], s, count=1)
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', '', s, flags=re.S)
    s = s.replace('<script src="assets/search.js" defer></script>', '')
    # links: home and faq stay inside this language page, everything else goes to the English page
    s = s.replace('href="index.html#faq"', 'href="#faq"').replace('href="index.html"', 'href="index.html"')
    s = re.sub(r'(href|src)="(?!https?:|#|index\.html|mailto:)([^"]+)"', lambda m: f'{m.group(1)}="../{m.group(2)}"', s)
    s = s.replace('url(assets/', 'url(../assets/')
    s = re.sub(r'<link rel="canonical"[^>]*>', '', s)
    s = s.replace('</head>', hreflang() + f'<link rel="canonical" href="{SITE}{code}/">' + '</head>', 1)
    s = s.replace('<nav class="nv"', switcher(code, '../') + '<nav class="nv"', 1)
    # note under the footer
    s = s.replace('<div class="bar">', f'<p style="background:#4A0E12;color:#fff;opacity:.9;font-size:13px;margin:0;padding:0 20px 20px;text-align:center">{t["switchnote"]}</p><div class="bar">', 1)
    os.makedirs(code, exist_ok=True)
    open(f'{code}/index.html', 'w', encoding='utf-8').write(s)
    return s

for c in ('de', 'fr', 'es'):
    out = build(c)
    print(c, len(out))

# English page: hreflang + switcher (idempotent, already stripped from BASE)
en = BASE.replace('</head>', hreflang() + '</head>', 1).replace('<nav class="nv"', switcher('en', '') + '<nav class="nv"', 1)
open('index.html', 'w', encoding='utf-8').write(en)
