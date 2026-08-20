#!/usr/bin/env python3
"""Prouve que check-readme.py refuse ce qu il dit refuser.

Un controle qui ne sait pas echouer ne controle rien. Chaque cas mute une seule
chose dans une copie du vrai README, puis verifie la sortie en erreur.
Bibliotheque standard uniquement.
"""

import importlib.util
import pathlib
import shutil
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent.parent

_spec = importlib.util.spec_from_file_location(
    "check_readme", ICI.parent / "check-readme.py"
)
check_readme = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_readme)

REEL = (RACINE / "README.md").read_text(encoding="utf-8")

MUTATIONS = [
    (
        '<img src="./assets/header.svg" width="100%" alt="Amaury Poltavtseef - Solo Full-Stack & Mobile Developer" />',
        '<img src="./assets/header.svg" width="100%" />',
        "img sans alt",
    ),
    (
        '<img src="./assets/gradient-line.svg" width="100%" alt="">',
        '<img src="./assets/disparu.svg" width="100%" alt="">',
        "reference locale absente",
    ),
]


def page(dossier: pathlib.Path, contenu: str) -> pathlib.Path:
    shutil.copytree(RACINE / "assets", dossier / "assets")
    chemin = dossier / "README.md"
    chemin.write_text(contenu, encoding="utf-8")
    return chemin


def refuse(contenu: str, cas: str) -> None:
    with tempfile.TemporaryDirectory() as brut:
        chemin = page(pathlib.Path(brut), contenu)
        try:
            check_readme.check(chemin)
        except SystemExit as sortie:
            assert sortie.code == 1, f"{cas}: sortie {sortie.code}, attendu 1"
            return
    raise AssertionError(f"{cas}: accepte alors qu il devait etre refuse")


def main() -> None:
    with tempfile.TemporaryDirectory() as brut:
        check_readme.check(page(pathlib.Path(brut), REEL))

    for motif, remplacement, cas in MUTATIONS:
        assert motif in REEL, f"{cas}: le motif attendu n est plus dans le README"
        refuse(REEL.replace(motif, remplacement, 1), cas)

    refuse(REEL + '\n<img src="./assets/header.svg">\n', "img ajoute sans alt")
    refuse(REEL + "\n![](./assets/header.svg)\n", "image markdown sans alt")
    refuse(
        REEL + "\n[lien](./assets/jamais-vu.svg)\n",
        "lien markdown vers un fichier absent",
    )

    print(f"{len(MUTATIONS) + 4} cas verifies, tous conformes")


if __name__ == "__main__":
    main()
