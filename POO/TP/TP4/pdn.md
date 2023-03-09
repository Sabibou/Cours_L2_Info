# TP 4

## Exercice 2

### Question 1

On peut ajouter des nombres dans un `ArrayList` de la manière suivante :

```java
ArrayList<Integer> list = new ArrayList<Integer>();
list.add(1);
list.add(2);
list.add(3);
```

On peut récupérer les valeurs entières d'un `ArrayList` de la manière suivante :

```java
int a = list.get(0);
int b = list.get(1);
int c = list.get(2);
```

# Exercice 3

## Question 2

Comme on marche avec des types génériques, on ne peut pas avoir de fonction `put(K key, int value)`. Il faudrait cast de `int` vers `V`.

On pourrait vérifier que c'est un `int` avec `instanceof`.

