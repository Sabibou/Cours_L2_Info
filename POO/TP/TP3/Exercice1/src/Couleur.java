package TP3.Exercice1.src;

public class Couleur {
    
    private String couleur;

    public Couleur(int valeur) {

        if (valeur < 1 || valeur > 14) {
            throw new IllegalArgumentException("La valeur de la carte doit être comprise entre 1 et 14");
        }

        this.couleur = null;

        switch (valeur) {
            case 1:
                this.couleur = "Coeur";
                break;
            case 2:
                this.couleur = "Carreau";
                break;
            case 3:
                this.couleur = "Pique";
                break;
            case 4:
                this.couleur = "Trèfle";
                break;
            default:
                break;
        }

    }

    public String getCouleur() {

        return this.couleur;

    }

}
