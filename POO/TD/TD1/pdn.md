# Exercice 1

# 1.1

- Un instant est un point dans le temps. Il ne peut pas changé. Il est donc immuable. On préfèrera aussi ne pas pouvoir le modifier pour comparer par valeur et non par référence.

- Pour lire les valeurs d'un instant, on doit pouvoir récupérer les valeurs de ses attributs avec des accesseurs.
   
- Comme un instant est immuable, on ne peut pas le modifier. On peut donc pas avoir de mutateurs.


# 1.2

Une interprétation en Java de la classe `Instant` serait la suivante :

*Note : Les setters sont déconseillés en Java (de les avoir en public), donc on les met en privé*

<details>
<summary>Classe de InstantTD</summary>

```java
class Instant {

    private int heures; // 0 <= heure < 24
    private int minutes; // 0 <= minute < 60
    private int secondes; // 0 <= seconde < 60

    // Constructeur
    Instant(int heures, int minutes, int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this.setHeures(heures);
        this.setMinutes(minutes);
        this.setSecondes(secondes);

    }

    // Getters
    public int getHeures() {
        return this.heures;
    }
    
    public int getMinutes() {
        return this.minutes;
    }
    
    public int getSecondes() {
        return this.secondes;
    }
    
    
    // Setters
    private void setHeures(int heures) {

        // Regarde si les heures sont valides
        if (0 > heures || heures >= 24) {
            throw new IllegalArgumentException("Heures invalides");
        }

        this.heures = heures;
    }
    
    private void setMinutes(int minutes) {

        // Regarde si les minutes sont valides
        if (0 > minutes || minutes >= 60) {
            throw new IllegalArgumentException("Minutes invalides");
        }

        this.minutes = minutes;
    }
    
    private void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (0 > secondes || secondes >= 60) {
            throw new IllegalArgumentException("Secondes invalides");
        }

        this.secondes = secondes;
    }
    
    public String stringify() {

        return String.format("%02d:%02d:%02d",
                this.getHeures(),
                this.getMinutes(),
                this.getSecondes());
    }
    
    public String toString() {
        return this.stringify();
    }

}
```

</details>

On propose une deuxième façon de coder `Instant`, avec seulement des secondes :

<details>

<summary>Classe de InstantTD2</summary>

```java
class Instant2 {

    private int secondes;
    private static final int SECONDES_PAR_HEURE = 3600;
    private static final int SECONDES_PAR_MINUTE = 60;
    private static final int SECOND_MAX = SECONDES_PAR_HEURE * 24;
    private static final int SECOND_MIN = 0;

    // Constructeur
    Instant2(int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this.setSecondes(secondes);

        // Permet d'utiliser des secondes seulement plutôt que des heures, minutes et secondes

    }

    Instant2(int heures, int minutes, int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this(heures * SECONDES_PAR_HEURE + minutes * SECONDES_PAR_MINUTE + secondes);

    }

    // Getters
    public int getHeures() {
        return this.secondes / SECONDES_PAR_HEURE;
    }

    public int getMinutes() {
        return (this.secondes / SECONDES_PAR_MINUTE) % SECONDES_PAR_MINUTE;
    }

    public int getSecondes() {
        return this.secondes % SECONDES_PAR_MINUTE;
    }


    // Setters
    private void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (SECOND_MIN >= secondes || secondes >= SECOND_MAX) {
            throw new IllegalArgumentException("Secondes invalides");
        }

        this.secondes = secondes;
    }

    public String stringify() {

        return String.format("%02d:%02d:%02d",
                this.getHeures(),
                this.getMinutes(),
                this.getSecondes());
    }

    public String toString() {
        return this.stringify();
    }

}
```

</details>

Une troisième façon, avec une création par une fonction statique :

<details>

<summary>Classe de InstantTD3</summary>

```java
class Instant3 {

    private int secondes;
    private static final int SECONDES_PAR_HEURE = 3600;
    private static final int SECONDES_PAR_MINUTE = 60;
    private static final int SECOND_MAX = SECONDES_PAR_HEURE * 24;
    private static final int SECOND_MIN = 0;


    public static Instant3 from(int heures, int minutes, int secondes) {
        return new Instant3(heures * SECONDES_PAR_HEURE + minutes * SECONDES_PAR_MINUTE + secondes);
    }

    public static Instant3 from(int secondes) {
        return new Instant3(secondes);
    }

    // Mettre en privé pour appeler par une méthode statique
    private Instant3(int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this.setSecondes(secondes);

        // Permet d'utiliser des secondes seulement plutôt que des heures, minutes et secondes

    }

    // Getters
    public int getHeures() {
        return this.secondes / SECONDES_PAR_HEURE;
    }

    public int getMinutes() {
        return (this.secondes / SECONDES_PAR_MINUTE) % SECONDES_PAR_MINUTE;
    }

    public int getSecondes() {
        return this.secondes % SECONDES_PAR_MINUTE;
    }

    // Setters
    private void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (SECOND_MIN >= secondes || secondes >= SECOND_MAX) {
            throw new IllegalArgumentException("Secondes invalides");
        }

        this.secondes = secondes;
    }

    public String stringify() {

        return String.format("%02d:%02d:%02d",
                this.getHeures(),
                this.getMinutes(),
                this.getSecondes());
    }

    public String toString() {
        return this.stringify();
    }

}
```


</details>

## Exercice 2

On implémente la fonction `minus` qui permet de soustraire deux instants. On peut utiliser soit :

- `minus(Instant i)` pour soustraire un `Instant` à l'`Instant` courant
  - On utilise `this` pour accéder à l'`Instant` courant
- `minus(Instant i1, Instant i2)` pour soustraire un `Instant` à un autre `Instant`
  - Une fonction statique, on utilise `Instant` pour accéder à la classe

Les deux méthodes :

<details>

<summary>`minus` avec `instant1, instant2`</summary>

```java
    public static Instant minus(Instant instant1, Instant instant2) {

        // On convertit les 2 instants en secondes
        int secondes1 = instant1.getHeures() * 3600 + instant1.getMinutes() * 60 + instant1.getSecondes();
        int secondes2 = instant2.getHeures() * 3600 + instant2.getMinutes() * 60 + instant2.getSecondes();

        // On calcule la différence
        int difference = secondes1 - secondes2;

        // On convertit la différence en heures, minutes et secondes
        int heures = difference / 3600;
        int minutes = (difference % 3600) / 60;
        int secondes = (difference % 3600) % 60;

        // On retourne un nouvel instant
        return new Instant(heures, minutes, secondes);

    }
```

</details>



<details>

<summary>`minus` avec this</summary>

```java

    
    public static Instant minus(Instant instant) {
        
        int secondes1 = this.getHeures() * 3600 + this.getMinutes() * 60 + this.getSecondes();
        int secondes2 = instant.getHeures() * 3600 + instant.getMinutes() * 60 + instant.getSecondes();

        int difference = secondes1 - secondes2;
        
        int heures = difference / 3600;
        int minutes = (difference % 3600) / 60;

        // On retourne un nouvel instant
        return new Instant(heures, minutes, difference % 60);

    }
```

</details>

La version avec `this` est préférable car on peut l'utiliser avec un `Instant` déjà existant.

