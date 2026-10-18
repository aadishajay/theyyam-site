#!/usr/bin/env python3
"""Hand-built vector illustrations of Theyyam faces for the homepage carousel.
Flat shapes, symmetric about x=200, drawn from reference photos (not auto-traced).
Run from the website folder: python3 tools/build_face_svgs.py  ->  assets/faces-svg/*.svg"""
import math, os

W, H = 400, 500
INK = '#1A0A08'; SILVER = '#EDEBE4'; SILVER_D = '#B9B6AE'; GOLD = '#F2B93B'; CREAM = '#F6EEDD'

def svg(body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" role="img">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')

def sym(inner):
    """draw `inner` (left half, x<200) and its mirror image"""
    return f'<g>{inner}</g><g transform="translate(400 0) scale(-1 1)">{inner}</g>'

def pt(cx, cy, r, deg):
    a = math.radians(deg); return cx + r*math.cos(a), cy + r*math.sin(a)

def radial_lines(cx, cy, r0, r1, a0, a1, step, **attrs):
    at = ' '.join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    out = ''
    a = a0
    while a <= a1 + 1e-6:
        x0, y0 = pt(cx, cy, r0, a); x1, y1 = pt(cx, cy, r1, a)
        out += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" {at}/>'
        a += step
    return out

def radial_petals(cx, cy, r, a0, a1, step, rx, ry, fill, stroke='none', sw=0):
    out = ''
    a = a0
    while a <= a1 + 1e-6:
        x, y = pt(cx, cy, r, a)
        out += (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
                f'transform="rotate({a+90:.1f} {x:.1f} {y:.1f})"/>')
        a += step
    return out

def radial_teeth(cx, cy, r0, r1, a0, a1, step, half, fill, stroke, sw=1):
    out = ''
    a = a0
    while a <= a1 + 1e-6:
        xa, ya = pt(cx, cy, r0, a - half); xb, yb = pt(cx, cy, r0, a + half); xt, yt = pt(cx, cy, r1, a)
        out += f'<path d="M{xa:.1f} {ya:.1f} L{xt:.1f} {yt:.1f} L{xb:.1f} {yb:.1f}Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
        a += step
    return out

def dots_on_circle(cx, cy, r, a0, a1, step, rad, fill):
    out = ''; a = a0
    while a <= a1 + 1e-6:
        x, y = pt(cx, cy, r, a); out += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{fill}"/>'; a += step
    return out

# ---------------------------------------------------------------- Vishnumoorthi
def vishnumoorthi():
    O = '#D9501A'; O2 = '#E98B54'; D = '#8A2D0E'
    b = '<circle cx="200" cy="250" r="190" fill="#5A1A17"/><circle cx="200" cy="250" r="150" fill="#6A2220"/>'
    # neck and shoulders
    b += '<path d="M158 400 C158 436 150 452 118 462 C80 474 52 486 36 500 L364 500 C348 486 320 474 282 462 C250 452 242 436 242 400Z" fill="#A83B16"/><path d="M158 440 C176 452 224 452 242 440" fill="none" stroke="#7E2C10" stroke-width="2.4" stroke-linecap="round"/>'
    # hair
    b += '<path d="M112 320 C84 190 112 84 200 78 C288 84 316 190 288 320 L288 350 L112 350Z" fill="#120C0B"/>'
    b += '<path d="M126 160 C150 116 250 116 274 160" fill="none" stroke="#2B2220" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M116 200 C136 140 264 140 284 200" fill="none" stroke="#2B2220" stroke-width="2.5" stroke-linecap="round"/>'
    # ears
    b += sym(f'<ellipse cx="119" cy="268" rx="13" ry="27" fill="{O}"/><path d="M117 252 C124 262 124 274 117 284" fill="none" stroke="{D}" stroke-width="2" stroke-linecap="round"/>')
    # face
    b += f'<path d="M122 218 C122 152 160 124 200 124 C240 124 278 152 278 218 L278 288 C278 352 240 406 200 420 C160 406 122 352 122 288Z" fill="{O}"/>'
    b += f'<path d="M134 214 C134 160 166 136 200 136 C234 136 266 160 266 214" fill="none" stroke="{D}" stroke-width="1.6"/>'
    b += f'<path d="M142 212 C142 168 170 146 200 146 C230 146 258 168 258 212" fill="none" stroke="{D}" stroke-width="1.2" stroke-dasharray="3 4" stroke-linecap="round"/>'
    # eye bands (black) with light eye
    eye = (f'<path d="M126 238 C126 204 162 196 197 214 L197 264 C166 272 130 266 126 238Z" fill="{INK}"/>'
           f'<path d="M146 240 C158 228 178 228 190 240 C178 252 158 252 146 240Z" fill="{CREAM}"/>'
           '<circle cx="168" cy="240" r="8" fill="#3A2216"/><circle cx="168" cy="240" r="3.6" fill="#000"/><circle cx="165.5" cy="237.5" r="1.6" fill="#fff"/>'
           + ''.join(f'<circle cx="{132+i*9}" cy="{262-abs(i-2)*0-(i*0)}" r="1.9" fill="{O}"/>' for i in range(0, 0)))
    b += sym(eye)
    # dotted rim under the eye bands
    b += sym(f'<path d="M128 252 C140 268 164 272 190 264" fill="none" stroke="{O2}" stroke-width="2.6" stroke-dasharray="0 5.5" stroke-linecap="round"/>')
    # brows
    b += sym(f'<path d="M128 200 C150 182 178 180 194 190" fill="none" stroke="{D}" stroke-width="3" stroke-linecap="round"/>'
             f'<path d="M132 190 C152 172 180 170 196 180" fill="none" stroke="{D}" stroke-width="1.6" stroke-dasharray="1 5" stroke-linecap="round"/>')
    # forehead medallion: green petals + sun
    pet = ''.join(f'<ellipse cx="200" cy="146" rx="5.5" ry="11" fill="#86A06F" transform="rotate({a} 200 168)"/>' for a in range(0, 360, 45))
    b += f'<circle cx="200" cy="168" r="27" fill="{O}" stroke="{D}" stroke-width="1.5"/>' + pet
    b += f'<circle cx="200" cy="168" r="14" fill="{O2}" stroke="{D}" stroke-width="1.6"/><circle cx="200" cy="168" r="6" fill="{D}"/><circle cx="200" cy="168" r="2.4" fill="{O2}"/>'
    b += ''.join(f'<line x1="200" y1="168" x2="{200+math.cos(math.radians(a))*13:.1f}" y2="{168+math.sin(math.radians(a))*13:.1f}" stroke="{D}" stroke-width="1.4"/>' for a in range(0, 360, 30))
    # nose
    b += (f'<path d="M200 226 L200 280" stroke="{D}" stroke-width="2" stroke-linecap="round" opacity=".55"/>'
          f'<path d="M200 284 C186 284 178 294 184 304 C192 312 208 312 216 304 C222 294 214 284 200 284Z" fill="none" stroke="{D}" stroke-width="2.4" stroke-linejoin="round"/>'
          f'<ellipse cx="191" cy="302" rx="3.4" ry="2.4" fill="{D}"/><ellipse cx="209" cy="302" rx="3.4" ry="2.4" fill="{D}"/>')
    # cheek scallops
    b += sym(''.join(f'<ellipse cx="{150+i*20}" cy="{300+i*3}" rx="11" ry="6.5" fill="{O2}" stroke="{D}" stroke-width="1.2"/>' for i in range(3)))
    # mouth
    b += ('<path d="M168 340 C182 330 194 331 200 335 C206 331 218 330 232 340 C222 358 178 358 168 340Z" fill="#5A2523"/>'
          f'<path d="M170 342 C188 347 212 347 230 342" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
          f'<path d="M184 336 L216 336" stroke="{CREAM}" stroke-width="3" stroke-linecap="round" opacity=".7"/>')
    # jaw dots
    b += f'<path d="M130 306 C132 360 168 406 200 416 C232 406 268 360 270 306" fill="none" stroke="{INK}" stroke-width="3.6" stroke-dasharray="0 8" stroke-linecap="round"/>'
    return svg(b, '#4A0E12')

# ---------------------------------------------------------------- Gulikan
def gulikan():
    RED = '#A8140F'; FR = '#C71E15'
    outline = ('M200 50 C186 50 176 64 170 82 C148 88 124 96 106 118 C82 148 86 192 98 234 '
               'C110 272 94 304 104 346 C116 396 156 440 200 472 L200 50Z')
    b = ''
    # wooden slats behind
    for i in range(0, 6):
        y = 20 + i*86
        b += sym(f'<rect x="-4" y="{y}" width="62" height="64" rx="6" fill="#D5E08D"/><circle cx="30" cy="{y+32}" r="7" fill="#4A0E12"/>')
    b += f'<path d="{outline}" transform="translate(0 0)" fill="{FR}" stroke="{FR}" stroke-width="20" stroke-linejoin="round"/>'.replace('L200 50Z', 'L200 472 L200 50Z')
    b += f'<g transform="translate(400 0) scale(-1 1)"><path d="{outline}" fill="{FR}" stroke="{FR}" stroke-width="20" stroke-linejoin="round"/></g>'
    # fringe texture dots
    b += sym(''.join(f'<circle cx="{pt(200,262,206-0,180+i*5.5)[0]:.1f}" cy="{pt(200,262,206,180+i*5.5)[1]:.1f}" r="0" />' for i in range(0)))
    # mask face
    b += f'<g transform="translate(200 262) scale(.93) translate(-200 -262)">' + sym(f'<path d="{outline}" fill="{RED}"/>') + '</g>'
    b += f'<g transform="translate(200 262) scale(.86) translate(-200 -262)">' + sym(f'<path d="{outline}" fill="none" stroke="{SILVER}" stroke-width="2.4" stroke-dasharray="1 7" stroke-linecap="round"/>') + '</g>'
    # silver diadem + cobra mark
    b += (f'<path d="M154 108 C160 70 240 70 246 108 C232 96 168 96 154 108Z" fill="{SILVER}" stroke="{SILVER_D}" stroke-width="2"/>'
          f'<ellipse cx="200" cy="90" rx="13" ry="16" fill="{GOLD}" stroke="{INK}" stroke-width="2"/><ellipse cx="200" cy="92" rx="4" ry="5" fill="{INK}"/>')
    b += dots_on_circle(200, 120, 56, 205, 335, 14, 3.2, SILVER)
    # forehead stem
    b += (f'<path d="M200 118 C214 138 212 162 200 186 C188 162 186 138 200 118Z" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>'
          f'<path d="M200 130 C206 146 206 160 200 174 C194 160 194 146 200 130Z" fill="{RED}"/>')
    # eyes: concentric
    def eye(cx, cy):
        s = f'<g transform="rotate(-8 {cx} {cy})">'
        for rx, ry, f in [(44, 52, CREAM), (40, 48, INK), (35, 43, CREAM), (27, 35, INK), (22, 29, CREAM), (14, 20, INK)]:
            s += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}"/>'
        s += f'<ellipse cx="{cx-4}" cy="{cy-6}" rx="3.6" ry="5" fill="{CREAM}"/></g>'
        return s
    b += eye(144, 236) + f'<g transform="translate(400 0) scale(-1 1)">{eye(144,236)}</g>'
    # nose
    b += (f'<path d="M200 186 C184 206 182 232 188 250 C172 268 174 294 196 306 L204 306 C226 294 228 268 212 250 C218 232 216 206 200 186Z" fill="{RED}" stroke="{CREAM}" stroke-width="3.4" stroke-linejoin="round"/>'
          f'<path d="M200 200 C194 222 194 240 200 252 C206 240 206 222 200 200Z" fill="none" stroke="{CREAM}" stroke-width="2"/>'
          f'<ellipse cx="188" cy="290" rx="6" ry="9" fill="{INK}" transform="rotate(14 188 290)"/><ellipse cx="212" cy="290" rx="6" ry="9" fill="{INK}" transform="rotate(-14 212 290)"/>')
    # mouth: white grimace with tusks
    mouth_half = 'M200 322 C168 312 134 326 118 350 C106 370 118 392 140 396 C146 384 158 376 174 376 C186 378 194 388 200 400'
    b += sym(f'<path d="{mouth_half} L200 322Z" fill="{CREAM}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    b += f'<path d="M158 352 C176 344 190 350 200 362 C210 350 224 344 242 352 C236 380 214 388 200 392 C186 388 164 380 158 352Z" fill="{INK}"/>'
    b += ''.join(f'<path d="M{x} 366 L{x+4} 384 L{x+8} 366Z" fill="{CREAM}"/>' for x in range(178, 224, 9))
    b += sym(f'<circle cx="146" cy="358" r="9" fill="{GOLD}" stroke="{INK}" stroke-width="2"/><circle cx="146" cy="358" r="3" fill="{INK}"/>')
    # chin lines
    b += sym(f'<path d="M200 410 C184 416 170 428 166 444" fill="none" stroke="{CREAM}" stroke-width="2.6" stroke-linecap="round"/>')
    b += sym(dots_on_circle(200, 262, 202, 150, 166, 8, 3, SILVER).replace('', ''))
    return svg(b, '#4A0E12')

# ---------------------------------------------------------------- Muchilot Bhagavathi
def muchilot():
    R1 = '#B5160F'; R2 = '#8F1410'; R3 = '#D42A1E'; O = '#E2531F'; D = '#9A2F0C'
    b = '<circle cx="200" cy="215" r="190" fill="#7A100D"/>'
    b += f'<circle cx="200" cy="215" r="176" fill="{R1}"/>' + radial_lines(200, 215, 150, 176, 180, 360, 6, stroke='#E9534A', stroke_width='3', stroke_linecap='round')
    b += f'<circle cx="200" cy="215" r="144" fill="{R3}"/><circle cx="200" cy="215" r="128" fill="{R2}"/>'
    b += dots_on_circle(200, 215, 136, 188, 352, 11, 2.8, SILVER)
    # shoulder discs
    for i, (rx, ry, f) in enumerate([(170, 62, R2), (146, 50, R3), (122, 40, R1), (98, 30, R2)]):
        b += f'<ellipse cx="200" cy="{478-i*4}" rx="{rx}" ry="{ry}" fill="{f}"/>'
    b += ''.join(f'<ellipse cx="200" cy="{478-i*4}" rx="{rx-5}" ry="{ry-5}" fill="none" stroke="{SILVER}" stroke-width="2" stroke-dasharray="1 7" stroke-linecap="round"/>' for i,(rx,ry) in enumerate([(170,62),(146,50),(122,40)]))
    # crown: silver fringe
    b += f'<path d="M104 214 C104 120 296 120 296 214 L276 214 C276 148 124 148 124 214Z" fill="{R2}"/>'
    b += radial_lines(200, 205, 58, 98, 192, 348, 5.4, stroke=SILVER, stroke_width='5', stroke_linecap='round')
    b += f'<path d="M108 205 A92 92 0 0 1 292 205" fill="none" stroke="{SILVER}" stroke-width="9"/><path d="M104 205 A96 96 0 0 1 296 205" fill="none" stroke="{SILVER_D}" stroke-width="2"/>'
    b += f'<path d="M142 205 A58 58 0 0 1 258 205" fill="none" stroke="{SILVER}" stroke-width="7"/><path d="M142 205 A58 58 0 0 1 258 205" fill="none" stroke="{SILVER_D}" stroke-width="1.6"/>'
    # forehead band
    b += f'<path d="M142 206 C142 168 258 168 258 206 L258 214 C230 196 170 196 142 214Z" fill="{R1}"/>'
    # face
    b += f'<path d="M140 214 C140 176 166 160 200 160 C234 160 260 176 260 214 L260 266 C260 318 232 354 200 362 C168 354 140 318 140 266Z" fill="{O}"/>'
    b += f'<path d="M152 262 C158 318 180 346 200 352 C220 346 242 318 248 262" fill="none" stroke="{D}" stroke-width="1.6" stroke-dasharray="3 4" stroke-linecap="round"/>'
    # eyes
    b += sym(f'<path d="M144 222 C156 208 182 208 196 218 L196 238 C182 246 156 246 144 236Z" fill="{INK}"/>'
             f'<path d="M158 228 C166 222 182 222 190 228 C182 236 166 236 158 228Z" fill="{CREAM}"/><circle cx="174" cy="229" r="4.6" fill="{INK}"/>'
             f'<path d="M146 204 C162 192 184 194 196 204" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    # nose, mouth
    b += (f'<path d="M200 222 C192 246 188 266 190 276 C196 282 204 282 210 276 C212 266 208 246 200 222Z" fill="none" stroke="{D}" stroke-width="2.6" stroke-linejoin="round"/>'
          f'<ellipse cx="193" cy="276" rx="3" ry="2" fill="{D}"/><ellipse cx="207" cy="276" rx="3" ry="2" fill="{D}"/>'
          '<path d="M182 304 C192 298 208 298 218 304 C212 318 188 318 182 304Z" fill="#6E2A24"/>')
    # white curled moustache
    b += sym(f'<path d="M197 298 C176 292 158 302 148 318 C144 326 152 330 160 326" fill="none" stroke="{SILVER}" stroke-width="6" stroke-linecap="round"/>'
             f'<path d="M197 298 C176 292 158 302 148 318" fill="none" stroke="{SILVER_D}" stroke-width="1.4"/>')
    # ear discs
    b += sym(f'<circle cx="124" cy="240" r="22" fill="{SILVER}" stroke="{SILVER_D}" stroke-width="3"/><circle cx="124" cy="240" r="13" fill="#D8D6CF"/><circle cx="124" cy="240" r="5" fill="{R1}"/>')
    # necklace
    b += f'<path d="M126 340 C150 392 250 392 274 340" fill="none" stroke="#E5B94E" stroke-width="5" stroke-dasharray="0 8" stroke-linecap="round"/>'
    return svg(b, '#4A0E12')

# ---------------------------------------------------------------- Kundora Chamundi
def kundora():
    R1 = '#D01E15'; R2 = '#E9382B'; R3 = '#9C120E'; O = '#E4552A'; D = '#9A2F0C'
    b = '<circle cx="200" cy="228" r="196" fill="#7A100D"/>'
    b += f'<circle cx="200" cy="228" r="186" fill="{R1}"/>'
    b += radial_petals(200, 228, 150, 190, 350, 13, 15, 38, R2, '#FFB2A5', 1.2)
    b += dots_on_circle(200, 228, 180, 192, 348, 13, 3.2, SILVER)
    b += f'<circle cx="200" cy="228" r="118" fill="{R3}"/>'
    # crown teeth
    b += radial_teeth(200, 205, 84, 118, 194, 346, 9.5, 5.2, SILVER, SILVER_D, 1)
    b += f'<path d="M116 205 A84 84 0 0 1 284 205" fill="none" stroke="{SILVER}" stroke-width="10"/><path d="M110 205 A90 90 0 0 1 290 205" fill="none" stroke="{SILVER_D}" stroke-width="1.6"/>'
    # crescent top
    b += f'<path d="M172 70 A28 28 0 0 0 228 70 A22 22 0 0 1 172 70Z" fill="{SILVER}" stroke="{SILVER_D}" stroke-width="2"/><circle cx="200" cy="62" r="5" fill="{GOLD}"/>'
    # side diamonds
    b += sym(f'<g transform="rotate(45 78 210)"><rect x="64" y="196" width="28" height="28" rx="3" fill="{INK}" stroke="{SILVER}" stroke-width="3"/></g>'
             f'<circle cx="104" cy="170" r="15" fill="#EFD7A8" stroke="{SILVER_D}" stroke-width="2.4"/><circle cx="104" cy="170" r="7" fill="{R1}"/>')
    # forehead band
    b += f'<path d="M140 208 C140 170 260 170 260 208 L260 214 C232 198 168 198 140 214Z" fill="{R1}"/>'
    # face
    b += f'<path d="M142 214 C142 178 168 162 200 162 C232 162 258 178 258 214 L258 266 C258 314 232 346 200 354 C168 346 142 314 142 266Z" fill="{O}"/>'
    # third eye crescent
    b += f'<path d="M188 188 A12 12 0 0 0 212 188 A8.5 8.5 0 0 1 188 188Z" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"/><circle cx="200" cy="198" r="3.4" fill="{R3}"/>'
    # eyes (round, open)
    b += sym(f'<path d="M146 226 C156 208 186 208 196 224 C186 242 156 242 146 226Z" fill="{INK}"/>'
             f'<ellipse cx="172" cy="226" rx="16" ry="10" fill="{CREAM}"/><circle cx="173" cy="226" r="7.4" fill="{INK}"/><circle cx="170.4" cy="223.6" r="2" fill="#fff"/>'
             f'<path d="M146 208 C162 192 186 194 198 206" fill="none" stroke="{INK}" stroke-width="5.4" stroke-linecap="round"/>')
    # nose / mouth
    b += (f'<path d="M200 230 C192 252 188 268 190 278 C196 284 204 284 210 278 C212 268 208 252 200 230Z" fill="none" stroke="{D}" stroke-width="2.6" stroke-linejoin="round"/>'
          f'<ellipse cx="193" cy="278" rx="3" ry="2" fill="{D}"/><ellipse cx="207" cy="278" rx="3" ry="2" fill="{D}"/>'
          '<path d="M180 306 C192 298 208 298 220 306 C212 326 188 326 180 306Z" fill="#3B0D0B"/><path d="M182 306 C194 311 206 311 218 306" fill="none" stroke="#7A1F1A" stroke-width="2"/>')
    b += f'<path d="M156 300 C160 336 184 350 200 352 C216 350 240 336 244 300" fill="none" stroke="{D}" stroke-width="1.6" stroke-dasharray="3 4" stroke-linecap="round"/>'
    # ear ornaments
    b += sym(f'<circle cx="132" cy="246" r="24" fill="#F1E6C8" stroke="{SILVER_D}" stroke-width="3"/><circle cx="132" cy="246" r="15" fill="{R1}" stroke="{SILVER}" stroke-width="2"/><circle cx="132" cy="246" r="6" fill="{GOLD}"/>')
    # chest ornament: concentric rings with a dotted rim
    b += (f'<circle cx="200" cy="506" r="96" fill="#C8501F" stroke="{SILVER}" stroke-width="8"/>'
          f'<circle cx="200" cy="506" r="78" fill="none" stroke="{SILVER}" stroke-width="2" stroke-dasharray="1 7" stroke-linecap="round"/>'
          f'<circle cx="200" cy="506" r="62" fill="#8E2A12"/><circle cx="200" cy="506" r="44" fill="none" stroke="#E4552A" stroke-width="3"/>'
          f'<circle cx="200" cy="506" r="26" fill="#C8501F" stroke="{GOLD}" stroke-width="3"/>')
    return svg(b, '#4A0E12')

if __name__ == '__main__':
    os.makedirs('assets/faces-svg', exist_ok=True)
    for name, fn in [('vishnumoorthi', vishnumoorthi), ('gulikan', gulikan), ('muchilot-bhagavathi', muchilot), ('kundora-chamundi', kundora)]:
        s = fn()
        open(f'assets/faces-svg/{name}.svg', 'w', encoding='utf-8').write(s)
        print(name, len(s)//1024, 'KB')
