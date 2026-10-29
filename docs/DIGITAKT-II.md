# Digitakt II (OS 1.17)

**À savoir d'abord :** les machines des captures mk1 (DIGISLICER, POLY, STRING, DT-FM, Digi Mono, DH-101…)
**n'existent pas sur Digitakt II**. Le DT2 a un autre processeur DSP (SHARC), et ces mods ne sont pas portés. Sur le
DT2, trois chaînes d'outils existent, et elles **s'excluent mutuellement** : on en flashe une seule à la fois.

## Les trois chemins

| | 1. elekloader | 2. digikit | 3. All-in-One |
|---|---|---|---|
| ce que ça ajoute | PERFORM KIT : accès direct, niveaux conservés | runtime (menu SETTINGS > DIGIKIT), PLUCK (corde pincée), frequency shifter | 25 modèles Plaits, 4 banques DX7, Musical WAVE / Déjà Vu, One-Shot Zoom |
| fichiers | ici : [`elemods/digitakt-ii/1.17/`](../elemods/digitakt-ii/1.17/) | [ElekLabs/digikit](https://github.com/ElekLabs/digikit) | [karigardarsson/digitakt-ii-research](https://github.com/karigardarsson/digitakt-ii-research) v0.3.0-beta |
| licence | GPL-2.0-or-later | AGPL-3.0-or-later | AGPL-3.0-or-later (racine du repo en MIT) |
| testé sur une machine | core + perform-direct oui, perform-levels oui ; les deux ensemble pas encore | runtime + PLUCK oui, freqshift non | une build précédente oui ; la v0.3.0 exacte non |
| builder | Python, toutes plateformes | `mise` + toolchains, macOS / Linux | **Windows x64 uniquement** (à reconstruire soi-même sur macOS) |

### Pourquoi on ne peut pas les combiner

Vérifié dans les sources : `mods/core-dt2/mod.json` (elekloader) et `devices/ports/dt2-1.17.toml` (digikit).

- **Même site de patch.** Le core DT2 d'elekloader et le menu digikit détournent tous les deux la liste SETTINGS en
  `0x400a5eac`.
- **Même mémoire.** La région d'expansion de digikit (`0x47e8b000-0x47fe0000`) contient celle du core elekloader
  (`0x47F00000-0x47F40000`).
- **Chaque outil refuse un OS déjà patché par l'autre**, car les deux exigent un OS stock reconnu par son hash.
- **All-in-One** est bâti sur digikit, mais il intègre ses machines dans l'image. Il ne contient ni le runtime, ni
  PLUCK, ni freqshift, et on ne peut pas y charger de modules digikit.

## 1. elekloader : core + perform

| mod | ce qu'il fait |
|---|---|
| **core** 1.0 | le core DT2 d'elekloader (tick, draw, key, enc, SETTINGS, PERSONALIZE) |
| **perform-direct** 1.0 | [PRESET] seul bascule PERFORM KIT ; [FUNC] + [PRESET] ouvre le menu PRESET/KIT |
| **perform-levels** 1.0 | les niveaux de piste réglés en PERFORM KIT restent quand on en sort |

Source : [toonst/digitakt2-perform](https://github.com/toonst/digitakt2-perform) v1.0. Combinaison vérifiée par
`elekloader --check` sur l'OS 1.17 stock : environ 255 KB de RAM restent libres. Voir la recette
[`recipes/digitakt-ii/perform-1.17.txt`](../recipes/digitakt-ii/perform-1.17.txt).

L'app elekloader v0.4.0 est antérieure au support DT2. Utilise la ligne de commande depuis `main` (`tools/build.sh`
le fait pour toi). La page web n'a pas été vérifiée pour le DT2.

## 2. digikit

```sh
mise install && mise run setup && mise run patch:toolchains
mise run patch -- --firmware firmware/Digitakt_II_OS1.17.syx -o out/patch/digikit-dt2.syx
mise run patch:preflight -- out/patch/digikit-dt2.syx        # doit afficher PREFLIGHT OK
# flasher via Transfer (USB), puis charger un module :
mise run dk:run -- digikit/pluck --port Digitakt --seconds 60
```

Sans `--modules`, le patch applique le set `device`. Celui-ci contient `dynfx` et `fxpages`, dont freqshift a besoin.

## 3. All-in-One

Lance `DT2-All-in-One-Builder.exe` sous Windows avec ton `Digitakt_II_OS1.17.syx`. Lis d'abord leurs pages
[Installation](https://github.com/karigardarsson/digitakt-ii-research/blob/main/docs/INSTALLATION.md) et
[Recovery](https://github.com/karigardarsson/digitakt-ii-research/blob/main/docs/RECOVERY.md). Problème connu : un
clic récurrent au déclenchement de Plaits. Le `.syx` produit contient du code Elektron : ne le redistribue jamais.

## Référencés mais pas redistribués ici

| projet | statut |
|---|---|
| [octplane/digitakt-ii-splash-screens](https://github.com/octplane/digitakt-ii-splash-screens) | affiche les 5 splashs de démarrage ; MIT, mais **OS 1.16 seulement**, le patch avorte sur 1.17 |
| [Fadedlimes/digisplash-ii](https://github.com/Fadedlimes/digisplash-ii) | splash ou animation de démarrage custom, OS 1.17 ; **pas de licence** |
| [lalzart/dt2-machine-lab](https://github.com/lalzart/dt2-machine-lab) | Sketch/BUF, Capicola, ARP ; OS 1.16, **pas de licence**, labo de recherche |
| [heavylight-industries/keyframer-lab](https://github.com/heavylight-industries/keyframer-lab) | outil de recherche dans le navigateur ; pas un mod |

## Récupération (DT2)

Maintiens FUNC à l'allumage, appuie sur TRIG 4 (OS UPGRADE), puis envoie l'OS stock avec Transfer, en mode legacy,
**par MIDI DIN** (pas par USB). Ça prend une quinzaine de minutes.
