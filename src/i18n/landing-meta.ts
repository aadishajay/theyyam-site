import type { Lang } from '../lib/site';

// <head> copy and structured-data strings for the landing page of each language.
export const landingMeta: Record<Lang, { title: string; description: string; ogAlt: string; orgDescription: string; crumb: string; credit: string }> = {
  en: {
    title: 'Guided Theyyam Tours in North Malabar, Kerala | LGFC Theyyam',
    description: 'Small-group and custom Theyyam tours in Kannur and Kasaragod. Stays and transfers, with a local guide if you want one. Enquire for a quote.',
    ogAlt: 'A Theyyam in a large red and silver headdress at a shrine in Kannur, Kerala',
    orgDescription: 'Guided Theyyam tours and cultural journeys in North Malabar, Kerala: small-group and private trips in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba and Kanhangad.',
    crumb: 'Home', credit: 'Photograph: LetsGoForACamp',
  },
  de: {
    title: 'Geführte Kulturreisen zum Theyyam in Nordkerala | LGFC Theyyam',
    description: 'Geführte Theyyam-Reisen in Kannur und Kasaragod: Kleingruppe oder individuell, mit Unterkunft und Transfers, auf Wunsch mit Guide. Jetzt anfragen.',
    ogAlt: 'Ein Theyyam in großem rotem und silbernem Kopfschmuck an einem Schrein in Kannur, Kerala',
    orgDescription: 'Geführte Theyyam-Reisen und Kulturreisen in Nord-Malabar, Kerala: Kleingruppen- und Privatreisen in Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba und Kanhangad.',
    crumb: 'Startseite', credit: 'Foto: LetsGoForACamp',
  },
  fr: {
    title: 'Voyages culturels autour du Theyyam | LGFC Theyyam',
    description: 'Voyages Theyyam en petit groupe ou sur mesure à Kannur et Kasaragod. Hébergement, transferts et guide local en option. Demandez un devis.',
    ogAlt: 'Un Theyyam coiffé d’un grand ornement rouge et argent dans un sanctuaire de Kannur, Kerala',
    orgDescription: 'Voyages culturels pour découvrir le Theyyam dans le Malabar du Nord, Kerala : petits groupes et voyages privés à Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba et Kanhangad.',
    crumb: 'Accueil', credit: 'Photo : LetsGoForACamp',
  },
  es: {
    title: 'Viajes culturales para descubrir el Theyyam | LGFC Theyyam',
    description: 'Viajes al Theyyam en grupo reducido o a medida en Kannur y Kasaragod. Alojamiento, traslados y guía local opcional. Pida presupuesto.',
    ogAlt: 'Un Theyyam con un gran tocado rojo y plateado en un santuario de Kannur, Kerala',
    orgDescription: 'Viajes culturales para descubrir el Theyyam en el Malabar del Norte, Kerala: grupos reducidos y viajes privados en Kannur, Kasaragod, Thalassery, Payyannur, Thaliparamba y Kanhangad.',
    crumb: 'Inicio', credit: 'Foto: LetsGoForACamp',
  },
};
