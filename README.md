<p align="center">
<img src="docs/icons/digislicer.svg" width="48"> <img src="docs/icons/digipoly.svg" width="48"> <img src="docs/icons/digistring.svg" width="48"> <img src="docs/icons/dt-fm.svg" width="48"> <img src="docs/icons/digimono.svg" width="48"> <img src="docs/icons/digi101.svg" width="48"> <img src="docs/icons/digimacro.svg" width="48"> <img src="docs/icons/tonefx.svg" width="48"> <img src="docs/icons/perform-direct-dt2.svg" width="48">
</p>

<h1 align="center">digitakt-mods</h1>

<p align="center">
Tous les mods open source pour <b>Elektron Digitakt</b> et <b>Digitakt II</b>, au même endroit,<br>
vérifiés ensemble, en packs prêts à installer.
</p>

<p align="center"><a href="docs/GUIDE.md"><b>👉 Guide pas à pas illustré (aucune connaissance de GitHub requise)</b></a></p>

---

**Pour les installer, en une ligne :** télécharge l'OS officiel de ta machine et un [pack](#les-packs), glisse les deux
sur [elekloader.github.io/elekloader](https://elekloader.github.io/elekloader/), clique sur **Build**, puis envoie le
`.syx` obtenu à la Digitakt avec Elektron Transfer.

![Les 4 étapes](docs/img/flow.svg)

> ⚠️ **Non officiel.** Rien ici n'est affilié à Elektron, et tu flashes à tes risques. Le bootloader n'est jamais
> modifié, donc l'OS officiel restaure toujours la machine ([comment](docs/GUIDE.md#si-ça-ne-marche-pas)). Ce dépôt
> ne contient **aucun firmware Elektron**.

## Les packs

Un pack, c'est un `.zip` de mods qui se combinent, vérifié par elekloader contre l'OS officiel.

| pack | machine | contenu | |
|---|---|---|---|
| **Digitakt « on crack »** | Digitakt, OS 1.54 | SLICER, POLY, STRING, DT-FM, Digi Mono, DH-101 | [⬇ zip](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-graete-1.54.zip) |
| **Max synthés** | Digitakt, OS 1.54 | 16 mods : le pack précédent, plus MACRO, NEIGHBOR, Matrix, Utilities, EQ, digihealth, DIGISNAKE | [⬇ zip](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-max-synth-1.54.zip) |
| **Effets** | Digitakt, OS 1.54 | Tone+FX, DigiFilter, SLICER, digihealth, Matrix, Utilities | [⬇ zip](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-fx-1.54.zip) |
| **OB-1 + SOPHIE** | Digitakt, OS 1.54 | OB-1, SOPHIE, Digi Mono, DH-101, SLICER, POLY, STRING, digihealth | [⬇ zip](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-ob1-sophie-1.54.zip) |
| **PERFORM KIT** | Digitakt II, OS 1.17 | core, perform-direct, perform-levels | [⬇ zip](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-perform-1.17.zip) |
| **Tous les mods** | Digitakt 1.54 · 1.53 · Digitakt II | tous les fichiers, à trier toi-même | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/tous-les-mods-mk1-1.54.zip) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/tous-les-mods-mk1-1.53.zip) · [⬇ DT2](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/tous-les-mods-dt2-1.17.zip) |

## Tous les mods : Digitakt (OS 1.54 / 1.53)

Pour en ajouter un seul, télécharge son fichier (colonne de droite, celui de **ton** OS) et glisse-le sur la page
elekloader avec les autres. elekloader ajoute tout seul ceux dont il a besoin.

