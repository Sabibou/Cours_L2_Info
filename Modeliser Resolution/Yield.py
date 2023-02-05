# Exercices Python sur les itérateurs, yield, yield from.
# Utilisez chaque itérateur pour produire des éléments. 

#------------------------------------------------------------------------------
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


#------------------------------------------------------------------------------
def iter_fibo():
    """Générateur des éléments de la suite de Fibonacci."""
    un = 1
    un1 = 1

    while True:
        yield un
        un, un1 = un1, un + un1
    

#------------------------------------------------------------------------------
def look_and_say_iter(z, k=1):
    """La suite Look and say mise en oeuvre avec un itérateur."""
    l = [1]

    for _ in range(k):

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


for i in look_and_say_iter(1, 10):
    print(i)



#------------------------------------------------------------------------------
def iter_tous_les_facteurs(mot):
    """Création d'un itérateur qui génére tous les facteurs non vides du mot
    donné en paramètre. Exemple : tous les facteurs de la chaine "abcd" sont :
    a ab abc abcd b bc bcd c cd d """ 
    pass


#------------------------------------------------------------------------------
def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    pass

#------------------------------------------------------------------------------
def iter_nombres_premiers(v=1):
    """Itérateur produisant tous les nombres premiers à partir de v."""
    import math  # Bibliothèque autorisée si besoin. 
    pass


#------------------------------------------------------------------------------
def iter_tous_les_sous_ensembles(ensemble):
    """Itérateur produisant tous les sous-ensembles possibles de l'ensemble
    donné en entrée."""
    pass
