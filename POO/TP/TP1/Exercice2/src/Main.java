package TP1.Exercice2.src;

import java.util.Random;


public class Main {

    public static void main(String[] args) {

        int nb1 = 0;
        int nb2 = 0;

        try {

            nb1 = Integer.parseInt(args[0]);
            nb2 = Integer.parseInt(args[1]);

        } catch (ArrayIndexOutOfBoundsException e) {

            throw new IllegalArgumentException("Vous devez saisir deux nombres en paramètres");

        } catch (NumberFormatException e) {

            throw new IllegalArgumentException("Vous devez saisir des nombres en paramètres");

        }

        new Main().run(nb1, nb2);

    }
    
    public void run(int nb1, int nb2) {


        if (nb1 > nb2) {

            throw new IllegalArgumentException("Le premier nombre doit être inférieur au second");

        }

        // Utilisation de nextInt pour générer un nombre aléatoire entre nb1 et nb2
        Random random = new Random();
        int randomInt = random.nextInt(nb2 - nb1 + 1) + nb1;

        int guess = -randomInt; // Valeur initiale différente de randomInt

        while (guess != randomInt) {

            System.out.println("Quel est le nombre à trouver ? ");

            try {

                guess = Integer.parseInt(System.console().readLine());

                if (guess < randomInt) {

                    System.out.println("Le nombre à trouver est plus grand");

                } else if (guess > randomInt) {

                    System.out.println("Le nombre à trouver est plus petit");

                }

            } catch (ArrayIndexOutOfBoundsException e) {

                System.out.println("Vous devez saisir un nombre en paramètre");

            } catch (NumberFormatException e) {

                System.out.println("Vous devez saisir un nombre en paramètre");

            }

        }

        System.out.println("Bravo, vous avez trouvé le nombre à trouver");

    }

}
