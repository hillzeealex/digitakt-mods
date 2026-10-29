#!/usr/bin/env python3
"""Télécharge les .elemod listés dans mods.json et vérifie leur sha256.

    python3 tools/sync.py            # télécharge ce qui manque ou a changé
    python3 tools/sync.py --verify   # vérifie seulement, hors ligne (CI)
"""
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check(root, manifest, download=False):
    """Renvoie la liste des problèmes (vide si tout est bon)."""
    problems = []
    root = root.resolve()
    for m in manifest['mods']:
        path = (root / m['path']).resolve()
        if root / 'elemods' not in path.parents:
            problems.append('%s: chemin hors de elemods/' % m['path'])
            continue
        if path.is_file() and sha256(path.read_bytes()) == m['sha256']:
            continue
        if not download:
            problems.append('%s: %s' % (m['path'], 'sha256 différent' if path.is_file() else 'absent'))
            continue
        data = urllib.request.urlopen(m['url'], timeout=60).read()
        if sha256(data) != m['sha256']:
            problems.append('%s: le fichier amont (%s) ne correspond pas au sha256 attendu' % (m['path'], m['url']))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        print('téléchargé', m['path'])
    return problems


def main(argv):
    manifest = json.loads((ROOT / 'mods.json').read_text())
    problems = check(ROOT, manifest, download='--verify' not in argv)
    for p in problems:
        print('PROBLÈME:', p)
    print('%d fichiers, %d problèmes' % (len(manifest['mods']), len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
