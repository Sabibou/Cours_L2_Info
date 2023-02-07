# Introduction

## Évaluation

- Individuelle
- TP
- 2h

## Prise de note du 7 Février

### Le système qu'on va utiliser

- On va travailler avec des ==équations binaires== (Vrai / Faux)
- On autorise les ==variables== (valeurs boléennes) : $x_i$
- On va utiliser : $\lnot, \lor$
- On va faire des ==littéraux== : $x_i, \lnot x_i$
  - On va les manipuler avec des $\lor$ : $x_2 \lor x_4 \lor x_5$ (c'est une ==clause==)
  
### Les opérations sur les littéraux

- On peut donner une valeur à une variable : $x_2 = \lnot x_2$ : on dit que $x_2$ est ==assignée==
- Une clause est ==satisfaite== si au moins un de ses littéraux est vrai
- On peut faire un système de clauses :

$$\begin{array}{l}
x_1 \lor x_2 \lor x_3 \\
x_1 \lor \lnot x_2 \lor x_3 \\
\lnot x_1 \lor x_2 \lor x_3 \\
\lnot x_1 \lor \lnot x_2 \lor x_3 \\
\end{array}$$

