---
title: TD 2 Implémentation BDD
author: VAN DE MERGHEL Robin
date: 2023
lang: fr
geometry: margin=2cm
---

# Exercice 1

> **Considérons les deux transactions suivantes :**
> `T1 : READ(A,t) ; t := t+2 ; WRITE(A,t) ; READ(B,t) ; t=t*3 ; WRITE(B,t) ; COMMIT`
> `T2 : READ(B,s) ; s := s*2 ; WRITE(B,s) ; READ(A,s) ; s=s+3 ; WRITE(A,s) ; COMMIT`


## Question 1

> **Donner les plans correspondant aux exécutions en série $(T_1,T_2)$ et $(T_2,T_1)$**

Avc $(T_1, T_2)$ :

| $T_1$ | $T_2$ | A | B |
|-------|-------|---|---|
| $r(A, t)$ | | $a$ | |
| $t:=t+2$ | | $a$ | |
| $w(A, t)$ | | $a+2$ | |
| $r(B, t)$ | | $a+2$ | $b$ |
| $t:=t\times 3$ | | $a+2$ | $b$ |
| $w(B, t)$ | | $a+2$ | $b\times 3$ |
| $commit$ | | $a+2$ | $b\times 3$ |
| | $r(B, s)$ | $a+2$ | $b\times 3$ |
| | $s:=s\times 2$ | $a+2$ | $b\times 3$ |
| | $w(B, s)$ | $a+2$ | $b\times 6$ |
| | $r(A, s)$ | $a+2$ | $b\times 6$ |
| | $s:=s+3$ | $a+2$ | $b\times 6$ |
| | $w(A, s)$ | $a+5$ | $b\times 6$ |
| | $commit$ | $a+5$ | $b\times 6$ |


État final : $A = a+5$ et $B = b\times 6$

Avec $(T_2, T_1)$ :

| $T_2$ | $T_1$ | A | B |
|-------|-------|---|---|
| $r(B, s)$ | |  | $b$ |
| $s:=s\times 2$ | |  | $b$ |
| $w(B, s)$ | |  | $b\times 2$ |
| $r(A, s)$ | | $a$ | $b\times 2$ |
| $s:=s+3$ | | $a$ | $b\times 2$ |
| $w(A, s)$ | | $a + 3$ | $b\times 2$ |
| $commit$ | | $a + 3$ | $b\times 2$ |
| | $r(A, t)$ | $a + 3$ | $b\times 2$ |
| | $t:=t+2$ | $a + 3$ | $b\times 2$ |
| | $w(A, t)$ | $a + 5$ | $b\times 2$ |
| | $r(B, t)$ | $a + 5$ | $b\times 2$ |
| | $t:=t\times 3$ | $a + 5$ | $b\times 2$ |
| | $w(B, t)$ | $a + 5$ | $b\times 6$ |
| | $commit$ | $a + 5$ | $b\times 6$ |

État final : $A = a+5$ et $B = b\times 6$


## Question 2

> **Montrer que les exécutions $(T_1,T_2)$ et $(T_2,T_1)$ sont équivalentes, en commençant sur un exemple de base de données initial.**


On a les deux mêmes états finaux, donc les deux exécutions sont équivalentes.

## Question 3

> **Donner l'exemple d'une exécution de $T_1$ et de $T_2$ qui fait appraître un problème de lectures impropres.**

Avec $(T_1, T_2)$ :


| $T_1$ | $T_2$ | A | B |
|-------|-------|---|---|
| $r(A, t)$ | | $a$ | |
| $t:=t+2$ | | $a$ | |
| $w(A, t)$ | | $a+2$ | |
| $r(B, t)$ | | $a+2$ | $b$ |
| $t:=t\times 3$ | | $a+2$ | $b$ |
| | $r(B, s)$ | $a+2$ | $b$ |
| | $s:=s\times 2$ | $a+2$ | $b$ |
| | $w(B, s)$ | $a+2$ | $b\times 2$ |
| | $r(A, s)$ | $a+2$ | $b\times 2$ |
| | $s:=s+3$ | $a+2$ | $b\times 2$ |
| | $w(A, s)$ | $a+5$ | $b\times 2$ |
| $w(B, t)$ | | $a+5$ | $b\times 2$ |
| $commit$ | | $a+5$ | $b\times 2$ |
| | $commit$ | $a+5$ | $b\times 2$ |


