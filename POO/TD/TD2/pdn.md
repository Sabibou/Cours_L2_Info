# TD2

## Exercice 1


### Question 1

<!-- Une voiture de type A est constituée d’un moteur, d’une carrosserie et de quatre roues. La carrosserie est constituée de portes, dont le nombre peut varier entre 2 et 4. 
Proposez un diagramme de classes pour les voitures A.
-->

```dot
digraph {
    rankdir=LR;
    node [shape=rectangle];
    edge [arrowhead=normal, arrowtail=diamond];

    Voiture[label="Voiture A"]

    Voiture -> Moteur[label="1"];
    Voiture -> Carrosserie[label="1"];
    Voiture -> Roue[label="4"];

    Carrosserie -> Porte[label="2..4"];
}
```

### Question 2

<!-- Les voitures de type B sont constituées de deux moteurs (l’un à l’avant et l’autre à l’arrière), d’une carrosserie et de six roues. La carrosserie est constituée de portes, dont le nombre peut varier entre 2 et 4. -->

```dot
digraph {
    rankdir=LR;
    node [shape=rectangle];
    edge [arrowhead=normal, arrowtail=diamond];
    
    Voiture1[label="Voiture A"];
    Voiture2[label="Voiture B"];

    Voiture1 -> Moteur[label="1"];
    Voiture1 -> Carrosserie[label="1"];
    Voiture1 -> Roue[label="4"];

    Voiture2 -> Moteur[label="2"];
    Voiture2 -> Carrosserie[label="1"];
    Voiture2 -> Roue[label="6"];

    Carrosserie -> Porte[label="2..4"];
}
```

On fait un type abstrait `Voiture`.

```dot
digraph {
    rankdir=LR;
    node [shape=rectangle];
    edge [arrowhead=normal, arrowtail=diamond];

    Voiture[label="Voiture"];

    Voiture -> Moteur[label="1"];
    Voiture -> Carrosserie[label="1"];
    Voiture -> Roue[label="4..6"];

    Carrosserie -> Porte[label="2..4"];
}
```
