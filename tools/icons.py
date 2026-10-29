#!/usr/bin/env python3
"""Génère docs/icons/<id>.svg : une icône pixel art 16x16 par mod, aux couleurs de l'écran de la machine.

    python3 tools/icons.py               # écrit les SVG (demande Pillow : pip install pillow)
    python3 tools/icons.py preview.png   # écrit aussi une planche agrandie pour les vérifier à l'œil

Ajouter un mod : une fonction de dessin dans ICONS, à son id (celui de mods.json).
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
N = 16
# Jaune OLED de la mk1, blanc de la Digitakt II.
COLORS = {'digitakt-mk1': ('#ffe23a', '#1b1808'), 'digitakt-ii': ('#f2f2f2', '#141414')}


def ascii_art(d, rows):
    assert len(rows) == N and all(len(r) == N for r in rows), rows
    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == '#':
                d.point((x, y), 1)


def chip(d):
    ascii_art(d, [
        '................',
        '....#.#..#.#....',
        '....#.#..#.#....',
        '...##########...',
        '.###........###.',
        '...#........#...',
        '.###.######.###.',
        '...#.#....#.#...',
        '...#.#....#.#...',
        '.###.######.###.',
        '...#........#...',
        '.###........###.',
        '...##########...',
        '....#.#..#.#....',
        '....#.#..#.#....',
        '................'])


def pages(d):
    ascii_art(d, [
        '................',
        '......########..',
        '......#......#..',
        '....########.#..',
        '....#......#.#..',
        '..########.#.#..',
        '..#......#.#.#..',
        '..#.####.#.#.#..',
        '..#......#.#.#..',
        '..#.###..#.#.#..',
        '..#......#.###..',
        '..#.####.#.#....',
        '..#......###....',
        '..#.##...#......',
        '..########......',
        '................'])


def slicer(d):
    for x, h in ((1, 2), (3, 5), (7, 6), (9, 3), (12, 4), (14, 1)):
        d.line((x, 8 - h, x, 7 + h), 1)
    for x in (5, 10):  # repères de slice, drapeau en haut
        d.line((x, 2, x, 15), 1)
        d.line((x, 0, x + 2, 1), 1)
        d.point((x, 1), 1)


def health(d):
    ascii_art(d, [
        '................',
        '................',
        '...###....###...',
        '..#####..#####..',
        '.##############.',
        '.##############.',
        '.##############.',
        '..############..',
        '...##########...',
        '....########....',
        '.....######.....',
        '......####......',
        '.......##.......',
        '................',
        '................',
        '................'])
    d.line([(0, 7), (4, 7), (6, 4), (9, 10), (11, 7), (15, 7)], 0)


def neighbor(d):
    d.rectangle((0, 3, 5, 12), outline=1)
    d.rectangle((10, 3, 15, 12), outline=1)
    for x in range(1, 5):  # l'audio de la piste voisine
        h = [2, 4, 3, 1][x - 1]
        d.line((x, 8 - h, x, 7 + h), 1)
    d.rectangle((6, 7, 8, 8), fill=1)
    d.line([(7, 5), (9, 7), (9, 8), (7, 10)], 1)


def bell(d):
    ascii_art(d, [
        '.......##.......',
        '......####......',
        '.....##..##.....',
        '.....#....#.....',
        '....##....##....',
        '....#......#....',
        '....#......#....',
        '...##......##...',
        '...#........#...',
        '..##........##..',
        '.##..........##.',
        '################',
        '................',
        '......####......',
        '.......##.......',
        '................'])


def sine(d, cycles=1, amp=5.5, y0=7.5):
    pts = [(x, round(y0 - amp * math.sin(2 * math.pi * cycles * x / (N - 1)))) for x in range(N)]
    d.line(pts, 1)


def macro(d):
    d.ellipse((1, 1, 14, 14), outline=1)
    for i in range(8):  # les 8 moteurs
        a = math.pi / 2 + i * math.pi / 4
        d.point((round(7.5 + 4.5 * math.cos(a)), round(7.5 - 4.5 * math.sin(a))), 1)
    d.rectangle((7, 7, 8, 8), fill=1)
    d.line((8, 7, 10, 5), 1)


def keyboard(d):
    d.rectangle((0, 4, 15, 14), outline=1)
    for x in (3, 6, 9, 12):
        d.line((x, 4, x, 14), 1)
    for x in (2, 5, 11):  # touches noires
        d.rectangle((x, 4, x + 2, 9), fill=1)


def chord(d):
    for y in (12, 8, 4):  # trois notes empilées : un accord
        d.ellipse((2, y, 6, y + 2), fill=1)
    d.line((6, 0, 6, 13), 1)
    d.line([(6, 0), (10, 2), (10, 5)], 1)


def matrix(d):
    on = {(0, 1), (1, 3), (2, 0), (3, 2), (2, 2)}
    for i in range(4):
        for j in range(4):
            x, y = 1 + 4 * i, 1 + 4 * j
            if (i, j) in on:
                d.rectangle((x - 1, y - 1, x + 1, y + 1), fill=1)
            else:
                d.point((x, y), 1)


def eq(d):
    pts = [(0, 9), (3, 4), (5, 7), (8, 11), (11, 6), (13, 8), (15, 8)]
    d.line(pts, 1)
    for x, y in pts[1:5]:  # les 4 bandes
        d.rectangle((x - 1, y - 1, x + 1, y + 1), outline=1)
    for x in range(0, N, 2):
        d.point((x, 14), 1)


def scope(d):
    d.rectangle((0, 1, 15, 14), outline=1)
    for x in range(2, 14, 2):
        d.point((x, 12), 1)
    d.line([(x, round(7 - 4 * math.sin(2 * math.pi * (x - 2) / 11))) for x in range(2, 14)], 1)


def rings(d):
    d.ellipse((0, 0, 15, 15), outline=1)
    d.ellipse((3, 3, 12, 12), outline=1)
    d.rectangle((6, 6, 9, 9), fill=1)


def filt(d):
    d.line([(0, 6), (6, 6), (8, 2), (9, 2), (10, 6), (12, 10), (15, 14)], 1)
    d.line([(0, 7), (6, 7)], 1)
    for x in range(0, N, 2):
        d.point((x, 15), 1)


def string(d, top=0):
    d.rectangle((0, 6 + top, 1, 9 + top), fill=1)
    d.rectangle((14, 6 + top, 15, 9 + top), fill=1)
    arc = [(x, round(7.5 + top - 4 * (1 - ((x - 7.5) / 6) ** 2))) for x in range(2, 14)]
    d.line(arc, 1)
    for x, y in arc[::2]:  # la vibration
        d.point((x, 2 * (7 + top) + 1 - y), 1)


def string_fast(d):
    string(d, top=-3)
    for ox in (4, 9):  # >>
        d.line([(ox, 10), (ox + 3, 12), (ox, 14)], 1)


def fm(d):
    for x, y in ((6, 0), (1, 6), (11, 6), (6, 12)):
        d.rectangle((x, y, x + 3, y + 3), outline=1)
    d.line([(6, 3), (3, 6)], 1)
    d.line([(9, 3), (12, 6)], 1)
    d.line([(3, 9), (6, 12)], 1)
    d.line([(12, 9), (9, 12)], 1)
    d.point((7, 1), 1)
    d.point((8, 2), 1)


def ob1(d):
    d.line([(0, 6), (0, 2), (4, 2), (4, 6), (8, 6), (8, 2), (12, 2), (12, 6), (15, 6)], 1)
    for x0 in (0, 8):
        d.line([(x0, 13), (x0 + 7, 9)], 1)
        d.line([(x0 + 7, 9), (x0 + 7, 13)], 1)


def events(d):
    d.line((0, 12, 15, 12), 1)
    for x, h in ((1, 3), (5, 6), (9, 2), (13, 8)):
        d.line((x, 12 - h, x, 12), 1)
        d.rectangle((x - 1, 11 - h, x + 1, 12 - h), fill=1)


def steps(d):
    pattern = ['#.#.', '.##.', '#..#', '####']
    for j, row in enumerate(pattern):
        for i, c in enumerate(row):
            box = (4 * i, 4 * j, 4 * i + 2, 4 * j + 2)
            d.rectangle(box, fill=1) if c == '#' else d.rectangle(box, outline=1)


def snake(d):
    d.line([(1, 2), (14, 2), (14, 7), (1, 7), (1, 12), (11, 12)], 1, width=2)
    d.rectangle((11, 11, 14, 14), fill=1)
    d.point((13, 12), 0)
    d.point((15, 13), 1)


def press(d):
    d.rounded_rectangle((1, 7, 14, 14), radius=2, outline=1)
    d.rectangle((4, 10, 11, 11), fill=1)
    d.line((7, 0, 7, 4), 1)
    d.line((8, 0, 8, 4), 1)
    d.line([(5, 3), (7, 5)], 1)
    d.line([(10, 3), (8, 5)], 1)


def faders(d):
    for x, y in ((2, 10), (6, 4), (9, 7), (13, 3)):
        for yy in range(1, 15, 2):
            d.point((x, yy), 1)
        d.rectangle((x - 1, y, x + 1, y + 1), fill=1)
    d.line((0, 15, 15, 15), 1)


def plaits(d):  # le gros bouton MODEL et ses modèles tout autour
    d.ellipse((4, 4, 11, 11), outline=1)
    d.line([(7, 8), (9, 6)], 1)
    d.line([(8, 8), (10, 6)], 1)
    for x, y in ((7, 0), (12, 2), (14, 7), (12, 12), (7, 14), (2, 12), (0, 7), (2, 2)):
        d.rectangle((x, y, x + 1, y + 1), fill=1)


ICONS = {
    'digitakt-mk1': {
        'core': chip, 'machine-pages': pages, 'digislicer': slicer, 'digihealth': health,
        'digineighbor': neighbor, 'digisophie': bell, 'digimono': sine, 'digimacro': macro,
        'digi101': keyboard, 'digipoly': chord, 'digimatrix': matrix, 'digieq': eq,
        'digiutils': scope, 'tonefx': rings, 'digifilter': filt, 'digistring': string,
        'digistring-fast': string_fast, 'dt-fm': fm, 'ob1': ob1, 'seq-events': events,
        'digiseq-dt': steps, 'digisnake-dt': snake,
    },
    'digitakt-ii': {'core': chip, 'perform-direct': press, 'perform-levels': faders, 'plaits': plaits},
}


def bitmap(fn):
    img = Image.new('1', (N, N), 0)
    fn(ImageDraw.Draw(img))
    return img


def svg(img, title, fg, bg):
    rects = []
    for y in range(N):
        x = 0
        while x < N:
            if img.getpixel((x, y)):
                x0 = x
                while x < N and img.getpixel((x, y)):
                    x += 1
                rects.append('<rect x="%d" y="%d" width="%d" height="1"/>' % (x0 + 2, y + 2, x - x0))
            x += 1
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="64" height="64" '
            'role="img" shape-rendering="crispEdges"><title>%s</title>'
            '<rect width="20" height="20" rx="3" fill="%s"/><g fill="%s">%s</g></svg>\n'
            % (title, bg, fg, ''.join(rects)))


def name(device, mod_id):
    return mod_id if device == 'digitakt-mk1' else '%s-dt2' % mod_id


BUTTONS = {  # nom : (titre, sous-titre, plein = téléchargement / contour = lien vers un site)
    'btn-os-dt': ('Télécharger l\'OS officiel', 'Digitakt · OS 1.54 · site Elektron', True),
    'btn-pack-dt': ('Télécharger le pack de mods', 'Digitakt · 8 mods · SLICER, POLY, STRING…', True),
    'btn-os-dt2': ('Télécharger l\'OS officiel', 'Digitakt II · OS 1.17 · site Elektron', True),
    'btn-pack-dt2': ('Télécharger le pack de mods', 'Digitakt II · PERFORM KIT', True),
    'btn-transfer': ('Installer Elektron Transfer', 'gratuit · Mac et Windows', False),
    'btn-elekloader': ('Ouvrir elekloader', 'le site qui fabrique ton OS', False),
}


def button(title, sub, filled):
    fg, bg = ('#1b1808', '#ffe23a') if filled else ('#ffe23a', '#1b1808')
    arrow = ('M34 22v26m-11-11 11 11 11-11M22 56h24' if filled else 'M24 38h22m-9-9 9 9-9 9')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 76" width="440" height="76" role="img">'
            '<title>%s, %s</title><rect x="1.5" y="1.5" width="437" height="73" rx="16" fill="%s" stroke="#ffe23a" stroke-width="3"/>'
            '<path d="%s" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            '<g font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif" fill="%s">'
            '<text x="70" y="34" font-size="22" font-weight="800">%s</text>'
            '<text x="70" y="58" font-size="15" font-weight="500">%s</text></g></svg>\n'
            % (title, sub, bg, arrow, fg, fg, title, sub))


def main(argv):
    for n, (title, sub, filled) in BUTTONS.items():
        (ROOT / 'docs' / 'img' / ('%s.svg' % n)).write_text(button(title, sub, filled))
    out = ROOT / 'docs' / 'icons'
    out.mkdir(parents=True, exist_ok=True)
    tiles = []
    for device, icons in ICONS.items():
        fg, bg = COLORS[device]
        for mod_id, fn in icons.items():
            img = bitmap(fn)
            (out / ('%s.svg' % name(device, mod_id))).write_text(svg(img, mod_id, fg, bg))
            tiles.append((name(device, mod_id), img, fg, bg))
    print('%d icônes dans %s' % (len(tiles), out.relative_to(ROOT)))
    if argv:  # planche de contrôle : 8 px par pixel, nom dessous
        s, cols = 8, 6
        sheet = Image.new('RGB', (cols * 160, -(-len(tiles) // cols) * 170), 'white')
        d = ImageDraw.Draw(sheet)
        for i, (n, img, fg, bg) in enumerate(tiles):
            ox, oy = (i % cols) * 160 + 16, (i // cols) * 170 + 8
            d.rectangle((ox, oy, ox + 18 * s, oy + 18 * s), fill=bg)
            for y in range(N):
                for x in range(N):
                    if img.getpixel((x, y)):
                        d.rectangle((ox + (x + 1) * s, oy + (y + 1) * s, ox + (x + 2) * s - 1, oy + (y + 2) * s - 1), fill=fg)
            d.text((ox, oy + 18 * s + 3), n, fill='black')
        sheet.save(argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])
