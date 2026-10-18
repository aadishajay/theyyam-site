export interface Trip {
  id: 'heritage' | 'deep-dive' | 'craft';
  name: string;
  nights: number;
  base: string;
  level: string;
  blurb: string;
  bullets: string[];
  img: string;
  alt: string;
  width: number;
  height: number;
  /** place named in the structured data */
  itinerary: string;
}

export const trips: Trip[] = [
  {
    id: 'heritage', name: 'The Heritage Journey', nights: 3, base: 'Base: Kannur', level: 'Beginners',
    blurb: 'Your first Theyyam, with the story behind it. Two ritual nights and one slow cultural day, with an optional guide who translates the songs, attire and gestures.',
    bullets: ['2 ritual nights, local guide optional', '1 day of weaving, food and coast', 'Boutique stay, private transfers'],
    img: 'lgfc-ornaments.jpg', alt: 'Close view of a Theyyam face with red and silver ornaments', width: 900, height: 600,
    itinerary: 'Kannur, North Malabar, Kerala',
  },
  {
    id: 'deep-dive', name: 'North Malabar Deep Dive', nights: 5, base: 'Bases: Kannur + Kanhangad', level: 'Enthusiasts',
    blurb: 'Cross the district line and see how the tradition changes. More ritual nights, a visit with a Theyyam family and time to rest between late finishes.',
    bullets: ['3 to 4 ritual nights, local guide optional', 'Time with a family that keeps the Theyyam', 'Two stays, all transfers'],
    img: 'lgfc-shrine-night.jpg', alt: 'A North Malabar shrine at night, decorated with marigold garlands and lamps', width: 900, height: 600,
    itinerary: 'Kannur and Kanhangad, North Malabar, Kerala',
  },
  {
    id: 'craft', name: 'Craft & Attire Journey', nights: 4, base: 'Base: Thalassery', level: 'Craft lovers',
    blurb: 'Meet the people behind the ritual: the maker of the attire, a musician, a weaver. A smaller group and a slower pace.',
    bullets: ['Group of up to 5', 'Pre-trip briefing on ritual etiquette', 'Flexible rest days'],
    img: 'lgfc-headdress-shrine.jpg', alt: 'A Theyyam in a large red and silver headdress with flowers, at a shrine in Kannur', width: 900, height: 720,
    itinerary: 'Thalassery, North Malabar, Kerala',
  },
];
