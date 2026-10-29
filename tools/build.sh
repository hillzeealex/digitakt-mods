#!/bin/bash
# Construit (ou vérifie) un OS à partir d'une recette et de TON OS stock.
#   tools/build.sh recipes/digitakt-mk1/graete-1.54.txt Digitakt_OS1.54.syx            # --check seulement
#   tools/build.sh recipes/digitakt-mk1/graete-1.54.txt Digitakt_OS1.54.syx out/os.syx # écrit l'OS
# VERSION=GR01 : ce que la machine affiche comme version (4 caractères). ELEKLOADER=chemin d'un clone existant.
set -euo pipefail
[ $# -ge 2 ] || { sed -n '2,5p' "$0"; exit 2; }
root=$(cd "$(dirname "$0")/.." && pwd)
recipe=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
stock=$(cd "$(dirname "$2")" && pwd)/$(basename "$2")
el=${ELEKLOADER:-$root/.cache/elekloader}
[ -d "$el/elekloader" ] || git clone -q --depth 1 https://github.com/elekloader/elekloader.git "$el"
args=()
while read -r f; do args+=(--mod "$root/$f"); done < <(grep -vE '^\s*(#|$)' "$recipe")
if [ $# -ge 3 ]; then
  out=$(mkdir -p "$(dirname "$3")" && cd "$(dirname "$3")" && pwd)/$(basename "$3")
  args+=(--out "$out" --version "${VERSION:-$(basename "$recipe" .txt | tr a-z A-Z | tr -cd A-Z0-9 | head -c 4)}")
else
  args+=(--check)
fi
cd "$el" && python3 -m elekloader.patch --stock "$stock" "${args[@]}"
