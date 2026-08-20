#!/usr/bin/env python3
"""Verifie la page de profil avant qu elle ne parte sur GitHub.

Deux choses, parce que ce sont les deux qui se degradent en silence a chaque
edition a la main. Un `<img>` sans `alt` a l interieur d un lien laisse ce lien
sans nom accessible, et un lecteur d ecran annonce l URL: c est le critere WCAG
1.1.1, de niveau A, et la page en comptait trente-huit. Une reference locale
vers un fichier absent devient une image cassee sur la page publique.

Un `alt` vide est accepte: c est le marqueur volontaire d une image decorative,
et le separateur en degrade en est une. Un `alt` absent ne l est pas.

Bibliotheque standard uniquement: rien a installer, ni ici ni sur le runner.
"""

import html.parser
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
EXTERNE = ("http://", "https://", "//", "#", "mailto:", "data:")
MARKDOWN_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<cible>[^)\s]+)")
# Cible locale d un lien ou d une image markdown: un chemin avec extension et
# sans schema. Le `:` exclut `https://` et `mailto:`, l extension exclut `#ancre`.
# Volontairement etroit: on verifie des chemins, on n ecrit pas un analyseur
# markdown, et les imbrications `[![alt](img)](lien)` n ont pas a etre demelees.
MARKDOWN_LOCAL = re.compile(r"\]\((?P<cible>\.{0,2}/?[^)\s:]+\.[A-Za-z0-9]+)\)")


def fail(message: str) -> None:
    print(f"ERREUR: {message}", file=sys.stderr)
    sys.exit(1)


class Lecteur(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sans_alt: list[str] = []
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributs = dict(attrs)
        if tag == "img" and "alt" not in attributs:
            self.sans_alt.append(attributs.get("src", "<sans src>"))
        for nom in ("src", "srcset", "href"):
            valeur = attributs.get(nom)
            if valeur:
                self.references.append(valeur)


def check(page: pathlib.Path) -> None:
    texte = page.read_text(encoding="utf-8")

    lecteur = Lecteur()
    lecteur.feed(texte)

    if lecteur.sans_alt:
        for source in lecteur.sans_alt[:5]:
            print(f"  sans alt: {source}", file=sys.stderr)
        fail(f"{page.name}: {len(lecteur.sans_alt)} image(s) sans attribut alt")

    references = list(lecteur.references)
    for correspondance in MARKDOWN_IMAGE.finditer(texte):
        if not correspondance.group("alt").strip():
            fail(
                f"{page.name}: image markdown sans alt vers {correspondance.group('cible')}"
            )
    references += [m.group("cible") for m in MARKDOWN_LOCAL.finditer(texte)]

    manquants = []
    for reference in references:
        if reference.startswith(EXTERNE):
            continue
        if not (page.parent / reference.lstrip("./")).is_file():
            manquants.append(reference)
    if manquants:
        fail(f"{page.name}: reference(s) locale(s) absente(s): {', '.join(manquants)}")

    images = sum(1 for _ in re.finditer(r"<img\b", texte))
    print(
        f"{page.name}: {images} images, toutes avec alt, aucune reference locale morte"
    )


if __name__ == "__main__":
    check(RACINE / "README.md")
