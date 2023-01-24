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


def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor



def sont_couplés(n, m):
    
    return sum(divisors(n)) == m and sum(divisors(m)) == n


print(sont_couplés(9, 88))
print(sont_couplés(7, 7))

# Ecrivez la fonction qui prend en entrée un entier n_max et affiche toutes
# les paires n, m d'entiers couplés pour tout n < n_max.
# Chaque paire ne doit être affichée qu'une seule fois.

def affiche_tous_couplés(n_max):

    explored_pairs = []

    for number in range(1, n_max):
        
        for number2 in range(1, n_max):

            if number != number2:

                smaller_number = min(number, number2)
                bigger_number = max(number, number2)

                if (smaller_number, bigger_number) not in explored_pairs:

                    if sont_couplés(number, number2):
                            
                        explored_pairs.append((smaller_number, bigger_number))
                        print(f"{smaller_number} and {bigger_number} are coupled.")

                
MAX = 100000

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
