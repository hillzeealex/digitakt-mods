# Digitakt mk1 (OS 1.53 / 1.54)

Fichiers : [`elemods/digitakt-mk1/1.54/`](../elemods/digitakt-mk1/1.54/) et
[`elemods/digitakt-mk1/1.53/`](../elemods/digitakt-mk1/1.53/). Prends le dossier de **ton** OS : elekloader refuse un
mod fait pour une autre version. Tous les mods sont au format 2 (linkables) et demandent le **core**. Le core 4.0
donne 256 KB de RAM aux mods ; elekloader indique quand une sélection dépasse ce budget.

## Les mods

La liste, avec ce que fait chaque mod, son icône et son fichier : [README](../README.md#tous-les-mods--digitakt-os-154--153).
Les dépendances de chaque fichier sont dans le champ `requires` de [`mods.json`](../mods.json), et elekloader les coche tout seul.

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
