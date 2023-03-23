import random

""" Un element est soit une agence, soit un candidat : les classes Agence et
Candidat héritent de la classe Element.
La classe Element a deux attributs :
+ nom : chaine de caractères.
+ tuple_choix : tuple (pas une liste) des objets constituant ses choix.
La classe Element a deux méthodes :
+ __init__ pour initialiser.
+ choix() qui retourne le tuple de ses choix.
Les deux classes filles, Agence et Candidat ont une méthode spéciale __repr__
pour un affichage confortable de l'élément.
"""

# Ecrivez ces trois classes ici


class Element:
    def __init__(self, nom, tuple_choix):
        self.nom = nom
        self.tuple_choix = tuple_choix

    def choix(self):
        return self.tuple_choix


class Agence(Element):
    def __repr__(self):
        return f"Agence {self.nom}"


class Candidat(Element):
    def __repr__(self):
        return f"Candidat {self.nom}"


# ------------------------------------------------------------------------------
"""La classe Instance a deux attributs :
+ ens_agences :  l'ensemble des agences de l'instance
+ ens_candidats : l'ensemble des candidats de l'instance.
Elle contient les méthodes :
+ __init__ pour initialiser.
+ ajouter_agence qui prend en entrée une agence et l'ajoute dans l'ensemble
des agences de l'instance.
+ ajouter_candidat qui prend en entrée un candidat et l'ajoute dans l'ensemble
des candidats de l'instance.
+ __repr__ pour un affichage confortable de l'instance.
+ __len__ pour retourner le nombre d'agences (ou de candidats) de l'instance.
+ affiche_choix qui affiche proprement les choix de chaque agence et de chaque
candidat."""

# Ecrivez cette classe ici


class Instance:
    def __init__(self, ens_agences, ens_candidats):
        self.ens_agences = ens_agences
        self.ens_candidats = ens_candidats

    def ajouter_agence(self, agence):
        self.ens_agences.append(agence)

    def ajouter_candidat(self, candidat):
        self.ens_candidats.append(candidat)

    def __repr__(self):
        return f"Instance avec {len(self.ens_agences)} agences et {len(self.ens_candidats)} candidats"

    def __len__(self):
        return len(self.ens_agences)

    def affiche_choix(self):
        for agence in self.ens_agences:
            print(f"{agence} a pour choix : {agence.choix()}")
        for candidat in self.ens_candidats:
            print(f"{candidat} a pour choix : {candidat.choix()}")

    def __contains__(self, element):
        return element in self.ens_agences or element in self.ens_candidats

    def agences(self):
        return self.ens_agences

    def candidats(self):
        return self.ens_candidats


# ------------------------------------------------------------------------------
"""La classe Affectation a un attribut :
+ dico_agence_candidat : chaque clé est une agence et la valeur correspondante
est le candidat auquel il est affecté.
Cette classe contient les méthodes :
+ __init__ pour initialiser.
+ candidat_affecté_à : prend en entrée une agence et retourne le candidat qui
lui est affecté (None s'il n'y en a pas).
+ agence_affectée_à : prend en entrée un candidat et retourne l'agence qui
lui est affectée (None s'il n'y en a pas).
+ affecter : prend en entrée une agence, un candidat et affecte l'un à l'autre.
+ changer_affectation_candidat : prend en entrée agence, candidat,
nouvelle_agence et affecte candidat à nouvelle_agence et "dé-affecte" agence.
"""

# Ecrivez cette classe ici


