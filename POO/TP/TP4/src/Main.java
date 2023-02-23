package TP4.src;

public class Main {
    
    public static void main(String[] args) {
        
        // ------------------------ Exercice 1 ------------------------
        // Matrice matrice1 = new Matrice(3, 3);
        // Matrice matrice2 = new Matrice(3, 3);
        
        // matrice1.remplirMatrice();
        // matrice2.remplirMatrice();
        
        // matrice1.afficheMatrice();
        // System.out.println();
        // matrice2.afficheMatrice();
        // System.out.println();
        
        // Matrice matriceResultat = matrice1.addition(matrice2);
        // matriceResultat.afficheMatrice();
        // System.out.println();
        
        // matriceResultat = matrice1.multiplication(matrice2);
        // matriceResultat.afficheMatrice();
        // System.out.println();

        // Matrice triangulaire = Matrice.matriceTriangulaire(3);
        // triangulaire.afficheTriangulaire();

        // ------------------------ Exercice 2 ------------------------
        Liste liste = new Liste();

        liste.ajouter(1);
        liste.ajouter(2);
        liste.ajouter(3);

        liste.afficher();

        liste.reverse();
        liste.afficher();

    }

}
