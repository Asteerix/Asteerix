# Asteerix

Repo "profil GitHub" personnel d'Amaury Poltavtseef (`Asteerix`) — README.md + assets SVG (header, gradient-line). Page de présentation publique : bio, stack, projets phares (2gather, Klarvon, Afreecab, asc-toolkit, etc.), contact.

## Stack

- Pas de code applicatif
- Markdown enrichi (badges img.shields.io, skillicons.dev, readme-typing-svg)
- SVG personnalisés (`assets/header.svg`, `assets/gradient-line.svg`)

## Commands

```bash
# Aucune. Le rendu est géré par GitHub côté profil utilisateur.
# Pour prévisualiser localement :
npx markdown-cli README.md            # ou tout viewer Markdown
```

## Project layout

- `README.md` — page profil GitHub (rendu sur https://github.com/Asteerix)
- `assets/header.svg` — bannière SVG du profil
- `assets/gradient-line.svg` — séparateur visuel
- `LICENSE` — MIT

## Conventions

- Tout ajout de projet phare doit pointer vers un repo réel (pas de lien mort)
- Conserver les badges en cohérence avec la stack annoncée (Flutter / Next.js / NestJS / Go / TypeScript)
- **Tout `<img>` porte un `alt`**, y compris un badge. Un badge sans `alt` à l'intérieur
  d'un lien laisse ce lien sans nom accessible : un lecteur d'écran annonce l'URL. C'est le
  critère WCAG 1.1.1, de niveau A, et la page en comptait 38 avant le 2026-08-20. Un `alt`
  vide (`alt=""`) est le bon choix pour un séparateur décoratif, et seulement pour lui.
- Ne **pas** modifier `assets/header.svg` sans backup — c'est l'identité visuelle
- Conventional commits : `type(scope): description`

## Branches

- `dev` — branche par défaut, et donc **celle que GitHub rend sur le profil**. C'est là que
  le README se modifie.
- `main` — production, reçoit une fusion depuis `dev`. Le seul déclencheur `push` de
  `snake.yml` la vise.
- `output` — **branche d'artefact, écrite uniquement par la CI**, jamais à la main. Elle ne
  contient que les deux SVG du serpent, régénérés chaque nuit et servis au README par URL
  brute. Ce n'est pas une troisième branche de travail : rien ne s'y développe, et rien ne
  s'en fusionne vers `dev`. Une fusion de ce type a déjà eu lieu et a laissé 166 Ko de
  doublons à la racine, supprimés le 2026-08-20.

## Notes

- Le repo doit s'appeler exactement comme l'utilisateur GitHub (`Asteerix`) pour que GitHub
  l'utilise comme profil.
- **Et il doit être public, ce qu'il n'est pas.** GitHub ne rend un README de profil que
  depuis un dépôt public : tant que celui-ci est privé, `github.com/Asteerix` n'affiche
  aucune page de profil. Les URL brutes du serpent
  (`raw.githubusercontent.com/Asteerix/Asteerix/output/...`) sont inaccessibles sans jeton
  pour la même raison, donc l'animation serait cassée même si la page s'affichait. Le
  rendre public contredit la règle « tous les dépôts sont privés », donc c'est un arbitrage
  à prendre, pas un oubli à corriger. État constaté le 2026-08-20.
- Une CI existe : `.github/workflows/snake.yml` régénère l'animation chaque nuit et pousse
  sur `output`. Il n'y a en revanche aucun build : une modification du `README.md` est
  visible sur le profil dès la poussée sur la branche par défaut.
- Liens emails (`mailto:apoltavtseef@gmail.com`) **publics** — pas un secret, mais à mettre
  à jour si l'adresse change.