class Affectation:
    def __init__(self, dico_agence_candidat):
        self.dico_agence_candidat = dico_agence_candidat

    def candidat_affecté_à(self, agence):
        return self.dico_agence_candidat[agence]

    def agence_affectée_à(self, candidat):
        for agence, candidat_affecté in self.dico_agence_candidat.items():
            if candidat_affecté == candidat:
                return agence
        return None

    def agence_est_affectée(self, agence):
        return agence in self.dico_agence_candidat

    def candidat_est_affecté(self, candidat):
        for agence, candidat_affecté in self.dico_agence_candidat.items():
            if candidat_affecté == candidat:
                return True
        return False

    def affecter(self, agence, candidat):
        self.dico_agence_candidat[agence] = candidat

    def changer_affectation_candidat(self, agence, candidat, nouvelle_agence):
        # On affecte le candidat à la nouvelle agence
        self.dico_agence_candidat[nouvelle_agence] = None
        # On dé-affecte l'ancienne agence
        del self.dico_agence_candidat[agence]

    def __repr__(self) -> str:
        return f"Affectation : {self.dico_agence_candidat}"

    def __contains__(self, element):
        return element in self.dico_agence_candidat or element in self.dico_agence_candidat.values()

    def __len__(self):
        return len({candidat for candidat in self.dico_agence_candidat.values() if candidat is not None})

# ------------------------------------------------------------------------------


def extraire_instance_du_fichier(file):
    """Prend en entrée un nom de fichier (chaine de caractères) et retourne
    l'instance stockée dans ce fichier. Le format du fichier est :
    n (seul sur la première ligne)
    suivi de n lignes, chacune étant sous le format :
     X:Y1:Y2:...:Yn ou X est le nom d'une agence et les n Yi suivants sont les
     noms des candidats, dans l'ordre des choix de X.
    suivi de n lignes, chacune étant sous le format :
     X:Y1:Y2:...:Yn ou X est le nom d'un candidat et les n Yi suivants sont les
     noms des agences, dans l'ordre des choix de X.
     Le séparateur est ':' sans espace entre les éléments.
     Les noms des agences et candidats ne doivent pas contenir le caractère ":"
     """
    with open(file, "r") as buffer:

        # Différence avec le code précédent : on utilise les classes

        n = int(buffer.readline())

        # On va stocker les agences et les candidats dans des dictionnaires ("nom":"objet en classe")
        dico_agences = {}
        dico_candidats = {}

        choix_agences = {}
        choix_candidats = {}

        for _ in range(n):
            line = buffer.readline()
            line = line.split(":")
            agence = line[0]
            candidats = line[1:]
            candidats = [candidat.strip() for candidat in candidats]
            choix_agences[agence] = candidats
            dico_agences[agence] = Agence(agence, None)

        for _ in range(n):
            line = buffer.readline()
            line = line.split(":")
            candidat = line[0]
            agences = line[1:]
            agences = [agence.strip() for agence in agences]
            choix_candidats[candidat] = agences
            dico_candidats[candidat] = Candidat(candidat, None)

        # Les agences ont comme liste de candidats des strings, on va les remplacer par des objets Candidat
        for agence in dico_agences.values():
            agence.tuple_choix = tuple(
                [dico_candidats[candidat] for candidat in choix_agences[agence.nom]])

        # Les candidats ont comme liste d'agences des strings, on va les remplacer par des objets Agence
        for candidat in dico_candidats.values():
            candidat.tuple_choix = tuple(
                [dico_agences[agence] for agence in choix_candidats[candidat.nom]])

        return Instance(dico_agences.values(), dico_candidats.values())


# ------------------------------------------------------------------------------


