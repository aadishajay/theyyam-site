#!/usr/bin/env bash
# Build for theyyamtrips.com (site root) and upload dist/ to the Hostinger web folder over SSH.
#   scripts/deploy-hostinger.sh              keeps pages noindex
#   INDEXABLE=1 scripts/deploy-hostinger.sh  launch build: fails while placeholders remain
# rsync --delete makes the server folder match dist/ exactly, so only use it for this site's public_html.
set -euo pipefail
cd "$(dirname "$0")/.."
SITE=https://theyyamtrips.com BASE=/ npm run build
node scripts/check-placeholders.mjs
scripts/make-webp.sh
node scripts/picturefy.mjs
rsync -az --delete -e "ssh -p 65002 -o BatchMode=yes" dist/ u444028149@217.21.90.3:~/domains/theyyamtrips.com/public_html/
echo "uploaded dist/ to theyyamtrips.com"
