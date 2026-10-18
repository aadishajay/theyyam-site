#!/usr/bin/env bash
# Build locally and publish ONLY the static output (dist/) to the gh-pages branch.
# GitHub Pages serves that branch; the source stays on main.
#   npm run deploy                      review site (noindex)
#   SITE=https://example.com BASE=/ INDEXABLE=1 npm run deploy
set -euo pipefail
cd "$(dirname "$0")/.."
remote=$(git remote get-url origin)
npm run build
tmp=$(mktemp -d)
cp -R dist/. "$tmp"/
touch "$tmp/.nojekyll"
git -C "$tmp" init -q -b gh-pages
git -C "$tmp" add -A
git -C "$tmp" commit -q -m "Deploy $(date -u +%Y-%m-%dT%H:%MZ) from $(git rev-parse --short HEAD)"
git -C "$tmp" push -f -q "$remote" gh-pages
rm -rf "$tmp"
echo "pushed dist/ to gh-pages"
