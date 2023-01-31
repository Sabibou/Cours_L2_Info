# Question 4

Le flag `-d` de la commande `javac` permet de spécifier le répertoire de travail de l'application. 

Rajouter `package poo.tp.premierspas;` permet de spécifier le package de l'application. Au moment du *build*, le compilateur va chercher les classes dans le répertoire `poo/tp/premierspas` (en fonction du flag `-d`).

Le flag `-cp` de la commande `java` permet de spécifier le répertoire où se trouvent les classes à charger.

Si je viens d'exectuer `javac -d build src/*.java`, avec le fichier `Hello.java` dans le répertoire `src` qui contient le code suivant:

```java
package poo.tp.premierspas;

class main {
    public static void main(String[] args) {
        System.out.println("Hello " + args[0] + " !");
    }
}
```

Je peux exécuter l'application avec la commande suivante:

```bash
java -cp build poo.tp.premierspas.main "World"
```