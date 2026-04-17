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
- Ne **pas** modifier `assets/header.svg` sans backup — c'est l'identité visuelle
- Conventional commits : `type(scope): description`

## Notes

- Le repo doit s'appeler exactement comme l'utilisateur GitHub (`Asteerix`) pour que GitHub l'utilise comme profil.
- Pas de CI, pas de build — toute modification du `README.md` est immédiatement visible sur le profil après push.
- Liens emails (`mailto:apoltavtseef@gmail.com`) **publics** — pas un secret, mais à mettre à jour si l'adresse change.
