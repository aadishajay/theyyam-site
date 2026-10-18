import { marked } from 'marked';

/** inline Markdown (links, emphasis) -> HTML */
export const inline = (s: string) => marked.parseInline(s, { async: false }) as string;
/** Markdown -> plain text (for structured data) */
export const plain = (s: string) =>
  s.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[*_`]/g, '');
