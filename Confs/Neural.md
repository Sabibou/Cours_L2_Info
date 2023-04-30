# Introduction

L'intelligence artificielle avec réseau de neurones provient d'une discussion entre un neuro-biologiste et un mathématicien. 

On peut essayer de simuler le cerveau humain en utilisant des réseaux de neurones artificiels.

# Réseaux de neurones

On peut représenter un réseau de neurones par un graphe orienté. Les neurones sont les sommets et les connexions entre les neurones sont les arêtes.

On a attaché à chaque paire de neurones un poids noté $w_{ij}$ qui représente la force de la connexion entre les neurones $i$ et $j$.

On a donc une fonction $y=f_w(x)$.

On règle ces poids pour que à partir de notre entrée $x$, on obtienne la sortie $y$ désirée. C'est de l'apprentissage supervisé.

# Données

Pour l'apprentissage, on peut utiliser des données réelles ou des données simulées.

On peut avoir des données brutes (un chien, un chat) ou des données sémantiques (un chat qui boit du lait).