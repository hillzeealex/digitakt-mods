#!/bin/bash
# Construit l'OS Digitakt II « All-in-One » (Plaits + DX7 + Musical WAVE + Zoom) sur Mac ou Linux,
# à partir de TON OS 1.17 officiel. L'outil de l'auteur ne tourne que sous Windows : ce script prend
# sa release, recompile ses deux outils natifs depuis la source fournie et lance son propre builder.
#   tools/build-plaits.sh Digitakt_II_OS1.17.syx [out/DT2_All-in-One_v0.3.0-beta_OS1.17.syx]
# Il faut : cargo (https://rustup.rs), uv, un compilateur C. La sortie doit être identique à la
# release (sha256 426dd1be…) : le builder de l'auteur refuse d'écrire autre chose.
set -euo pipefail
[ $# -ge 1 ] || { sed -n '2,7p' "$0"; exit 2; }
for t in cargo uv cc; do command -v $t >/dev/null || { echo "il manque $t (voir l'en-tête du script)"; exit 1; }; done
root=$(cd "$(dirname "$0")/.." && pwd)
stock=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
out=${2:-$root/out/DT2_All-in-One_v0.3.0-beta_OS1.17.syx}
mkdir -p "$(dirname "$out")" && out=$(cd "$(dirname "$out")" && pwd)/$(basename "$out")
c=$root/.cache/plaits && mkdir -p "$c"

zip=DT2-All-in-One-v0.3.0-beta-Windows-r2.zip
[ -f "$c/$zip" ] || curl -fsSL -o "$c/$zip" "https://github.com/karigardarsson/digitakt-ii-research/releases/download/v0.3.0-beta/$zip"
echo "b9759287b746407e35f1c26afa6783c166717c5b3f5c39e7d2e7359534b31b4e  $c/$zip" | shasum -a 256 -c -s \
  || { echo "le zip téléchargé n'est pas celui de la release r2"; rm -f "$c/$zip"; exit 1; }
rm -rf "$c/win" "$c/src" "$c/build" && mkdir -p "$c/build"
unzip -q "$c/$zip" -d "$c/win" && win=$c/win/DT2-All-in-One-v0.3.0-beta
unzip -q "$win/DT2-All-in-One-Corresponding-Source-r2.zip" -d "$c/src"

echo "Compilation des outils natifs…"
(cd "$c/src/digikit" && cargo build -q --locked --release -p patchkit --bin patchkit)
make -s -C "$c/src/elektron-firmware-tool" >/dev/null

# Les 201 ressources du builder (modules Plaits, interface, Déjà Vu…) sont dans l'exécutable Windows.
cp "$c/src/builder/"*.py "$c/build/"
uv run -q --no-project --with pyinstaller==6.16.0 python -I - "$win/DT2-All-in-One-Builder.exe" "$c/build" <<'EOF'
import hashlib, json, pathlib, sys
from PyInstaller.archive.readers import CArchiveReader
exe, out = sys.argv[1], pathlib.Path(sys.argv[2]).resolve()
a = CArchiveReader(exe)
for name in a.toc:
    rel = name.replace('\\', '/')
    if rel.startswith('resources/'):
        dest = (out / rel).resolve()
        assert out in dest.parents, name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(a.extract(name))
inv = json.loads((out / 'resources/inventory.json').read_text())
bad = [n for n, d in inv['files'].items() if hashlib.sha256((out / 'resources' / n).read_bytes()).hexdigest() != d]
sys.exit('ressources non conformes : %s' % bad if bad else 0)
EOF

# Les outils Windows sont remplacés par ceux compilés ici ; l'inventaire est mis à jour pour eux seuls.
python3 -I - "$c" <<'EOF'
import hashlib, json, pathlib, shutil, sys
c = pathlib.Path(sys.argv[1]); r = c / 'build/resources'
inv = json.loads((r / 'inventory.json').read_text())
for name, src in {'native/patchkit.exe': 'src/digikit/target/release/patchkit',
                  'native/elektron-firmware-tool.exe': 'src/elektron-firmware-tool/elektron-firmware-tool'}.items():
    shutil.copy2(c / src, r / name)
    inv['files'][name] = hashlib.sha256((r / name).read_bytes()).hexdigest()
(r / 'inventory.json').write_text(json.dumps(inv, indent=1))
EOF

echo "Construction…"
rm -f "$out"
cd "$c/build" && python3 - "$stock" "$out" <<'EOF'
import sys
import builder_core as old, all_in_one as aio
extract = old._extract_all
def extract_unix(tool, syx, out):
    # Hors Windows, l'outil garde le « ? » de section_8_?.bin que Windows écrit « _ ».
    try:
        return extract(tool, syx, out)
    except old.BuildError:
        for p in out.iterdir():
            p.rename(p.with_name(p.name.replace('?', '_')))
        files = {p.name: p for p in out.iterdir() if p.is_file()}
        if set(files) != old.EXPECTED_SECTION_FILES:
            raise
        return files
old._extract_all = extract_unix
try:
    r = aio.build_firmware(sys.argv[1], sys.argv[2], progress=print)
except old.BuildError as e:
    sys.exit('ÉCHEC : %s' % e)
print('OK', r['path'], r['sha256'])
EOF