| | mod | ce que ça fait | fichier |
|---|---|---|---|
| <img src="docs/icons/core.svg" width="40"> | **core** | le socle sur lequel tous les autres mods se branchent (choisi tout seul par elekloader) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/core-4.0-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/core-4.0.elemod) |
| <img src="docs/icons/machine-pages.svg" width="40"> | **machine-pages** | dessine les pages des nouvelles machines ; permet d'en avoir plusieurs à la fois | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/machine-pages-1.3-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/machine-pages-1.3.elemod) |
| <img src="docs/icons/digislicer.svg" width="40"> | **DIGISLICER** | machine de découpe : coupe un sample où tu veux, joue les slices sur les trigs, STRETCH sans changer le pitch | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digislicer-2.5-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digislicer-2.5.elemod) |
| <img src="docs/icons/digimono.svg" width="40"> | **Digi Mono** | 7 synthés façon Monomachine (SIN, NOISE, SAW, PULSE, ENS, VO, POLY SIN) et CHORDS | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digimono-0.24-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digimono-0.24.elemod) |
| <img src="docs/icons/digi101.svg" width="40"> | **DH-101** | monosynthé façon SH-101, avec son filtre résonant et le glide | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digi101-0.25-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digi101-0.25.elemod) |
| <img src="docs/icons/digimacro.svg" width="40"> | **Digi Macro** | MACRO : 8 moteurs de Plaits (FM, grains, kick, snare, hi-hat…) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digimacro-1.2-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digimacro-1.2.elemod) |
| <img src="docs/icons/digipoly.svg" width="40"> | **Digi Poly** | POLY : des accords sur une piste en empruntant les voix des autres pistes, MIDI polyphonique | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digipoly-2.1-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digipoly-2.1.elemod) |
| <img src="docs/icons/dt-fm.svg" width="40"> | **DT-FM** | synthé FM 4 opérateurs, 8 algorithmes | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/dt-fm-1.2.1-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/dt-fm-1.2.1-os1.53.elemod) |
| <img src="docs/icons/digistring.svg" width="40"> | **STRING** | corde pincée ou frottée (Karplus-Strong) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digistring-0.8.0-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digistring-0.8.0.elemod) |
| <img src="docs/icons/digistring-fast.svg" width="40"> | **STRING-fast** | STRING en plus léger quand FAST AUDIO est actif ; à prendre à la place de STRING | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digistring-fast-0.8.0-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digistring-fast-0.8.0.elemod) |
| <img src="docs/icons/ob1.svg" width="40"> | **OB-1** | les oscillateurs de l'Oberheim OB-1 : 2 VCO, sync, cross-mod, sub (OS 1.54) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/ob1-0.6-os1.54.elemod) · – |
| <img src="docs/icons/digisophie.svg" width="40"> | **SOPHIE** | percussion métallique : FUSE, BOOM, PIPE, SHARD | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digisophie-1.2.0-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digisophie-1.2.0.elemod) |
| <img src="docs/icons/digineighbor.svg" width="40"> | **NEIGHBOR** | une piste joue le son d'une autre piste à travers ses propres effets (prototype) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digineighbor-0.7-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digineighbor-0.7.elemod) |
| <img src="docs/icons/digihealth.svg" width="40"> | **digihealth** | FAST AUDIO (soulage le processeur), SYSTEM INFO (charge CPU/DSP à l'écran) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digihealth-1.0-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digihealth-1.0.elemod) |
| <img src="docs/icons/digimatrix.svg" width="40"> | **Digi Matrix** | matrice de modulation : n'importe quel LFO sur n'importe quel paramètre, 8 slots | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digimatrix-1.0c-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digimatrix-1.0c.elemod) |
| <img src="docs/icons/digieq.svg" width="40"> | **Digi EQ** | EQ 4 bandes sur toutes les sorties | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digieq-1.0c-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digieq-1.0c.elemod) |
| <img src="docs/icons/digiutils.svg" width="40"> | **Digi Utilities** | scope, spectre, vue X-Y, accordeur, activité des pistes | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digiutils-1.9a-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digiutils-1.9a.elemod) |
| <img src="docs/icons/tonefx.svg" width="40"> | **Tone+FX** | effets master : ring mod, wavefolder, tilt EQ, bitcrusher, pitch, stéréo, pads PERFORM | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/tonefx-4.0c-dt-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/tonefx-4.0c-dt.elemod) |
| <img src="docs/icons/digifilter.svg" width="40"> | **DigiFilter** | nouveaux filtres par piste : BP, BP2, COMB, TRASH | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digifilter-1.3.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digifilter-1.1a.elemod) |
| <img src="docs/icons/seq-events.svg" width="40"> | **seq-events** | le socle commun de DIGISEQ et DIGISNAKE (choisi tout seul par elekloader) | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/seq-events-dt-0.2-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/seq-events-dt-0.2-os1.53.elemod) |
| <img src="docs/icons/digiseq-dt.svg" width="40"> | **DIGISEQ** | un type de séquenceur différent pour chaque piste | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digiseq-dt-0.2-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digiseq-dt-0.2-os1.53.elemod) |
| <img src="docs/icons/digisnake-dt.svg" width="40"> | **DIGISNAKE** | séquenceur « serpent » qui se balade dans une grille, façon MDD Snake / René | [⬇ 1.54](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.54/digisnake-dt-0.3-os1.54.elemod) · [⬇ 1.53](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-mk1/1.53/digisnake-dt-0.3-os1.53.elemod) |

