export interface JournalCard { slug: string; img: string; alt: string; width: number; height: number; k: string; title: string }

// Cards shown on the journal index (image, label and headline are chosen for the index and can differ from the article itself).
export const featured = {
  "slug": "what-is-theyyam",
  "img": "lgfc-ornaments.jpg",
  "alt": "Close view of a Theyyam face with red and silver ornaments",
  "width": 900,
  "height": 675,
  "k": "Featured · Culture · 9 min read",
  "title": "What is Theyyam? A first-timer’s guide to Kerala’s living ritual",
  "blurb": "The gods, the families and the ritual, explained before you arrive."
};

export const latest: JournalCard[] = [
  {
    "slug": "steps-of-a-theyyam",
    "img": "lgfc-headdress-shrine.jpg",
    "alt": "A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur",
    "width": 600,
    "height": 400,
    "k": "Culture · 8 min",
    "title": "The steps of a Theyyam: thottam, vellattam, purappadu and more explained"
  },
  {
    "slug": "theyyam-etiquette",
    "img": "lgfc-portrait-ritual.jpg",
    "alt": "Portrait of a Theyyam in a red headdress during the ritual",
    "width": 600,
    "height": 400,
    "k": "Etiquette · 6 min",
    "title": "Theyyam etiquette: do’s and don’ts for visitors"
  },
  {
    "slug": "theyyam-season",
    "img": "lgfc-daytime-theyyam.jpg",
    "alt": "A Theyyam in a red cone headdress at a family shrine by day in Kannur",
    "width": 600,
    "height": 400,
    "k": "Planning · 7 min",
    "title": "Theyyam season: the best months to visit North Malabar"
  },
  {
    "slug": "planning-theyyam-on-your-own",
    "img": "lgfc-shrine-night.jpg",
    "alt": "A North Malabar shrine at night, decorated with marigold garlands and lamps",
    "width": 600,
    "height": 400,
    "k": "Planning · 6 min",
    "title": "Why Theyyam is hard to plan on your own"
  },
  {
    "slug": "main-theyyams",
    "img": "lgfc-headdress-shrine.jpg",
    "alt": "A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur",
    "width": 600,
    "height": 400,
    "k": "Theyyam types · 8 min",
    "title": "Muthappan, Pottan and Vishnumoorthi: the main Theyyams"
  },
  {
    "slug": "attire-and-craft",
    "img": "lgfc-ornaments.jpg",
    "alt": "Close view of a Theyyam face with red and silver ornaments",
    "width": 600,
    "height": 400,
    "k": "Culture · 5 min",
    "title": "Attire and craft: how a Theyyam’s attire is made"
  },
  {
    "slug": "cameras-and-ritual",
    "img": "lgfc-headdress-shrine.jpg",
    "alt": "A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur",
    "width": 600,
    "height": 480,
    "k": "Etiquette · 6 min",
    "title": "Cameras and ritual: why some Theyyams allow no photos or video"
  }
];
