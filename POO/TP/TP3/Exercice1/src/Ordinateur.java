package TP3.Exercice1.src;

import java.util.Random;

public class Ordinateur extends Joueur {

    public Ordinateur(String nom) {
        super(nom);
    }

    @Override
    public Carte choisirCarte() {

        int min = 0;
        int max = this.paquet.taille() - 1;

        Random random = new Random();
        int randomInt = random.nextInt(max - min + 1) + min;
        
        
        return this.paquet.get(randomInt);
    }


}
