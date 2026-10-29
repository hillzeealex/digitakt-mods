# digitakt-mods

Tous les mods open source pour **Elektron Digitakt mk1** (OS 1.53 / 1.54) et **Digitakt II** (OS 1.17), au même
endroit, avec leurs licences, leur source amont et des combinaisons vérifiées par
[elekloader](https://github.com/elekloader/elekloader).

> **Non officiel. Rien ici n'est affilié à Elektron.** Flasher un OS modifié se fait à tes risques. Le bootloader
> n'est jamais modifié, donc l'OS stock restaure toujours la machine (voir [Récupération](#récupération)).
> **Aucun firmware Elektron n'est dans ce repo** : chacun fournit son propre OS stock, et la CI refuse tout
> `.syx`, `.zip` ou `.bin`.

## Comment ça marche

Un mod `.elemod` ne contient que le code de son auteur, plus les empreintes des octets stock qu'il s'attend à
trouver. elekloader part de **ton** fichier OS officiel, vérifie que les mods choisis ne se marchent pas dessus
(sites, mémoire, symboles), puis écrit un `.syx` que tu flashes comme une mise à jour normale.

1. Télécharge l'OS stock sur le site d'Elektron :
   [Digitakt](https://www.elektron.se/support-downloads/digitakt) ou
   [Digitakt II](https://www.elektron.se/support-downloads/digitakt-ii).
2. Choisis tes mods dans [`elemods/`](elemods/), ou prends une recette toute prête dans [`recipes/`](recipes/).
3. Construis ton OS :
   - **dans le navigateur**, rien à installer : <https://elekloader.github.io/elekloader/>. Tu y déposes l'OS stock et
     les `.elemod`, puis tu cliques sur Build ;
   - **ou en ligne de commande** : `tools/build.sh` (voir [`recipes/`](recipes/)).
4. Envoie le `.syx` obtenu à la machine avec Elektron Transfer.

## Contenu

| chemin | rôle |
|---|---|
| `elemods/<appareil>/<os>/` | les fichiers `.elemod`, tels que publiés par leurs auteurs |
| `mods.json` | le manifeste : une entrée par fichier (licence, source `repo@ref`, URL, sha256) |
| `licenses/` | la licence de chaque projet amont |
| `recipes/` | des listes de mods qui se combinent, vérifiées par `elekloader --check` |
| `tools/sync.py` | retélécharge depuis l'amont et vérifie les sha256 (`--verify` : hors ligne) |

Mettre à jour un mod : modifie son entrée dans `mods.json` (url et sha256), puis lance `python3 tools/sync.py`.

## Appareils

- [Digitakt mk1, OS 1.53 / 1.54](docs/DIGITAKT-MK1.md) : 22 mods, conflits et budget RAM.

## Récupération

Si un OS custom ne démarre pas, maintiens **FUNC** à l'allumage pour ouvrir le menu de démarrage, appuie sur
**TRIG 4** (OS UPGRADE), puis envoie l'OS stock `.syx` avec Transfer, en mode legacy.

- Digitakt II : passe par les ports **MIDI DIN**, pas par l'USB.
- Digitakt mk1 : l'USB fonctionne.

## Licences

Chaque `.elemod` garde la licence de son auteur (champ `license` de `mods.json`, texte dans `licenses/`). Le code
source correspondant se trouve à la référence `source` de chaque entrée. L'outillage de ce repo est sous MIT.
