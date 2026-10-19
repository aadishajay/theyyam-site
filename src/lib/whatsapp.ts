import contact from '../data/contact.json';

/** wa.me link for the business number with a prefilled message (defaults to the standard enquiry line). */
export const waLink = (text: string = contact.whatsappMessage) =>
  `https://wa.me/${contact.phone.replace(/\D/g, '')}?text=${encodeURIComponent(text)}`;
