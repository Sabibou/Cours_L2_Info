package TP2.Exercice2.src;

public class Main {
    
    public static void main(String[] args) {
        
        String entreeUser = System.console().readLine("Entrez un mot: ");

        Mot mot = new Mot(entreeUser);

        mot.afficheVoyelles();

        String entreeUser2 = System.console().readLine("Entrez un autre mot: ");

        Mot mot2 = new Mot(entreeUser2);

        System.out.println(mot2.estPalindrome());

        System.out.println(mot.estContenu(mot2));

        System.out.println(mot2.trieMot());

    }

}
