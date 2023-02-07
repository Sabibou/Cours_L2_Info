# Exercices Python sur les itérateurs, yield, yield from.
# Utilisez chaque itérateur pour produire des éléments.

# ------------------------------------------------------------------------------
def iter_syracuse(n):
    """Prend en entrée un entier n>0. Retourne un itérateur sur les éléments de
    la suite de syracuse lorsque le terme initial est n."""
    un = 1
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + un
    yield 1

# for val in iter_syracuse(10):
#     print(val)


# ------------------------------------------------------------------------------
def iter_fibo():
    """Générateur des éléments de la suite de Fibonacci."""
    un = 1
    un1 = 1

    while True:
        yield un
        un, un1 = un1, un + un1

# for val in iter_fibo():
#     print(val)

# ------------------------------------------------------------------------------


def look_and_say_iter():
    """La suite Look and say mise en oeuvre avec un itérateur."""
    l = [1]

    while True:

        yield l

        n = 0
        m = 0
        l2 = []

        # On parcourt la liste l et on compte le nombre de fois que l[n] est égal à l[m]
        while n < len(l):

            # On incrémente n jusqu'à ce que l[n] soit différent de l[m]
            while n < len(l) and l[n] == l[m]:
                n += 1

            # On ajoute le nombre de fois que l[m] est présent dans l et l[m] à la liste l2
            l2.append(n - m)

            # On ajoute l[m] à la liste l2
            l2.append(l[m])

            m = n

        # On met à jour la liste l
        l = l2

# i = 0
# for val in look_and_say_iter():
#     print(val)
#     i+=1
#     if i == 10:
#         break

# ------------------------------------------------------------------------------


def iter_tous_les_facteurs(mot):
    """Création d'un itérateur qui génére tous les facteurs non vides du mot
    donné en paramètre. Exemple : tous les facteurs de la chaine "abcd" sont :
    a ab abc abcd b bc bcd c cd d """
    length = len(mot)
    for intervalleX in range(length):

        for intervalleY in range(intervalleX, length):

            yield (mot[intervalleX: intervalleY+1])

# for val in iter_tous_les_facteurs("abcd"):
#     print(val)


# ------------------------------------------------------------------------------

def decalage(liste):
    length = len(liste)
    return [liste[(i-1) % length] for i in range(length)]


def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    for i in range(2**n):
        l = []
        for j in range(n):
            l.append((i >> j) % 2)
        yield l


def iter_toutes_les_listes_binaires2(n):
    def h(i):
        if i == n:
            yield resultat
        else:
            resultat[i] = 0
            yield from h(i+1)
            resultat[i] = 1
            yield from h(i+1)

    resultat = ["RIEN"] * n
    yield from h(0)


# i = 0
# for val in iter_toutes_les_listes_binaires2(3):
#     i += 1
#     print(i,val)

# ------------------------------------------------------------------------------
def iter_nombres_premiers(v=1):
    """Itérateur produisant tous les nombres premiers à partir de v."""
    import math  # Bibliothèque autorisée si besoin.

    v = v if v % 2 == 1 else v+1

    while True:

        sqrtV = math.floor(math.sqrt(v))
        vo2 = math.ceil(v/2)

        isPrime = True

        for div in range(2, sqrtV):
            if v % div == 0:
                isPrime = False
                break

        if isPrime == True:
            yield v

        v += 2


# i = 0
# for prime in iter_nombres_premiers(30):
#     print(prime)

#     i += 1

#     if i == 10:
#         break


# ------------------------------------------------------------------------------
def iter_tous_les_sous_ensembles(ensemble):
    """Itérateur produisant tous les sous-ensembles possibles de l'ensemble
    donné en entrée."""
    length = len(ensemble)

    for i in range(2**length):
        l = []
        for j in range(length):
            if (i >> j) % 2 == 1:
                l.append(ensemble[j])
        yield l


def iter_tous_les_sous_ensembles2(ensemble):

    liste = list(ensemble)

    length = len(liste)

    for el in iter_toutes_les_listes_binaires2(length):
        yield [liste[i] for i in range(length) if el[i] == 1]

# i = 0
# for el in iter_tous_les_sous_ensembles2({"a", "b", "c", "d"}):
#     i += 1
#     print(i, el)
