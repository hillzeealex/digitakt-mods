#!/usr/bin/env python3
"""Dessine la façade de la Digitakt mk1 (docs/img/digitakt.svg) et l'insère dans l'étape 4 de docs/img/flow.svg.

Positions relevées sur le schéma « 3.1 Front panel » du manuel Elektron (OS 1.54), en pixels à 220 dpi.
Sans logo de marque. L'écran montre le menu MACHINE avec les machines des mods.

    python3 tools/digitakt_svg.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1106, 910
BODY, KEY, KEY_HI, KNOB = '#2b2b2d', '#3d3d41', '#505055', '#151516'
LABEL, SECOND, OLED, RED, ORANGE = '#ececec', '#9b9b9b', '#ffe23a', '#ff3b30', '#ff9f0a'


def text(x, y, s, size=13, fill=LABEL, weight=700, anchor='middle', family='Helvetica, Arial, sans-serif'):
    s = s.replace('&', '&amp;')
    return ('<text x="%g" y="%g" font-size="%g" fill="%s" font-weight="%d" text-anchor="%s" font-family="%s">%s</text>'
            % (x, y, size, fill, weight, anchor, family, s))


def key(x0, y0, x1, y1, fill=KEY):
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="10" fill="%s"/>'
            '<rect x="%g" y="%g" width="%g" height="%g" rx="9" fill="none" stroke="%s" stroke-width="2"/>'
            % (x0, y0, x1 - x0, y1 - y0, fill, x0 + 1, y0 + 1, x1 - x0 - 2, y1 - y0 - 2, KEY_HI))


def knob(cx, cy, r=34):
    return ('<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="#4a4a4e" stroke-width="3"/>'
            '<circle cx="%g" cy="%g" r="%g" fill="#202022"/>'
            '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
            % (cx, cy, r, KNOB, cx, cy, r - 9, cx, cy - r + 6, cx, cy - r + 18, LABEL))


def screen():
    # écran 128x64 : x 205-510, y 150-310 ; contenu inspiré du menu MACHINE
    o = ['<rect x="170" y="114" width="378" height="262" rx="4" fill="none" stroke="#56565a" stroke-width="2"/>',
         text(202, 132, '8 Voice Digital Drum Computer & Sampler', 13, LABEL, 700, 'start'),
         '<rect x="200" y="146" width="315" height="168" rx="3" fill="#050505"/>',
         '<rect x="208" y="154" width="44" height="22" fill="%s"/>' % OLED,
         '<rect x="257" y="154" width="250" height="22" fill="%s"/>' % OLED]
    mono = 'ui-monospace, Menlo, Consolas, monospace'
    o += [text(230, 171, 'A05', 15, '#050505', 800, 'middle', mono),
          text(265, 171, 'MACHINE', 15, '#050505', 800, 'start', mono),
          '<rect x="208" y="184" width="40" height="44" fill="none" stroke="%s" stroke-width="2.5"/>' % OLED,
          text(228, 200, 'SMP', 12, OLED, 800, 'middle', mono), text(228, 222, '2', 18, OLED, 800, 'middle', mono)]
    for i, (h) in enumerate([6, 14, 22, 12, 28, 18, 30, 16, 24, 10, 20, 8]):  # forme d'onde
        o.append('<rect x="%d" y="%d" width="4" height="%d" fill="%s"/>' % (258 + i * 7, 215 - h // 2, h, OLED))
    for j, name in enumerate(['DIGISLICER', 'POLY', 'STRING', 'MONO SAW']):
        y = 200 + j * 28
        if name == 'STRING':
            o.append('<rect x="352" y="%d" width="152" height="24" fill="none" stroke="%s" stroke-width="2.5"/>' % (y - 18, OLED))
        o.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (340 - 6, y - 12, OLED))
        o.append(text(358, y, name, 15, OLED, 800, 'start', mono))
    o.append(text(202, 359, 'Digitakt', 31, LABEL, 800, 'start'))
    return o


def icon(kind, cx, cy):
    s = 'stroke="%s" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"' % LABEL
    if kind == 'dots':
        return ''.join('<circle cx="%g" cy="%g" r="3.2" fill="%s"/>' % (cx + dx, cy, LABEL) for dx in (-9, 0, 9))
    if kind == 'gear':
        return ('<circle cx="%g" cy="%g" r="6" %s/><circle cx="%g" cy="%g" r="11" %s stroke-dasharray="4 3.2"/>'
                % (cx, cy, s, cx, cy, s))
    if kind == 'wave':
        return ''.join('<line x1="%g" y1="%g" x2="%g" y2="%g" %s/>' % (cx + dx, cy - h, cx + dx, cy + h, s)
                       for dx, h in ((-10, 4), (-5, 9), (0, 12), (5, 8), (10, 4)))
    if kind == 'tempo':
        return '<path d="M%g %gl8-20h4l8 20z M%g %gl14-14" %s/>' % (cx - 10, cy + 10, cx, cy + 4, s)
    if kind == 'rec':
        return '<circle cx="%g" cy="%g" r="9" %s/>' % (cx, cy, s)
    if kind == 'play':
        return '<path d="M%g %gv20l16-10z" %s/>' % (cx - 7, cy - 10, s)
    if kind == 'stop':
        return '<rect x="%g" y="%g" width="18" height="18" rx="3" %s/>' % (cx - 9, cy - 9, s)
    if kind in ('up', 'down', 'left', 'right'):
        d = {'up': 'M%g %gl12-12l12 12' % (cx - 12, cy + 6), 'down': 'M%g %gl12 12l12-12' % (cx - 12, cy - 6),
             'left': 'M%g %gl-12 12l12 12' % (cx + 6, cy - 12), 'right': 'M%g %gl12 12l-12 12' % (cx - 6, cy - 12)}[kind]
        return '<path d="%s" %s/>' % (d, s)
    raise ValueError(kind)


def panel():
    o = ['<rect width="%d" height="%d" rx="22" fill="%s"/>' % (W, H, BODY)]
    # connecteurs (face arrière, repérés sur le dessus)
    for x, a, b in ((137, 'Left', ''), (210, 'Right', ''), (287, 'Input L', ''), (363, 'Input R', ''),
                    (461, 'MIDI In', ''), (565, 'MIDI Out', 'Sync A'), (668, 'MIDI Thru', 'Sync B'),
                    (782, 'USB', ''), (880, 'DC In', ''), (994, 'Power', '')):
        o.append(text(x, 22, a, 12, SECOND))
        if b:
            o.append(text(x, 39, b, 12, SECOND))
    o.append('<path d="M66 26v-6a9 9 0 0 1 18 0v6" stroke="%s" stroke-width="2.5" fill="none"/>' % SECOND)
    o += screen()
    o += [knob(88, 166), text(88, 222, 'Master Volume'), knob(88, 297), text(88, 351, 'Level/Data'),
          text(88, 369, 'Sound Browser', 13, SECOND)]
    for y0, name, sub in ((440, 'FUNC', ''), (523, 'TRK', 'Chromatic'), (672, 'PTN', 'Metronome'), (789, 'BANK', 'Mute Mode')):
        o += [key(55, y0, 145, y0 + 52), text(100, y0 + 31, name, 13)]
        if sub:
            o.append(text(100, y0 + 68, sub, 13, SECOND))
    o.append('<circle cx="100" cy="611" r="7" fill="#1a1a1a" stroke="#56565a" stroke-width="2"/>')
    for cx, ic, sub in ((229, 'dots', 'Imp/Exp'), (312, 'gear', 'Save Proj'), (395, 'wave', 'Direct'), (478, 'tempo', 'Tap Tempo')):
        o += [key(cx - 29, 440, cx + 29, 493), icon(ic, cx, 466), text(cx, 509, sub, 13, SECOND)]
    for cx, ic, sub in ((245, 'rec', 'Copy'), (353, 'play', 'Clear'), (462, 'stop', 'Paste')):
        o += [key(cx - 45, 520, cx + 45, 574), icon(ic, cx, 547), text(cx, 591, sub, 13, SECOND)]
    for j, row in enumerate(('ABCD', 'EFGH')):
        for i, letter in enumerate(row):
            cx, cy = 630 + i * 128.3, 168 + j * 129
            o += [knob(cx, cy), text(cx, cy + 56, letter, 13)]
    for i, (name, sub) in enumerate((('TRIG', 'Quantize'), ('SRC', 'Assign'), ('FLTR', 'Delay'), ('AMP', 'Reverb'), ('LFO', 'Master'))):
        cx = 627 + i * 98
        o += [key(cx - 31, 385, cx + 31, 436, '#8a5a1c' if name == 'SRC' else KEY),  # SRC allumée : page active
              text(cx, 416, name, 13, ORANGE if name == 'SRC' else LABEL), text(cx, 455, sub, 13, SECOND)]
    o += [key(598, 480, 656, 532), text(627, 511, 'YES'), text(627, 550, 'Save Ptn', 13, SECOND),
          key(598, 562, 656, 614), text(627, 593, 'NO'), text(627, 633, 'Reload Ptn', 13, SECOND)]
    for cx, cy, ic, sub in ((793, 507, 'up', 'Rtrg/Oct+'), (710, 588, 'left', 'µTime -'), (793, 588, 'down', 'Rtrg/Oct -'),
                            (876, 588, 'right', 'µTime +')):
        o += [key(cx - 29, cy - 26, cx + 29, cy + 26), icon(ic, cx, cy), text(cx, cy + 45, sub, 13, SECOND)]
    for i, lab in enumerate(('1:4', '2:4', '3:4', '4:4')):
        x = 957 + i * 31
        o += [text(x, 513, lab, 12), '<circle cx="%g" cy="531" r="8" fill="%s"/>' % (x, RED if i == 0 else '#1a1a1a')]
    o += [key(960, 562, 1050, 614), text(1005, 593, 'PAGE'), text(1005, 633, 'Fill/Scale', 13, SECOND)]
    o.append('<rect x="196" y="653" width="858" height="212" rx="12" fill="#232325"/>')
    names = (('KICK', 'SNARE', 'TOM', 'CLAP', 'COWBELL', 'CLOSED HAT', 'OPEN HAT', 'CYMBAL'),
             ('MIDI A', 'MIDI B', 'MIDI C', 'MIDI D', 'MIDI E', 'MIDI F', 'MIDI G', 'MIDI H'))
    for j in range(2):
        y0 = 658 + j * 114
        for i in range(8):
            x0, n = 201 + i * 108.4, 1 + i + 8 * j
            lit = n in (1, 5, 9, 13)  # un trig sur chaque temps
            o.append(key(x0, y0, x0 + 89, y0 + 86, '#6b2420' if lit else KEY))
            o.append(text(x0 + 44.5, y0 + 44, str(n), 24, '#ffd0cc' if lit else LABEL, 500))
            o.append('<rect x="%g" y="%g" width="26" height="3" fill="%s"/>' % (x0 + 31.5, y0 + 55, LABEL))
            o.append(text(x0 + 44.5, y0 + 101, names[j][i], 12, SECOND))
    o += ['<path d="M1062 700h16v20M1062 820h16v-20" stroke="%s" stroke-width="2" fill="none" stroke-dasharray="3 3"/>' % SECOND,
          text(1080, 757, 'Quick', 12, SECOND, 700), text(1080, 773, 'Mute', 12, SECOND, 700)]
    return ''.join(o)


def main():
    body = panel()
    (ROOT / 'docs/img/digitakt.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img"><title>Digitakt (première génération), '
        'façade : écran sur le menu MACHINE avec les machines des mods</title>%s</svg>\n' % (W, H, body))
    flow = ROOT / 'docs/img/flow.svg'
    s = flow.read_text()
    a, b = s.index('<!-- 4 : la Digitakt -->'), s.index('<text class="t" x="800" y="200">')
    w = 180  # largeur dans la carte de 220, centrée, au-dessus du titre
    s = s[:a] + '<!-- 4 : la Digitakt -->\n<g transform="translate(%g 16) scale(%.4f)">%s</g>\n' % (780 + (220 - w) / 2, w / W, body) + s[b:]
    flow.write_text(s)
    print('écrit docs/img/digitakt.svg et l’étape 4 de docs/img/flow.svg')


if __name__ == '__main__':
    main()
