"""Docstring d'une ligne décrivant brièvement ce que fait le programme.

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Michaël")
__contact__ = ("michaelbecquer@yahoo.fr")
__copyright__ = "MIT"
__date__ = "2030-01-01"
__version__= "1.2.3"

import module_game


if __name__ == "__main__":
    # ici débute le programme principal
    c_game = module_game.Game()
    c_game.main()
