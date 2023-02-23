import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * main
 */
class Main {

    /**
     * main
     */
    public static void main(String[] args) {

        // ------------------------- Information utiles -----------------
        // [ VOUS POUVEZ DÉCOMMENTER LES LIGNES CI-DESSOUS POUR TESTER VOTRE CODE AVEC `CTRL /` DANS VISUAL STUDIO CODE ]

        // ------------------------- Question 2 -------------------------
        // // Création d'une instance
        // Instant2 instant = new Instant2(12, 30, 0);

        // // Print
        // System.out.println(instant);

        // Instant3 instant2 = Instant3.from(12, 30, 0);

        // // Print
        // System.out.println(instant2);

        // ------------------------- Question 3 -------------------------

        // // On fait deux instant que l'on va soustraire
        // Instant i1 = new Instant(12, 30, 0);
        // Instant i2 = new Instant(10, 30, 0);

        // // On soustrait les deux instants
        // Instant minus1 = Instant.minus(i1, i2);
        // Instant minus2 = i1.minus(i2);

        // System.out.println(minus1);
        // System.out.println(minus2);

        // ------------------------- Question 4 -------------------------

        // On compare deux instants
        // Instant i1 = new Instant(12, 30, 0);
        // Instant i2 = new Instant(10, 30, 0);

        // // On affiche le résultat de la comparaison
        // System.out.println(i1.compareTo(i2));

        // Instant i3 = new Instant(10, 30, 0);
        // Instant i4 = new Instant(10, 30, 0);
        // // Méthodes pour comparer :
        // System.out.println(i3.compareTo(i4) == 0); // true
        // System.out.println(i3.equals(i4)); // false (maintenant true car on a redéfini equals)    
        // System.out.println(i3 == i4); // false
        // System.out.println(i3.hashCode() == i4.hashCode()); // true

        // On a bien true pour le premier car on compare terme à terme
        // On a false pour les deux autres car on compare les références

        // On peut redéfinir la méthode equals pour qu'elle compare les instants correctement (comme on le voudrait)
        // Equals prend en paramètre un objet, non pas un Instant
        // PS : On peut avoir A == B et B != A si A et B ne sont pas de la même classe

        // ------------------------- Question 5 -------------------------

        // // On créer un tableau d'instants
        // Instant[] instants = new Instant[3];

        // Random random = new Random();

        // int randomHour;
        // int randomMinute;
        // int randomSecond;

        // // On ajoute des instants
        // for (int i = 0; i < instants.length; i++) {
        //     // On ajoute aléatoirement des instants
        //     randomHour = random.nextInt(24);
        //     randomMinute = random.nextInt(60);
        //     randomSecond = random.nextInt(60);

        //     instants[i] = new Instant(randomHour, randomMinute, randomSecond);
        // }

        // // On affiche les instants
        // for (Instant instant : instants) {

        //     System.out.printf("Instant : %s \n", instant);

        // }

        // // On fait toutes les combinaisons possibles
        // for (int i = 0; i < instants.length; i++) {
        //     for (int j = 0; j < instants.length; j++) {
        //         // On affiche le résultat de la comparaison
        //         System.out.printf("Comparaison de %s et %s : %d%n", instants[i], instants[j],
        //                 instants[i].compareTo(instants[j]));
        //     }
        // }

        // ------------------------- Question 6 -------------------------

        // List<Instant> instants = new ArrayList<>();

        // Random random = new Random();

        // int randomHour;
        // int randomMinute;
        // int randomSecond;

        // int n = 4;

        // // On ajoute des instants
        // for (int i = 0; i < n; i++) {
        //     // On ajoute aléatoirement des instants
        //     randomHour = random.nextInt(24);
        //     randomMinute = random.nextInt(60);
        //     randomSecond = random.nextInt(60);

        //     instants.add(new Instant(randomHour, randomMinute, randomSecond));
        // }

        // // On affiche les instants
        // for (Instant instant : instants) {

        //     System.out.printf("Instant : %s \n", instant);

        // }

        // // On retourne le plus petit instant strictement supérieur à un instant t donné en paramètre
        // Instant t = new Instant(12, 30, 0);

        // Instant result = Instant.getSmallestInstant(t, instants);

        // System.out.printf("Le plus petit instant strictement supérieur à %s est %s", t, result);

        // ------------------------- Question 7 -------------------------


        List<Instant> instants = new ArrayList<>();

        Random random = new Random();

        int randomHour;
        int randomMinute;
        int randomSecond;

        int n = 4;

        // On ajoute des instants
        for (int i = 0; i < n; i++) {
            // On ajoute aléatoirement des instants
            randomHour = random.nextInt(24);
            randomMinute = random.nextInt(60);
            randomSecond = random.nextInt(60);

            instants.add(new Instant(randomHour, randomMinute, randomSecond));
        }

        // On affiche les instants
        for (Instant instant : instants) {

            System.out.printf("Instant : %s \n", instant);

        }


        System.out.println("--------------");


        // On trie les instants
        Instant.sort(instants);

        // On affiche les instants
        for (Instant instant : instants) {

            System.out.printf("Instant : %s \n", instant);

        }

    }

}