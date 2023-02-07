package TP3.Exercice1.src;

public class Jeu {

    private Joueur humain;
    private Joueur ordinateur;
    private Paquet pioche;

    private int numeroJoueur;

    private Joueur jouerCoup() {
        
        this.numeroJoueur = (this.numeroJoueur + 1) % 2;

        return (numeroJoueur == 1) ? ordinateur : humain;

    }
    
    private void creerNouveauPaquet() {

        pioche = new Paquet();


        for (int i = 1; i <= 13 ; i++) {

            pioche.ajouter(new Carte(i, new Couleur(1).getCouleur()));
            pioche.ajouter(new Carte(i, new Couleur(2).getCouleur()));
            pioche.ajouter(new Carte(i, new Couleur(3).getCouleur()));
            pioche.ajouter(new Carte(i, new Couleur(4).getCouleur()));

        }

    }
    
    private void jouerPartie() {

        creerNouveauPaquet();

        this.pioche.melanger();


        humain = new Ordinateur("Joueur 1");
        ordinateur = new Ordinateur("Joueur 2");

        humain.nouveauJeu();
        ordinateur.nouveauJeu();

        distribuerPaquet();

        while (!humain.aPerdu() && !ordinateur.aPerdu()) {


            Joueur joueurA = jouerCoup();

            Carte carteJoueeA = joueurA.choisirCarte();

            joueurA.paquet.retirer(carteJoueeA);



            Joueur joueurB = jouerCoup();

            Carte carteJoueeB = joueurB.choisirCarte();

            joueurB.paquet.retirer(carteJoueeB);


            if (carteJoueeA.getValeur() > carteJoueeB.getValeur()) {

                joueurA.recupererCarte(carteJoueeA);
                joueurA.recupererCarte(carteJoueeB);
                System.out.printf("%s a récupérer la carte %s.\n", joueurA, carteJoueeB);

            } else if (carteJoueeA.getValeur() < carteJoueeB.getValeur()) {

                joueurB.recupererCarte(carteJoueeA);
                joueurB.recupererCarte(carteJoueeB);
                System.out.printf("%s a récupéré la carte %s.\n", joueurB, carteJoueeA);

            } else {

                joueurA.recupererCarte(carteJoueeA);
                joueurB.recupererCarte(carteJoueeB);
                System.out.println("Égalité !");

            }

            System.out.printf("%s a %d cartes.\n", joueurA, joueurA.paquet.taille());
            System.out.printf("%s a %d cartes.\n", joueurB, joueurB.paquet.taille());

            System.out.println("------------------------");

        }

    }
    
    public void distribuerPaquet() {

        for (int i = 0; i < pioche.taille() / 2; i++) {

            humain.recupererCarte(this.pioche.retirer(0));

        }

        for (int i = 0; i < pioche.taille() / 2; i++) {

            ordinateur.recupererCarte(this.pioche.retirer(0));

        }

    }
    
    public static void main(String[] args) {

        Jeu jeu = new Jeu();

        jeu.jouerPartie();

    }


}
