#!/usr/bin/env bash
# Write a .webp next to each .jpg/.png under dist/ (name.jpg -> name.jpg.webp); scripts/picturefy.mjs then points pages at them
# with <picture>. Keeps a file only if it is smaller. (Hostinger's CDN converts images on its own, but its files are often larger.)
set -euo pipefail
cd "$(dirname "$0")/../dist"
n=0; saved=0
while IFS= read -r -d '' f; do
  cwebp -quiet -q 76 -m 6 "$f" -o "$f.webp" 2>/dev/null || { rm -f "$f.webp"; continue; }
  a=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f"); b=$(stat -f%z "$f.webp" 2>/dev/null || stat -c%s "$f.webp")
  if [ "$b" -ge "$a" ]; then rm -f "$f.webp"; else n=$((n+1)); saved=$((saved + a - b)); fi
done < <(find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) -print0)
echo "webp: $n files, saved $((saved/1024)) KB"
