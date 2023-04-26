"""Codage de Huffman.
Cette verion est purement pédagogique et ne pourrait pas être de mise en
production de manière efficace.
Chaque étape donne lieu à des objets intermédiares qui peuvent être affichés,
visualisés, contrôlés. 
Cette version code des fichiers en UTF8 dont certains caractères sont codés sur
un, deux, trois ou quatre octets."""


def construit_liste_ss_arbres_caracteres_nombres(fichier, affiche=True):
    """Pour chaque caractère c du fichier, constuit une liste :
    [(c,n), None, None] où n est le nombre de fois que c est présent dans le
    fichier. Une telle liste sera vue plus tard comme une feuille.
    Si affiche == True, afficher les paires (c,n) dans l'ordre croissant de n.
    """
    characters = {}

    with open(fichier, "r") as f:

        for ligne in f.readlines():

            for char in ligne:

                if not char in characters:

                    characters[char] = [(char, 1), None, None]

                else:

                    characters[char] = [
                        (char, characters[char][0][1] + 1), None, None]

    # On le transforme en liste

    return [characters[key] for key in characters]


def arbre_gauche(noeud):
    return noeud[1]


def arbre_droit(noeud):
    return noeud[2]


def est_feuille(noeud):
    return arbre_gauche(noeud) == None and arbre_droit(noeud) == None


def caractère(noeud):
    """Retourne le caractère du noeud si le noeud est une feuille ;
    retourne None sinon."""
    if (est_feuille(noeud)):
        return noeud[0][0]
    return None


def nb_caractères(noeud):
    """Retourne le champ numérique du noeud."""
    return noeud[0][1]


def construit_arbre_huffman_depuis_liste(liste_car_nbre):
    """À partir de la liste composée de listes du type [(c,n), None, None],
    construit et retourne l'arbre de Huffman suivant l'algorithme classique.
    Le résultat (l'arbre) est une liste composée de listes du type :
    [(c,n), a_1, a_2] avec :
    + n un entier.
    + c un caractère ; dans ce cas a_1 et a_2 sont None et c'est une feuille
        ou c est None ; Dans ce cas c'est un noeud interne et a_1 et a_2 sont
        des sous-arbres. Par convention, a_1 est le sous-arbre gauche codant 0
        et a_1 le sous-arbre droit codant 1."""
    while len(liste_car_nbre) > 1:
        liste_car_nbre = sorted(liste_car_nbre, key=lambda x: x[0][1])
        noeud_gauche = liste_car_nbre.pop(0)
        noeud_droit = liste_car_nbre.pop(0)
        liste_car_nbre.append([(None, nb_caractères(
            noeud_gauche) + nb_caractères(noeud_droit)), noeud_gauche, noeud_droit])

    return liste_car_nbre[0]


def construit_table_codage_depuis_arbre_huffman(arbre):
    """Construit la table de codage à partir de l'arbre de Huffman.
    Le resultat est un dictionnaire dont les clés sont les caractères et les
    valeurs sont les codes binaires correspondant issus de l'arbre. Un code
    binaire est retourné ici sous forme de chaine de cararctères de '0' et '1'.
    """
    codes = {}

    def parcours(arbre, code):
        if est_feuille(arbre):
            codes[caractère(arbre)] = code
        else:
            parcours(arbre_gauche(arbre), code + "0")
            parcours(arbre_droit(arbre), code + "1")

    parcours(arbre, "")
    return codes


def code_fichier(fichier, table_codage):
    """Code chaque caractère du fichier avec la table de codage dont les clés
    sont les caractères et les valeurs les codes binaires sous forme de chaines
    de '0' et de '1'.
    Le résultat est une chaine de caractères de '0' et de '1'."""
    # On utilisera construit_liste_ss_arbres_caracteres_nombre pour construire la table de codage
    liste_feuilles = construit_liste_ss_arbres_caracteres_nombres(
        fichier, False)

    # On construit l'arbre de Huffman
    arbre = construit_arbre_huffman_depuis_liste(liste_feuilles)

    # On construit la table de codage
    table = construit_table_codage_depuis_arbre_huffman(arbre)

    result = ""

    for char in open(fichier, "r").read():

        if char in table:
            result += table[char]

    return result


def decode_message(message_binaire, arbre):
    """Prend en entrée une chaine de caractères de '0' et de '1' (message codé)
    + un arbre de huffman. Retourne le décodage sous forme d'une chaine de
    caractères."""
    result = ""
    node = arbre

    for char in message_binaire:

        if char == "0":
            node = arbre_gauche(node)
        else:
            node = arbre_droit(node)

        if est_feuille(node):
            result += caractère(node)
            node = arbre

    return result


# ----- Manipulations de ces fonctions.

# Partie codage du fichier :
fichier = "houghman.py"
# fichier = "Codage-Huffman-Simple.py" # Pour coder le fichier source lui-même.
liste_feuilles = construit_liste_ss_arbres_caracteres_nombres(fichier, False)
arbre = construit_arbre_huffman_depuis_liste(liste_feuilles)
table = construit_table_codage_depuis_arbre_huffman(arbre)
# Codage Huffman en bin. du fichier
message_codé = code_fichier(fichier, table)

print(f"Le message codé est :\n{message_codé}")
print(10*"---")
print(f"La taille du message codé est de : {len(message_codé)} bits, soit " +
      f"{len(message_codé)/8} octets.")
print(10*"---")

# Partie décodage :

message_décodé = decode_message(message_codé, arbre)
print(f"Le message décodé est : \n{message_décodé}")
