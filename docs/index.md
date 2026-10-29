---
title: Installer des mods sur ta Digitakt
---

# Installer des mods sur ta Digitakt

Sans savoir coder. Il te faut ta machine, son câble USB, un ordinateur et 20 minutes.

![En 4 étapes : télécharge, construis, envoie, joue](img/flow.svg)

Regarde ce qui est écrit sous l'écran : **[Digitakt](#digitakt)** ou **[Digitakt II](#digitakt-ii)** ?

> **Attention :** si un jour la machine ne démarre plus, la réparation passe par une **interface MIDI** (les prises
> rondes), pas par l'USB. C'est la même chose sur les deux Digitakt. Sans interface MIDI, ne l'installe pas.

---

## Digitakt

<img src="img/digitakt.svg" width="360" alt="La Digitakt sur le menu MACHINE avec DIGISLICER, POLY, STRING">

Tu ajoutes les synthés de la story : DIGISLICER, POLY, STRING, DT-FM, MONO, CHORDS et DH-101.

**1. Télécharge ces 2 fichiers** (et installe [Elektron Transfer](https://www.elektron.se/support-downloads/transfer) si tu ne l'as pas)

[![Télécharger l'OS officiel Digitakt 1.54](img/btn-os-dt.svg)](https://www.elektron.se/wp-content/uploads/2026/10/Digitakt_OS1.54_dist.zip)
[![Télécharger le pack de mods Digitakt](img/btn-pack-dt.svg)](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-graete-1.54.zip)

Double-clique sur le **pack** pour l'ouvrir (sur Windows : clic droit, puis **Extraire tout**). Laisse le fichier
Elektron tel quel.

<a id="etape-2"></a>

**2. Fabrique ton OS** sur [elekloader](https://elekloader.github.io/elekloader/)

![Schéma de la page elekloader](img/elekloader.svg)

Clique sur **Digitakt**. Glisse le fichier Elektron, puis les 8 fichiers du pack, et clique sur **Build**. Un fichier
`.syx` se télécharge : c'est ton OS avec les mods.

**3. Envoie-le dans la Digitakt**

Branche-la en USB et ouvre **Transfer**. Glisse le `.syx` dans la fenêtre, puis appuie sur **YES** sur la machine.
Elle redémarre toute seule.

Pas de Transfer ? [Envoie-le depuis cette page](envoyer.html), avec Chrome ou Edge sur ordinateur (nouveau).

**4. Joue**

Maintiens **FUNC** et appuie sur **SRC**. Choisis une machine avec les flèches **HAUT** / **BAS**, puis appuie sur
**YES**.

---

## Digitakt II

Tu ajoutes deux améliorations de PERFORM KIT : **[PRESET]** seul l'active, et tes niveaux de piste restent quand tu
en sors. Les synthés de la Digitakt (STRING, POLY…) n'existent pas sur la Digitakt II.

[![Télécharger l'OS officiel Digitakt II 1.17](img/btn-os-dt2.svg)](https://www.elektron.se/wp-content/uploads/2026/10/Digitakt_II_OS1.17_dist.zip)
[![Télécharger le pack Digitakt II](img/btn-pack-dt2.svg)](https://github.com/hillzeealex/digitakt-mods/releases/latest/download/pack-perform-1.17.zip)

Ensuite, fais comme pour la Digitakt ([étapes 2 et 3](#etape-2)), en cliquant sur **Digitakt II** et en glissant les
3 fichiers du pack.

---

<a id="si-ca-plante"></a>

<details markdown="1">
<summary><b>Si ça plante</b></summary>

Pas de panique : les mods ne touchent jamais à la partie qui démarre la machine. Tu peux toujours remettre l'OS
officiel. Le fichier `.syx` à renvoyer est dans le `.zip` Elektron : double-clique dessus pour le sortir.

**Si elle démarre encore**, renvoie l'OS officiel comme à l'étape 3, en USB.

**Si elle ne démarre plus**, branche une interface MIDI sur ses prises rondes, puis :

![Récupération : FUNC à l'allumage, puis TRIG 4, puis renvoyer l'OS officiel](img/recovery.svg)

</details>

<details markdown="1">
<summary><b>Les mots bizarres</b></summary>

| mot | ce que c'est |
|---|---|
| **OS** | le logiciel qui tourne dans ta Digitakt |
| **.zip** | un fichier qui en contient d'autres ; on l'ouvre par un double-clic |
| **.elemod** | un mod, qui ajoute une fonction |
| **.syx** | le fichier qu'on envoie à la Digitakt pour changer son OS |
| **elekloader** | le site qui mélange l'OS officiel et les mods |
| **Transfer** | le logiciel d'Elektron qui envoie des fichiers à la machine |

</details>

<details markdown="1">
<summary><b>Comment se servir de chaque mod</b> (modes d'emploi de leurs auteurs, en anglais)</summary>

| | mod | mode d'emploi |
|---|---|---|
| <img src="icons/digislicer.svg" width="28"> | DIGISLICER | [irpina/digislicer](https://github.com/irpina/digislicer#readme) |
| <img src="icons/digipoly.svg" width="28"> | POLY, MONO, CHORDS, MACRO, MATRIX, EQ, scope | [digi1_mods](https://github.com/gdeo607/digi1_mods/blob/main/docs/USAGE.md) |
| <img src="icons/digi101.svg" width="28"> | DH-101 | [digi1_mods, DH-101](https://github.com/gdeo607/digi1_mods/blob/main/mods/digi101/README.md) |
| <img src="icons/digistring.svg" width="28"> | STRING | [Alez22/digistring](https://github.com/Alez22/digistring#readme) |
| <img src="icons/dt-fm.svg" width="28"> | DT-FM | [mtalikka/DT-FM](https://github.com/mtalikka/DT-FM#readme) |
| <img src="icons/digihealth.svg" width="28"> | FAST AUDIO, SYSTEM INFO | [irpina/digihealth](https://github.com/irpina/digihealth#readme) |
| <img src="icons/digineighbor.svg" width="28"> | NEIGHBOR | [irpina/digineighbor](https://github.com/irpina/digineighbor#readme) |
| <img src="icons/digisophie.svg" width="28"> | SOPHIE | [soejrd/digisophie](https://github.com/soejrd/digisophie#readme) |
| <img src="icons/ob1.svg" width="28"> | OB-1 | [simonjohansson/elektrob-1](https://github.com/simonjohansson/elektrob-1#readme) |
| <img src="icons/tonefx.svg" width="28"> | Tone+FX | [DigiAlchemydsp/Tone-FX](https://github.com/DigiAlchemydsp/Tone-FX#readme) |
| <img src="icons/digifilter.svg" width="28"> | DigiFilter | [DigiAlchemydsp/DigiFilter](https://github.com/DigiAlchemydsp/DigiFilter#readme) |
| <img src="icons/digiseq-dt.svg" width="28"> | DIGISEQ | [ClaidArremer/digitakt-digiseq](https://github.com/ClaidArremer/digitakt-digiseq#readme) |
| <img src="icons/digisnake-dt.svg" width="28"> | DIGISNAKE | [ClaidArremer/digitakt-digisnake](https://github.com/ClaidArremer/digitakt-digisnake#readme) |
| <img src="icons/perform-direct-dt2.svg" width="28"> | PERFORM KIT (Digitakt II) | [toonst/digitakt2-perform](https://github.com/toonst/digitakt2-perform#readme) |

</details>

<details markdown="1">
<summary><b>D'autres packs, chaque mod un par un</b></summary>

Max synthés, effets, OB-1 + SOPHIE, et le téléchargement de chaque mod séparément : tout est sur la
[page du projet](https://github.com/hillzeealex/digitakt-mods#les-packs). Ça s'installe de la même façon, seul le
pack change.

</details>

<sub>Ces mods ne viennent pas d'Elektron : tu les installes à tes risques. Sauvegarde tes projets importants avant,
comme pour n'importe quelle mise à jour.</sub>
