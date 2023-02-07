
package TP3.Exercice1.src;

class Carte implements Comparable<Carte> {

    /*
     * 1 = 1
     * ...
     * 10 = 10
     * 11 = Valet
     * 12 = Dame
     * 13 = Roi
     * 14 = As
     * 
     */
    public final String[] VALEURS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"};

    private int valeur;
    private String couleur;

    public Carte(int valeur, String couleur) {

        if (couleur != "Coeur" && couleur != "Carreau" && couleur != "Pique" && couleur != "Trèfle") {
            throw new IllegalArgumentException("La couleur de la carte doit être Coeur, Carreau, Pique ou Trèfle");
        }

        if (valeur < 1 || valeur > 14) {
            throw new IllegalArgumentException("La valeur de la carte doit être comprise entre 1 et 14");
        }

        this.valeur = valeur;
        this.couleur = couleur;

    }

    @Override
    public String toString() {

        return VALEURS[this.valeur] + " - " + this.couleur;

    }

    @Override
    public int compareTo(Carte o) {

        if (this.valeur > o.valeur) {
            return 1;
        } else if (this.valeur < o.valeur) {
            return -1;
        }

        return 0;
    }
    
    public int getValeur() {

        return this.valeur;

    }

    

}