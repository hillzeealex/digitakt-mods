# Recettes

Chaque fichier liste des `.elemod` qui se combinent. Toutes les recettes ont passé `elekloader.patch --check`
contre l'OS stock officiel le 29 octobre 2026 : pas de chevauchement, octets stock conformes, RAM dans le budget.

| recette | contenu | RAM libre |
|---|---|---|
| [`digitakt-mk1/graete-1.54.txt`](digitakt-mk1/graete-1.54.txt) | la build des captures : DIGISLICER, POLY, STRING, DT-FM, Digi Mono, DH-101 | 123 KB |
| [`digitakt-mk1/max-synth-1.54.txt`](digitakt-mk1/max-synth-1.54.txt) | 16 mods : graete, plus MACRO, NEIGHBOR, digihealth, Matrix, Utilities, EQ, DIGISNAKE | 18 KB |
| [`digitakt-mk1/fx-1.54.txt`](digitakt-mk1/fx-1.54.txt) | Tone+FX, DigiFilter, DIGISLICER, digihealth, Matrix, Utilities | 92 KB |
| [`digitakt-mk1/ob1-sophie-1.54.txt`](digitakt-mk1/ob1-sophie-1.54.txt) | OB-1 et SOPHIE, plus Mono, DH-101, SLICER, POLY, STRING, digihealth | 38 KB |
| [`digitakt-ii/perform-1.17.txt`](digitakt-ii/perform-1.17.txt) | core DT2, perform-direct, perform-levels | 255 KB |

## Construire

```sh
tools/build.sh recipes/digitakt-mk1/graete-1.54.txt ~/Downloads/Digitakt_OS1.54.syx               # vérifie seulement
tools/build.sh recipes/digitakt-mk1/graete-1.54.txt ~/Downloads/Digitakt_OS1.54.syx out/graete.syx # écrit l'OS
```

Il faut Python 3.9+ et git. Le script clone elekloader dans `.cache/`. `VERSION=GR01` choisit la version affichée
par la machine.

Sans ligne de commande : ouvre <https://elekloader.github.io/elekloader/>, dépose ton OS stock et les fichiers de la
recette, puis clique sur Build.

## Notes

- **Une recette a passé `--check`, pas un test sur machine.** Chaque mod a été testé par son auteur, mais pas
  forcément dans cette combinaison. Une machine qui ne démarre pas se récupère toujours avec l'OS stock (FUNC +
  TRIG 4).
- **Le DSP limite avant la RAM.** Active FAST AUDIO (digihealth) et surveille SYSTEM INFO avant de lancer huit pistes
  de synthé.
- **Pas de recette OS 1.53.** Elektron ne publie plus que la 1.54. Les mêmes mods existent dans
  `elemods/digitakt-mk1/1.53/` (sauf OB-1 et DigiFilter 1.3), mais ces combinaisons n'ont pas été vérifiées.
