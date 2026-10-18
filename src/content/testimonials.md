---
# Single source for guest testimonials (landing pages and the trips page).
# Items are anonymised guest feedback from the VoiceTraq post-trip form: shown as "Theyyam Trip <place>, <month year>".
# Coordinator names are replaced with "the guide". Quotes are the guests' own words; only spelling and obvious
# typing slips were corrected, and a few sentences are shortened with an ellipsis (…).
# Published items rotate in the landing-page carousel (in this order, with the photo of their trip from `trips`).
# The same items, after the first, also appear in "What guests say" on the trips page.
# Cover photos are one group photo or highlight per trip (public/assets/testimonials/). Check guests are happy to be shown.
trips:
  feb26:
    image: "group-feb-2026.jpg"
    alt: "Guests of the Theyyam trip standing together under a large banyan tree"
  mar25-payyanur:
    image: "group-mar-2025-payyanur.jpg"
    alt: "Guests of the Theyyam trip standing together under a banyan tree near a shrine"
  mar25-kasaragod:
    image: "highlight-mar-2025-kasaragod.jpg"
    alt: "A Theyyam with a yellow painted face in red and white attire"
items:
  - id: "feb26-kandanar-kelan"
    quote: "Thank you so much for the trip, it was truly a divine experience and I feel like Kandanar Kelan showed me that the human psyche is divine and limitless."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Feb 2026"
    trip: "feb26"
    source: "feedback"
    published: true
    theyyam: true
  - id: "mar25-guide-comms"
    quote: "The guide did a great job in terms of communication and updates."
    label: "Theyyam Trip Kasaragod"
    date: "Mar 2025"
    trip: "mar25-kasaragod"
    source: "feedback"
    published: true
    theyyam: true
  - id: "mar25-organised"
    quote: "The guide meticulously organized and executed the trip in a timely manner."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Mar 2025"
    trip: "mar25-payyanur"
    source: "feedback"
    published: true
    theyyam: true
  - id: "feb26-everything"
    quote: "Happy with everything, excellent job guys. Thank you, we will be travelling again with you soon."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Feb 2026"
    trip: "feb26"
    source: "feedback"
    published: true
    theyyam: true
  - id: "mar25-stay-food"
    quote: "Stay was awesome as well as the food."
    label: "Theyyam Trip Kasaragod"
    date: "Mar 2025"
    trip: "mar25-kasaragod"
    source: "feedback"
    published: true
    theyyam: true
  - id: "feb26-guide-knowledge"
    quote: "The guide is thoroughly familiar with all the rituals … which shows the deep knowledge in her. That is truly remarkable."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Feb 2026"
    trip: "feb26"
    source: "feedback"
    published: true
    theyyam: true
  - id: "feb26-guide-calm"
    quote: "The guide co-ordinates well and is capable of handling all age groups, and calmly answers all the questions we shoot."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Feb 2026"
    trip: "feb26"
    source: "feedback"
    published: true
    theyyam: true
  - id: "feb26-stay"
    quote: "Comfortable and excellent stay."
    label: "Theyyam Trip Payyanur, Kannur"
    date: "Feb 2026"
    trip: "feb26"
    source: "feedback"
    published: true
    theyyam: true
  - id: "example"
    quote: "[TRAVELLER TESTIMONIAL: one sentence on what the guide made possible]"
    label: "[Trip name and place]"
    date: "[Month year]"
    trip: "feb26"
    source: "email"
    published: false
    theyyam: true
---