À savoir :
- **DT-FM ou SOPHIE**, pas les deux.
- **OB-1 demande machine-pages 1.2** : prends le [pack OB-1 + SOPHIE](#les-packs), qui la contient.
- **Tout prendre ne tient pas en mémoire** : elekloader te prévient.

Le détail (conflits, mémoire de chaque mod, projets non inclus) est dans [docs/DIGITAKT-MK1.md](docs/DIGITAKT-MK1.md).

## Digitakt II (OS 1.17)

Les machines de la Digitakt (SLICER, POLY, STRING, MONO…) **n'existent pas sur la Digitakt II** : elle a un autre
processeur audio, et elles ne sont pas portées. Voici ce qui existe aujourd'hui avec elekloader :

| | mod | ce que ça fait | fichier |
|---|---|---|---|
| <img src="docs/icons/core-dt2.svg" width="40"> | **core** | le socle des mods Digitakt II (choisi tout seul par elekloader) | [⬇ 1.17](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-ii/1.17/core-1.0.elemod) |
| <img src="docs/icons/perform-direct-dt2.svg" width="40"> | **perform-direct** | [PRESET] seul active PERFORM KIT ; FUNC + PRESET ouvre le menu PRESET/KIT | [⬇ 1.17](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-ii/1.17/perform-direct-1.0.elemod) |
| <img src="docs/icons/perform-levels-dt2.svg" width="40"> | **perform-levels** | les niveaux de piste réglés en PERFORM KIT restent quand tu en sors | [⬇ 1.17](https://github.com/hillzeealex/digitakt-mods/raw/main/elemods/digitakt-ii/1.17/perform-levels-1.0.elemod) |

Deux autres projets ajoutent des synthés à la Digitakt II : [digikit](https://github.com/ElekLabs/digikit) (PLUCK) et
l'[All-in-One](https://github.com/karigardarsson/digitakt-ii-research) (Plaits, DX7). Ils **ne se combinent ni avec
ces mods ni entre eux** : on en installe un seul à la fois. Le pourquoi et le comment sont dans
[docs/DIGITAKT-II.md](docs/DIGITAKT-II.md).

## Pour les développeurs

| chemin | rôle |
|---|---|
| `elemods/<appareil>/<os>/` | les `.elemod`, tels que publiés par leurs auteurs |
| `mods.json` | le manifeste : licence, source `repo@ref`, URL et sha256 de chaque fichier |
| `recipes/` | les packs, en listes de fichiers ; chacun vérifié par `elekloader --check` ([détails](recipes/README.md)) |
| `tools/build.sh` | `tools/build.sh recipes/digitakt-mk1/graete-1.54.txt Digitakt_OS1.54.syx out/os.syx` |
| `tools/sync.py` | retélécharge depuis l'amont et vérifie les sha256 (`--verify` : hors ligne, utilisé par la CI) |
| `tools/icons.py` | génère les icônes de `docs/icons/` ; une fonction de dessin par mod |
| `.github/workflows/release.yml` | pousser un tag `vX.Y` publie les packs `.zip` en release |

Mettre à jour un mod : change son url et son sha256 dans `mods.json`, lance `python3 tools/sync.py`, puis vérifie les
recettes avec `tools/build.sh`.

## Licences

Chaque mod garde la licence de son auteur : champ `license` de `mods.json`, texte dans [`licenses/`](licenses/), code
source à la référence `source`. Merci à leurs auteurs : irpina, gdeo607, Robbie, soejrd, Alez22, mtalikka,
simonjohansson, DigiAlchemydsp, ClaidArremer, toonst, et l'équipe elekloader. L'outillage de ce dépôt est sous
[MIT](LICENSE).
