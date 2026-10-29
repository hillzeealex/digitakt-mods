# Digitakt mk1 (OS 1.53 / 1.54)

Fichiers : [`elemods/digitakt-mk1/1.54/`](../elemods/digitakt-mk1/1.54/) et
[`elemods/digitakt-mk1/1.53/`](../elemods/digitakt-mk1/1.53/). Prends le dossier de **ton** OS : elekloader refuse un
mod fait pour une autre version. Tous les mods sont au format 2 (linkables) et demandent le **core**. Le core 4.0
donne 256 KB de RAM aux mods ; elekloader indique quand une sélection dépasse ce budget.

## Les mods

| mod | ce qu'il ajoute | demande | auteur / source |
|---|---|---|---|
| **core** 4.0 | le bus d'événements sur lequel tous les autres se branchent | – | [elekloader](https://github.com/elekloader/elekloader) |
| **machine-pages** 1.3 / 1.2 | dessine les pages SRC/LFO des machines, ce qui permet à plusieurs machines de partager une build | core ≥ 3.0 | elekloader |
| **DIGISLICER** 2.5 | machine de découpe avec éditeur de slices, jeu sur les trigs ou le clavier, STRETCH sans changer le pitch | machine-pages | [irpina/digislicer](https://github.com/irpina/digislicer) |
| **digihealth** 1.0 | FAST AUDIO (baisse la charge DSP), SYSTEM INFO (CPU, DSP et mémoire dans la barre du haut) | core | [irpina/digihealth](https://github.com/irpina/digihealth) |
| **NEIGHBOR** 0.7 | une piste joue l'audio d'une autre piste à travers sa propre chaîne, comme sur l'Octatrack (prototype) | machine-pages | [irpina/digineighbor](https://github.com/irpina/digineighbor), build digi1_mods |
| **SOPHIE** 1.2.0 | percussion métallique, 4 modèles : FUSE, BOOM, PIPE, SHARD | machine-pages | [soejrd/digisophie](https://github.com/soejrd/digisophie) |
| **Digi Mono** 0.24 | MONO SIN, NOISE, SAW, PULSE, ENS, VO, POLY SIN, CHORDS | machine-pages | [gdeo607/digi1_mods](https://github.com/gdeo607/digi1_mods) |
| **Digi Macro** 1.2 | MACRO : 8 moteurs de Plaits (waveshaping, FM 2-op, noise, particles, kick, snare, hi-hat, grains) | Digi Mono | digi1_mods |
| **DH-101** 0.25 | monosynthé façon SH-101 avec son filtre 4 pôles et le glide | Digi Mono, machine-pages 1.2+ | digi1_mods (Robbie) |
| **Digi Poly** 2.1 | POLY : accords à partir des trigs d'une piste, en empruntant les voix des autres pistes ; MIDI polyphonique | machine-pages | digi1_mods |
| **Digi Matrix** 1.0c | matrice de modulation : n'importe quel LFO vers n'importe quel paramètre, 8 slots par pattern | core | digi1_mods |
| **Digi EQ** 1.0c | EQ master 4 bandes sur toutes les sorties | core | digi1_mods |
| **Digi Utilities** 1.9a | maintenir « ... » : scope, spectre, vue X-Y, accordeur, activité des pistes | core | digi1_mods |
| **Tone+FX** 4.0c | effets master : ring mod, wavefolder, tilt EQ, bitcrusher, pitch, stéréo, pads PERFORM | core | [DigiAlchemydsp/Tone-FX](https://github.com/DigiAlchemydsp/Tone-FX) |
| **DigiFilter** 1.3 (1.54) / 1.1a (1.53) | modes de filtre par piste : BP, BP2, COMB, TRASH | core | [DigiAlchemydsp/DigiFilter](https://github.com/DigiAlchemydsp/DigiFilter) |
| **STRING** 0.8.0 | corde pincée Karplus-Strong, excitateurs BOW, HIT, NOISE, PLUCK | core | [Alez22/digistring](https://github.com/Alez22/digistring) |
| **STRING-fast** 0.8.0 | STRING avec sa boucle en SRAM quand FAST AUDIO est actif, donc plus de pistes | digihealth | Alez22/digistring |
| **DT-FM** 1.2.1 | synthé FM 4 opérateurs, 8 algorithmes | machine-pages | [mtalikka/DT-FM](https://github.com/mtalikka/DT-FM) |
| **OB-1** 0.6 (1.54) | section oscillateurs de l'Oberheim OB-1 : 2 VCO, sync, cross-mod, sub | machine-pages **1.2** | [simonjohansson/elektrob-1](https://github.com/simonjohansson/elektrob-1) |
| **seq-events** 0.2 | événements de séquenceur partagés par DIGISEQ et DIGISNAKE | core | [ClaidArremer](https://github.com/ClaidArremer/digitakt-digiseq) |
| **DIGISEQ** 0.2 | un type de séquenceur par piste, sur la 2e page TRIG | seq-events, core ≥ 3.0 | [ClaidArremer/digitakt-digiseq](https://github.com/ClaidArremer/digitakt-digiseq) |
| **DIGISNAKE** 0.3 | séquenceur cartésien, d'après MDD Snake et René | seq-events, core ≥ 3.0 | [ClaidArremer/digitakt-digisnake](https://github.com/ClaidArremer/digitakt-digisnake) |

elekloader coche tout seul les dépendances déclarées par un mod (`requires` dans `mods.json`).

## Ce qui ne se combine pas

Tout a été vérifié avec `elekloader.patch --check` sur l'OS 1.54 stock (voir [`recipes/`](../recipes/)).

- **DT-FM ou SOPHIE, pas les deux** : ils exportent les mêmes symboles (`ds_machine`, `ds_voice_render`…).
- **OB-1 0.6 ne marche qu'avec machine-pages 1.2** : il patche le même site que machine-pages 1.3 (`0x40010d50`).
- **STRING ou STRING-fast**, pas les deux (conflit déclaré).
- **Tout ensemble dépasse les 256 KB de RAM.** Coût RAM approximatif de chaque mod sur core 4.0 :

| mod | RAM | mod | RAM |
|---|---|---|---|
| Tone+FX | 73 KB | DIGISNAKE (hors seq-events) | 14 KB |
| Digi Mono | 40 KB | DT-FM | 12 KB |
| DigiFilter 1.3 | 34 KB | Digi EQ | 9 KB |
| Digi Macro | 32 KB | Utilities | 9 KB |
| DIGISEQ (hors seq-events) | 27 KB | SOPHIE | 8 KB |
| NEIGHBOR | 26 KB | digihealth | 6 KB |
| STRING-fast / STRING | 26 / 25 KB | Poly | 5.5 KB |
| DIGISLICER | 23 KB | Matrix | 4.5 KB |
| DH-101 | 14 KB | seq-events | 3.4 KB |

Base : core 4.0 et machine-pages 1.3 prennent environ 15 KB.

- **La vraie limite en jeu, c'est le DSP**, pas la RAM. Le rendu stock occupe déjà environ 80 % de chaque bloc
  audio. Garde peu de pistes de synthé lourdes (VO, ENS, PULSE, STRING, DT-FM), active **FAST AUDIO** (digihealth)
  et surveille SYSTEM INFO.

## Référencés mais pas redistribués ici

| projet | pourquoi |
|---|---|
| [freeze157-prog/digipools](https://github.com/freeze157-prog/digipools) | machine multi-sample (OS 1.54) ; pas de licence, pas de release |
| [mdbjanssen-ship-it/elemod](https://github.com/mdbjanssen-ship-it/elemod) (digitom 0.8) | annoncé GPL, mais publié sans code source ; en conflit avec NEIGHBOR |
| [DigiAlchemydsp/DigiSplash](https://github.com/DigiAlchemydsp/DigiSplash) | splash screens de démarrage (OS 1.53) ; source seulement, à compiler |
| [digitaktplus/trig-pages](https://github.com/digitaktplus/trig-pages), [lvntszcs/grain](https://github.com/lvntszcs/grain) | source seulement, pas de `.elemod` publié |
| [JGuzak/digi_battery](https://github.com/JGuzak/digi_battery) | mod **matériel** (batterie), pas un firmware |