def génère_instance_aléatoire(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""
    pass

# ------------------------------------------------------------------------------


def gale_shapley_algorithm2(instance):
    """Exécute l'algorithme de Gale-Shapley sur l'instance et retourne
    l'affectation construite."""
    agenciesAssign = Affectation({})
    candidatesAssign = Affectation({})

    agenciesIndex = {agency: 0 for agency in instance.agences()}

    n = len(instance.agences())

    while not len(agenciesAssign) == n:
        for agency in instance.agences():
            if agency in agenciesAssign:
                continue

            candidate = agency.tuple_choix[agenciesIndex[agency]]

            if candidate not in candidatesAssign:
                agenciesAssign.affecter(agency, candidate)
                candidatesAssign.affecter(candidate, agency)
            else:
                currentAgency = candidatesAssign.dico_agence_candidat[candidate]
                candidateAgencyRank = candidate.tuple_choix.index(agency)

                candidateAgencyIndex = candidate.tuple_choix.index(
                    currentAgency)

                if candidateAgencyRank < candidateAgencyIndex:
                    agenciesAssign.changer_affectation_candidat(
                        currentAgency, candidate, agency)
                    candidatesAssign.changer_affectation_candidat(
                        candidate, currentAgency, agency)

            agenciesIndex[agency] += 1

    return agenciesAssign


def gale_shapley_algorithm(instance):

    affectation = Affectation({})

    agences_iter = {agence: iter(agence.choix())
                    for agence in instance.ens_agences}

    liste_agences_non_affectees = list(instance.ens_agences)

    while len(liste_agences_non_affectees) > 0:

        a = random.choice(liste_agences_non_affectees)
        c = next(agences_iter[a])

        if affectation.agence_affectée_à(c) is None:
            affectation.affecter(a, c)
            liste_agences_non_affectees.remove(a)
        else:
            k = affectation.agence_affectée_à(c)

            if c.choix().index(a) < c.choix().index(k):
                affectation.changer_affectation_candidat(k, c, a)
                liste_agences_non_affectees.remove(a)
                liste_agences_non_affectees.append(k)

    return affectation


# ------------------------------------------------------------------------------


def nombre_de_couples_non_stables(instance, affectation):
    """Retourne le nombre de couples non stables de l'affectation liée à 
    l'instance."""
    nombre_de_couples_non_stables = 0

    for a in instance.ens_agences:
        c = affectation.candidat_affecté_à(a)
        rang_de_c = a.choix().index(c)

        if rang_de_c > 0:

            liste_cand_potentiels = a.choix()[:rang_de_c]

            for cand in liste_cand_potentiels:
                agence_de_cand = affectation.agence_affectée_à(cand)
                if cand.choix().index(a) < cand.choix().index(agence_de_cand):
                    nombre_de_couples_non_stables += 1

    return nombre_de_couples_non_stables

# ------------------------------------------------------------------------------


def génère_affectation_aléatoire(instance):
    """Retourne une affectation aléatoire de l'instance."""
    number = len(instance.agences)
    import random

    # On créer deux listes de candidats et d'agences
    candidats = list(instance.candidats)
    agences = list(instance.agences)

    # On mélange les listes
    random.shuffle(candidats)
    random.shuffle(agences)

    # On créer un dictionnaire qui va contenir les affectations

    return Affectation({agence: candidat for agence, candidat in zip(agences, candidats)})


# ------------------------------------------------------------------------------


def iter_toutes_les_affectations(instance):
    """Un itérateur de toutes les affectations possibles (stables ou non
    stables). Utilise la bibliothèque itertools. """
    import itertools

    it = itertools.permutations(instance.ens_candidats)
    tuple_des_agences = tuple(instance.ens_agences)
    for perm in it:
        yield Affectation({agence: candidat for agence, candidat in zip(tuple_des_agences, perm)})

# ------------------------------------------------------------------------------
#               Tests
# ------------------------------------------------------------------------------


fichier = "couple.txt"
inst = extraire_instance_du_fichier(fichier)
# inst.affiche_choix()


# affect = gale_shapley_algorithm(inst)
# print("L'affectation produite par l'algorithme de Gayle-Shapley est :")
# print(affect)
# if nombre_de_couples_non_stables(inst, affect) != 0:
#     raise Exception("Erreur : le nbre de couples non stables doit être 0 !!")

# print(nombre_de_couples_non_stables(inst, affect))

# affect = génère_affectation_aléatoire(inst)
# print(f"Le nbre de couples non stables dans l'affectation aléatoire")
# print(affect)
# print(f"est de {nombre_de_couples_non_stables(inst, affect)}")

it = iter_toutes_les_affectations(inst)
print([el for el in it])
# liste = [nombre_de_couples_non_stables(inst, affect) for affect in it]
# liste.sort()
# print(liste)
