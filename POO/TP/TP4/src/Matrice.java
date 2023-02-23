package TP4.src;

public class Matrice {
    
    private float[][] matrice;
    private int nbLignes;
    private int nbColonnes;

    public Matrice(int nbLignes, int nbColonnes) {
        this.nbLignes = nbLignes;
        this.nbColonnes = nbColonnes;
        this.matrice = new float[nbLignes][];
    }

    public Matrice(int taille) {
        this.nbLignes = taille;
        this.nbColonnes = taille;
        this.matrice = new float[taille][];
    }

    public void afficheMatrice() {
        for (int i = 0; i < this.nbLignes; i++) {
            for (int j = 0; j < this.nbColonnes; j++) {
                System.out.print(this.matrice[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public void remplirMatrice() {
        for (int i = 0; i < this.nbLignes; i++) {

            this.matrice[i] = new float[this.nbColonnes];

            for (int j = 0; j < this.nbColonnes; j++) {
                this.matrice[i][j] = (int) (Math.random() * 10);
            }
        }
    }

    public void remplirMatriceZero() {
        for (int i = 0; i < this.nbLignes; i++) {

            this.matrice[i] = new float[this.nbColonnes];

            for (int j = 0; j < this.nbColonnes; j++) {
                this.matrice[i][j] = 0;
            }
        }
    }

    Matrice addition(Matrice matrice) {
        Matrice matriceResultat = new Matrice(this.nbLignes, this.nbColonnes);
        matriceResultat.remplirMatriceZero();


        for (int i = 0; i < this.nbLignes; i++) {
            for (int j = 0; j < this.nbColonnes; j++) {
                matriceResultat.matrice[i][j] = this.matrice[i][j] + matrice.matrice[i][j];
            }
        }

        return matriceResultat;
    }

    Matrice multiplication(Matrice matrice) {
        Matrice matriceResultat = new Matrice(this.nbLignes, this.nbColonnes);
        matriceResultat.remplirMatriceZero();

        for (int i = 0; i < this.nbLignes; i++) {
            for (int j = 0; j < this.nbColonnes; j++) {
                matriceResultat.matrice[i][j] = this.matrice[i][j] * matrice.matrice[i][j];
            }
        }

        return matriceResultat;
    }

    Matrice multiplication(float alpha) {
        Matrice matriceResultat = new Matrice(this.nbLignes, this.nbColonnes);
        matriceResultat.remplirMatriceZero();

        for (int i = 0; i < this.nbLignes; i++) {
            for (int j = 0; j < this.nbColonnes; j++) {
                matriceResultat.matrice[i][j] = this.matrice[i][j] * alpha;
            }
        }

        return matriceResultat;
    }

    public static Matrice matriceTriangulaire(int taille) {

        // On crée un tableau avec taille lignes et le nombre de colonnes est 1, 2, 3, ..., taille
        Matrice matriceResultat = new Matrice(taille);

        for (int i = 0; i < taille; i++) {

            matriceResultat.matrice[i] = new float[i + 1];

            for (int j = 0; j < i + 1; j++) {
                matriceResultat.matrice[i][j] = 0;
            }

        }

        return matriceResultat;

    }
    
    public void afficheTriangulaire() {
        for (int i = 0; i < this.nbLignes; i++) {

            for (int j = 0; j < i + 1; j++) {
                System.out.print(this.matrice[i][j] + "\t");
            }

            System.out.println();
        }
    }
    


}
