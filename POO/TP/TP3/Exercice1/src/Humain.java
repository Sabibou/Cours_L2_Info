package TP3.Exercice1.src;

public class Humain extends Joueur {
    
    public Humain(String nom) {
        super(nom);
    }
    
    @Override
    public Carte choisirCarte() {
        
        System.out.println("Vos cartes : ");

        System.out.println(this.paquet.toString());
        
        int numCarte = -1;

        do {

            try {
                numCarte = Integer.parseInt(System.console().readLine("Entrez le numéro de la carte : "));
            } catch (NumberFormatException e) {
                System.out.println("Veuillez rentrer un nombre.");
                numCarte = -1;
            }

            if (numCarte < 0 || numCarte >= paquet.taille()) {
                
                System.out.printf("Veuillez rentrer un nombre entre 0 et %d.\n", paquet.taille());
                numCarte = -1;

            }

        } while(numCarte < 0 || numCarte >= paquet.taille());

        Carte carte = paquet.get(numCarte);

        return carte;

    }

}
