package TP3.Exercice1.src;

public abstract class Joueur {

    private String nom;
    protected Paquet paquet;

    public Joueur(String nom) {

        this.nom = nom;

    }
    
    public void nouveauJeu() {

        this.paquet = new Paquet();

    }
    
    public Carte jouer() {
        Carte carte = choisirCarte();
        return carte;
    }

    public abstract Carte choisirCarte();

    public void recupererCarte(Carte carte) {

        this.paquet.ajouter(carte);

    }

    public boolean aPerdu() {
        return this.paquet.estVide();
    }

    @Override
    public String toString() {
        return this.nom;
    }

}