import { defineConfig } from 'astro/config';
import remarkDirective from 'remark-directive';
import remarkBlocks from './src/plugins/remark-blocks.mjs';
import { site, base } from './src/lib/env.mjs';
import { fileURLToPath } from 'node:url';
import { existsSync, mkdirSync, renameSync } from 'node:fs';
import { join } from 'node:path';

// build.format 'file' writes /theyyams as theyyams.html; the live URLs (/theyyams/, /de/ ...) need <dir>/index.html.
const dirIndex = (dirs) => ({
  name: 'dir-index',
  hooks: {
    'astro:build:done': ({ dir }) => {
      const out = fileURLToPath(dir);
      for (const d of dirs) {
        const f = join(out, `${d}.html`);
        if (!existsSync(f)) continue;
        mkdirSync(join(out, d), { recursive: true });
        renameSync(f, join(out, d, 'index.html'));
      }
    },
  },
});

// SITE and BASE come from the environment so the same build serves the review URL and the launch domain:
//   review (GitHub Pages):  SITE=https://aadishajay.github.io BASE=/theyyam-site   (defaults)
//   launch (own domain):    SITE=https://your-domain.com    BASE=/

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  build: { format: 'file', inlineStylesheets: 'always' },
  integrations: [dirIndex(['theyyams', 'de', 'fr', 'es'])],
  markdown: { remarkPlugins: [remarkDirective, remarkBlocks] },
});
