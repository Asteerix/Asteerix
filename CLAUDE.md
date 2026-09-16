# Asteerix

Repo "profil GitHub" personnel d'Amaury Poltavtseef (`Asteerix`) — README.md + assets SVG (header, gradient-line). Page de présentation publique : bio, stack, expériences, contact. Depuis le 2026-09-16 son contenu est le miroir du CV : la seule source des faits est `~/Desktop/Freelance/cv/src/cv_base.py` (dates, rôles, puces, compétences). Aucun chiffre d'inventaire (écrans, apps, produits), aucun lien de store, aucun projet absent du CV ; Genie et Thot ont été livrées aux clients et jamais publiées, Sinao et 2gather sont les deux applications en ligne.

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
- Conserver les badges en cohérence avec les compétences de `cv_base.py` (Flutter, Dart, TypeScript, NestJS, Next.js, React, Vue.js, Symfony, Go, C#) ; pas de badge d'un fournisseur de modèle autre qu'Anthropic
- **Tout `<img>` porte un `alt`**, y compris un badge. Un badge sans `alt` à l'intérieur
  d'un lien laisse ce lien sans nom accessible : un lecteur d'écran annonce l'URL. C'est le
  critère WCAG 1.1.1, de niveau A, et la page en comptait 38 avant le 2026-08-20. Un `alt`
  vide (`alt=""`) est le bon choix pour un séparateur décoratif, et seulement pour lui.
- Ne **pas** modifier `assets/header.svg` sans backup, c'est l'identité visuelle ; le sous-titre est passé de « Solo Full-Stack & Mobile Developer » à « Flutter and Full-Stack Developer » le 2026-09-16, l'ancien texte est dans l'historique git
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
- **Et il est public depuis le 2026-09-17**, par décision d'Amaury (arbitrage tranché contre la règle « tous les dépôts sont privés », pour ce seul dépôt : les gabarits shipkit et polta-starters restent privés). GitHub ne rend un README de profil que depuis un dépôt public, et les URL brutes du serpent (`raw.githubusercontent.com/Asteerix/Asteerix/output/...`) ne répondent qu'à cette condition ; les deux sont vérifiés le 2026-09-17 (page rendue, SVG en 200). Wiki, issues, projets et discussions sont désactivés sur ce dépôt : c'est une page, pas un projet.
- Une CI existe : `.github/workflows/snake.yml` régénère l'animation chaque nuit et pousse
  sur `output`. Il n'y a en revanche aucun build : une modification du `README.md` est
  visible sur le profil dès la poussée sur la branche par défaut.
- Liens emails (`mailto:apoltavtseef@gmail.com`) **publics** — pas un secret, mais à mettre
  à jour si l'adresse change.

## Réglages du dépôt, posés par l'API le 2026-09-17

Tout est lisible par `gh api repos/Asteerix/Asteerix/...`, rien n'est à refaire à la main.

- **Actions** : `allowed_actions: selected`, actions GitHub seules plus l'allow-list
  `Platane/snk@*`, `Platane/snk/svg-only@*`, `crazy-max/ghaction-github-pages@*` ;
  `sha_pinning_required: true` (les trois `uses` sont déjà épinglés au SHA) ; jeton par
  défaut en lecture seule, sans approbation de PR ; approbation exigée pour tout
  contributeur externe avant qu'un workflow de fork ne tourne. **Piège mesuré** : le motif
  `Platane/snk@*` ne couvre pas l'action en sous-dossier `Platane/snk/svg-only`, le
  workflow du serpent est parti en `startup_failure` jusqu'à l'ajout du motif complet.
- **Ruleset** « dev et main : ni suppression ni force push » (id 23566854), actif, sur
  `refs/heads/dev` et `refs/heads/main`. `output` n'y est pas : la CI la réécrit.
- **Sécurité** : alertes Dependabot, mises à jour de sécurité Dependabot, secret scanning
  et push protection actifs, signalement privé de vulnérabilités ouvert. Les motifs hors
  fournisseur et les contrôles de validité restent `disabled` : ils demandent Advanced
  Security, indisponible sur ce plan. CodeQL non configuré : le dépôt n'a aucun langage
  détecté (les deux scripts Python vivent sous `.github/`), la configuration par défaut
  tournait à vide.
- **Interactions** limitées aux collaborateurs jusqu'au 2027-03-16 (six mois, le maximum
  que GitHub accepte) : ni issue, ni PR, ni commentaire d'inconnu sur une page de profil.
- **Fonctionnalités** : wiki, issues, projets, discussions désactivés ; squash et rebase
  autorisés, merge commit non ; branches fusionnées supprimées automatiquement.
- **Posés par l'interface, sans API** (2026-09-17, extension Chrome) : commentaires sur les
  commits désactivés (`has_commit_comments`), mises à jour de sécurité groupées et alertes
  malware Dependabot activées, limites de revue de code (`/settings/code_review_limits`,
  approbations réservées aux comptes ayant au moins l'accès lecture). Rétention des
  journaux d'Actions laissée à 90 jours : aucun artefact n'est produit.
