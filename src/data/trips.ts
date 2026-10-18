export interface Trip {
  id: 'one-night' | 'two-nights' | 'immersion';
  name: string;
  /** "1 night", "2 nights", "3+ days" */
  length: string;
  /** ISO 8601 duration for structured data; omitted when the length is open ended */
  duration?: string;
  base: string;
  level: string;
  blurb: string;
  bullets: string[];
  img: string; // under public/assets/
  alt: string;
  width: number;
  height: number;
  /** place named in the structured data */
  itinerary: string;
}

// Three programmes: one night, two nights and a deeper immersion of three or more days.
export const trips: Trip[] = [
  {
    id: 'one-night', name: 'A Night at the Kavu', length: '1 night', duration: 'P2D', base: 'Base: Kannur', level: 'First encounter',
    blurb: 'Your first Theyyam in a single night. An evening at a village shrine, the ritual through the night and a slow morning after, with an optional guide who explains each step.',
    bullets: ['1 ritual night, local guide optional', 'A short, easy way in for first-timers', 'Stay and private transfers'],
    img: 'blog/theyyam-etiquette.jpg', alt: 'A village shrine at night with a flagstaff of palm leaves and marigold garlands', width: 1200, height: 675,
    itinerary: 'Kannur, North Malabar, Kerala',
  },
  {
    id: 'two-nights', name: 'Two Nights in Kolathunadu', length: '2 nights', duration: 'P3D', base: 'Base: Kannur', level: 'Beginners',
    blurb: 'Time to see more. The ritual night, a slow cultural day of weaving, food and coast, and time to rest between late finishes. Kolathunadu is the old name of the Kannur region.',
    bullets: ['1 to 2 ritual nights, depending on the season', '1 day of weaving, food and coast', 'Boutique stay, private transfers'],
    img: 'blog/what-is-theyyam.jpg', alt: 'Close portrait of a Theyyam with a yellow painted face, silver crown and flower garlands', width: 1200, height: 675,
    itinerary: 'Kannur, North Malabar, Kerala',
  },
  {
    id: 'immersion', name: 'North Malabar Deep Immersion', length: '3+ days', base: 'Bases: Kannur, Kanhangad, Thalassery', level: 'Enthusiasts and craft lovers',
    blurb: 'For travellers who want to go deeper. Three or more days across the district line: several ritual nights, a visit with a family that keeps the Theyyam, and the people behind the ritual, the maker of the attire, a musician and a weaver.',
    bullets: ['3 or more days, 3 to 4 ritual nights', 'Time with a family that keeps the Theyyam', 'Meet the attire maker, a musician and a weaver', 'Smaller group and a slower pace'],
    img: 'blog/attire-and-craft.jpg', alt: 'A craftsman weaving yellow palm fibre for Theyyam attire', width: 1200, height: 675,
    itinerary: 'Kannur, Kanhangad and Thalassery, North Malabar, Kerala',
  },
];
