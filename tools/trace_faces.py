#!/usr/bin/env python3
"""Trace the Theyyam face photos (assets/faces/*.jpg) into clean colour SVGs (assets/faces-svg/*.svg).

Faithful trace, not an illustration: shadows are lifted and noise smoothed (OpenCV), then the photo is
vectorised with the VTracer CLI (spline mode, stacked layers). Run from the website folder.

Setup (once):
  cargo install vtracer                       # CLI; binary at ~/.cargo/bin/vtracer
  python3 -m venv .venv && .venv/bin/pip install opencv-python-headless numpy
Run:
  .venv/bin/python tools/trace_faces.py [slug ...]
"""
import os, re, subprocess, sys, tempfile
import cv2, numpy as np

SLUGS = ['vishnumoorthi', 'kundora-chamundi', 'gulikan', 'muchilot-bhagavathi', 'panjuruli']
VTRACER = os.environ.get('VTRACER', os.path.expanduser('~/.cargo/bin/vtracer'))
ARGS = ['--colormode', 'color', '--hierarchical', 'stacked', '--mode', 'spline', '--filter_speckle', '14',
        '--color_precision', '7', '--gradient_step', '22', '--corner_threshold', '60', '--segment_length', '8',
        '--splice_threshold', '45', '--path_precision', '1']

os.makedirs('assets/faces-svg', exist_ok=True)
for slug in (sys.argv[1:] or SLUGS):
    im = cv2.imread(f'assets/faces/{slug}.jpg')
    im = cv2.resize(im, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    im = cv2.bilateralFilter(im, 9, 35, 9)                                   # smooth noise, keep edges
    im = (np.power(im.astype(np.float32) / 255.0, 0.72) * 255).clip(0, 255).astype(np.uint8)  # lift shadows
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, 'in.png'); out = os.path.join(d, 'out.svg')
        cv2.imwrite(src, im)
        subprocess.run([VTRACER, '--input', src, '--output', out, *ARGS], check=True, capture_output=True)
        s = open(out, encoding='utf-8').read()
    w, h = re.search(r'width="(\d+)" height="(\d+)"', s).groups()
    s = re.sub(r'<\?xml[^>]*\?>\s*|<!--.*?-->\s*', '', s, flags=re.S)
    s = re.sub(r'<svg[^>]*>', f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img">', s, count=1)
    s = s.replace('\n', '').replace(' transform="translate(0,0)"', '')
    open(f'assets/faces-svg/{slug}.svg', 'w', encoding='utf-8').write(s)
    print(slug, len(s) // 1024, 'KB')
