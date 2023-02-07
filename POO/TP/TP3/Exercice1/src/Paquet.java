package TP3.Exercice1.src;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Paquet {
    
    private List<Carte> paquet;
    private int indexMin;

    public Paquet() {
        this.paquet = new ArrayList<Carte>();
        this.indexMin = 0;
    }

    public void ajouter(Carte carte) {

        if (indexMin >= 52) {
            
            throw new IllegalArgumentException("Le paquet est déjà plein.");

        }

        this.paquet.add(carte);
        indexMin++;

    }

    public int taille() {

        return this.indexMin;

    }

    public boolean estVide() {

        return this.indexMin == 0;

    }

    public Carte retirer(Carte carte) {

        if (indexMin >= 52) {

            throw new IllegalArgumentException("Le paquet est déjà plein.");

        };

        this.paquet.remove(carte);

        indexMin--;

        return carte;

    }

    public Carte retirer(int carte) {

        if (carte >= 52 || carte < 0) {

            throw new IllegalArgumentException("Indexe invalide.");

        }

        Carte carteRetiree = this.paquet.get(carte);

        this.paquet.remove(carteRetiree);

        indexMin--;

        return carteRetiree;

    }
    
    @Override
    public String toString() {

        String text = "";

        int i = 0;

        for (Carte carte : this.paquet) {

            text += i + " - " + carte.toString() + "\n";
            i++;

        }

        return text;

    }

    public Carte get(int index) {

        if (index < 0 || index >= this.paquet.size()) {

            throw new IllegalArgumentException("Indexe invalide.");

        }

        return this.paquet.get(index);

    }

    public void melanger() {
        int x = 2 * this.paquet.size();

        int min = 0;
        int max = this.paquet.size() - 1;

        Random random = new Random();

        for (int i = 0; i < x; i++) {

            int randomInt = 0;
            int randomInt2 = 0;

            do {

                randomInt = random.nextInt(max - min + 1) + min;
                randomInt2 = random.nextInt(max - min + 1) + min;

            } while (randomInt == randomInt2);

            Collections.swap(this.paquet, randomInt, randomInt2);

        }
        
    }

}
