import time
import math

# Dans cette activité, tous les entiers sont positifs.
# Soit n un entier.
# On dit que d est un "diviseur strict" de n si d divise n et d<n.
# On dira que deux entiers n et m sont "couplés" si :
# la somme des diviseurs stricts de n est égale à m et la somme des
# diviseurs stricts de m est égale à n.
# NB : n et m peuvent avoir la même valeur (un entier peut donc
# être couplé avec lui même).

# Ecrivez la fonction Booléenne qui prend en entrée deux entiers et
# retourne la valeur Bolléenne vrai si ces deux entiers sont couplés.

DIVISORS = {1: 1}  # Memoization of divisors
SUM_DIVISORS = {1: 1}  # Memoization of sum of divisors


def divisors(n):

    if n in DIVISORS:
        return DIVISORS[n] + [1]

    sqrtN = math.ceil(math.sqrt(n))

    diviseurs = []

    # While the number is not in the memoization
    it = range(sqrtN, math.ceil(n/2)+1, 2 if n % 2 else 1)

    for i in it:

        if n % i == 0:
            diviseurs.append(i)
            diviseurs.append(n//i)
        
        if i > sqrtN:
            break

    DIVISORS[n] = diviseurs

    return diviseurs + [1]

    


def sont_couplés(n, m):

    if not n in SUM_DIVISORS:
        SUM_DIVISORS[n] = sum(divisors(n))

    if SUM_DIVISORS[n] != m:
        return False

    if not m in SUM_DIVISORS:
        SUM_DIVISORS[m] = sum(divisors(m))

    if SUM_DIVISORS[m] != n:
        return False

    return True


# Ecrivez la fonction qui prend en entrée un entier n_max et affiche toutes
# les paires n, m d'entiers couplés pour tout n < n_max.
# Chaque paire ne doit être affichée qu'une seule fois.

def affiche_tous_couplés(n_max):

    n = 0

    for number in range(2, n_max):

        if not number in SUM_DIVISORS:
            SUM_DIVISORS[number] = sum(divisors(number))

        numberDivisors = SUM_DIVISORS[number]
        number2 = numberDivisors

        if number % 2 != number2 % 2:
            continue

        if number2 >= n_max:
            continue

        if not number2 in SUM_DIVISORS:
            SUM_DIVISORS[number2] = sum(divisors(number2))

        if SUM_DIVISORS[number2] == number:

            print(f"{number} and {number2} are coupled.")
            n += 1

    print(n, "pairs found.")


MAX = 500_000

begin = time.time()
affiche_tous_couplés(MAX)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)

# begin = time.time()
# affiche_tous_couplés(10_000)
# print(f"Duration = {time.time() - begin} seconds to complete.")
# print("-"*50)

# begin = time.time()
# affiche_tous_couplés(500_000)
# print(f"Duration = {time.time() - begin} seconds to complete.")
# print("-"*50)