On a $a+3$ dans $A$, modifié par $T_2$, alors que $T_1$ n'a pas encore commit.


## Question 4

> **Donner l'exemple d'une exécution de $T_1$ et de $T_2$ qui fait appraître un problème de perte de mise à jour.**


Avec $(T_1, T_2)$ :

| $T_1$ | $T_2$ | A | B |
|-------|-------|---|---|
| $r(A, t)$ | | $a$ | |
| $t:=t+2$ | | $a$ | |
| $w(A, t)$ | | $a+2$ | |
| $r(B, t)$ | | $a+2$ | $b$ |
| $t:=t\times 3$ | | $a+2$ | $b$ |
| | $r(B, s)$ | $a+2$ | $b$ |
| | $s:=s\times 2$ | $a+2$ | $b$ |
| | $w(B, s)$ | $a+2$ | $b\times 2$ |
| | $r(A, s)$ | $a+2$ | $b\times 2$ |
| | $s:=s+3$ | $a+2$ | $b\times 2$ |
| | $w(A, s)$ | $a+5$ | $b\times 2$ |
| $w(B, t)$ | | $a+5$ | $b\times 2$ |
| $commit$ | | $a+5$ | $b\times 2$ |
| | $commit$ | $a+5$ | $b\times 2$ |


On a $a+3$ dans $A$, modifié par $T_2$, alors que $T_1$ n'a pas encore commit.


# Exercice 2

> **Considérons les deux transactions suivantes :**
> `T1 : r1(a) w1(a) w1(b) r1(b) commit1`
> `T2 : r2(b) w2(b) r2(a) w2(a) commit2`


## Question 1

> **Donner trois exécutions sérialisables de $T_1$ et $T_2$.**

On a :

$$E_1 = (T_1, T_2) = r_1(a) \ w_1(a) \ w_1(b) \ r_1(b) \ r_2(b) \ w_2(b) \ r_2(a) \ w_2(a) \ commit_1 \ commit_2$$

| $T_1$ | $T_2$ |
|-------|-------|
| $r_1(A)$ | |
| $w_1(A)$ | |
| $w_1(B)$ | |
| $r_1(B)$ | |
| $commit_1$ | |
| | $r_2(B)$ |
| | $w_2(B)$ |
| | $r_2(A)$ |
| | $w_2(A)$ |
| | $commit_2$ |


On a :

$$E_2 = (T_2, T_1) = r_2(b) \ w_2(b) \ r_2(a) \ w_2(a) \ r_1(a) \ w_1(a) \ w_1(b) \ r_1(b) \ commit_2 \ commit_1$$

| $T_2$ | $T_1$ |
|-------|-------|
| $r_2(B)$ | |
| $w_2(B)$ | |
| $r_2(A)$ | |
| $w_2(A)$ | |
| $commit_2$ | |
| | $r_1(A)$ |
| | $w_1(A)$ |
| | $w_1(B)$ |
| | $r_1(B)$ |
| | $commit_1$ |

On a aussi :

| $T_1$ | $T_2$ |
|-------|-------|
| $r_1(A)$ | |
| $w_1(A)$ | |
| $commit_1$ | |
| | $r_2(B)$ |
| | $w_2(B)$ |
| | $commit_2$ |
| $w_1(B)$ | |
| $r_1(B)$ | |
| $commit_1$ | |
| | $r_2(A)$ |
| | $w_2(A)$ |
| | $commit_2$ |

Équivalent à :

$$E = r_1(a) \ w_1(a) \ commit_1 \ r_2(b) \ w_2(b) \ commit_2 \ w_1(b) \ r_1(b) \ commit_1 \ r_2(a) \ w_2(a) \ commit_2$$

