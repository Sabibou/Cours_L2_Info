"""Programmation d'un système de re-écriture de chaines de caractères.

Dans cette activité on travaille avec des chaines de caractères ne
pouvant contenir QUE les caractères "X", "0" et "1".

En entrée on se donne une chaine composée uniquement de "X" (rien d'autre).
Cette chaine doit être re-écrite, tant que cela est possible, à l'aide des
règles ci-dessous.
Attention :
+ la règle 3 ne doit être utilisée QUE si les deux premières ne peuvent
pas/plus être utilisées. 
+ Dans la description des règles ci-dessous, w et w' désignent des chaines
quelconques, de longueurs quelconques, y compris nulles. 

Règle 1 : Xw -> 0Xw
Règle 2 : w0XXw' -> wX0w'
Règle 3 : w0Xw' -> w1w'

- XXX
- 0XXX
- X0X
- 0X0X
- 10X
- 11

À faire :
+ Essayez quelques cas à la main. Par exemple, re-écrivez "XXX".
+ Programmez ce procédé de re-écriture.
+ À quoi sert-il ? Prouvez-le...
+ Programmez le système inverse.

NB : vous ne devez pas utiliser de bibliothèque. 
"""


def regle_1(chaine):
    """Application de la règle 1"""
    if chaine.startswith("X"):
        return True, "0" + chaine
    return False, None


def regle_2(chaine):
    """Application de la règle 2. """
    index = chaine.find("0XX")

    if index != -1:
        return True, chaine[:index] + "X0" + chaine[index+3:]
    return False, None


def regle_3(chaine):
    """Application de la règle 3."""
    index = chaine.find("0X")

    if index != -1:
        return True, chaine[:index] + "1" + chaine[index+2:]
    return False, None


def regle_1_I(chaine):
    if chaine.startswith("0X"):
        return True, chaine[1:]

    return False, None

def regle_2_I(chaine):
    index = chaine.find("X0")

    if index != -1:
        return True, chaine.replace("X0", "0XX", 1)
    
    return False, None

def regle_3_I(chaine):
    index = chaine.find("1")

    if index != -1:
        return True, chaine.replace("1", "0X", 1)

    return False, None

def traduit(chaine):
    """Appliquer les règles de re-écriture 1, 2 et 3 tant que c'est possible.
    Attention : n'appliquer la règle 3 que si les deux premières ne sont plus
    applicables."""
    worked = True

    while worked:

        print(chaine)

        worked, chaine2 = regle_1(chaine)

        if worked:
            chaine = chaine2
            continue

        worked, chaine2 = regle_2(chaine)

        if worked:
            chaine = chaine2
            continue

        worked, chaine2 = regle_3(chaine)

        if worked:
            chaine = chaine2


def alpha(w):
    composanteA = w.replace("X", "")
    composanteB = 0
    subList = []

    for i in range(len(w)):
        if w[i] == "X":
            subList = w[i:]
            composanteB += 2 ** (subList.count("1") + subList.count("0"))
    
    # Transfrorm composanteA to decimal
    composanteA = int(composanteA, 2)

    return composanteA + composanteB


print(alpha("XXX11X0X110"))
# traduit("X"*31)
