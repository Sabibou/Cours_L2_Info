package TP4.src;

class Liste {
    private int[] liste;
    private int nbElements;

    public Liste() {
        this.liste = new int[10];
        this.nbElements = 0;
    }

    public Liste(int taille) {
        this.liste = new int[taille];
        this.nbElements = 0;
    }

    public Liste(Liste liste) {
        this.liste = new int[liste.liste.length];
        this.nbElements = liste.nbElements;

        for (int i = 0; i < liste.nbElements; i++) {

            this.liste[i] = liste.liste[i];
        
        }
    }

    public Liste(int[] liste) {
        this.liste = new int[liste.length];
        this.nbElements = liste.length;

        for (int i = 0; i < liste.length; i++) {
        
            this.liste[i] = liste[i];
        
        }
    }

    public void ajouter(int element) {
        if (this.nbElements == this.liste.length) {

            int[] listeTemp = new int[this.liste.length * 2];

            for (int i = 0; i < this.liste.length; i++) {

                listeTemp[i] = this.liste[i];

            }

            this.liste = listeTemp;
        
        }

        this.liste[this.nbElements] = element;
        this.nbElements++;
    }

    public void ajouter(int index, int element) {
        if (index < 0 || index > this.nbElements) {

            System.out.println("Index invalide");
            return;

        }
        
        if (this.nbElements == this.liste.length) {

            int[] listeTemp = new int[this.liste.length * 2];

            for (int i = 0; i < this.liste.length; i++) {

                listeTemp[i] = this.liste[i];

            }

            this.liste = listeTemp;

        }
        
        for (int i = this.nbElements; i > index; i--) {

            this.liste[i] = this.liste[i - 1];

        }
        
        this.liste[index] = element;
        this.nbElements++;
    }

    public void supprimer(int index) {
        
        if (index < 0 || index >= this.nbElements) {

            System.out.println("Index invalide");
            return;

        }
        
        for (int i = index; i < this.nbElements - 1; i++) {

            this.liste[i] = this.liste[i + 1];

        }
        
        this.nbElements--;
    }

    public void afficher() {
        
        for (int i = 0; i < this.nbElements; i++) {

            System.out.print(this.liste[i] + " ");

        }
        
        System.out.println();
    }

    public int get(int index) {

        if (index < 0 || index >= this.nbElements) {

            System.out.println("Index invalide");
            return -1;

        }
    
        return this.liste[index];
    }
    

    public void set(int index, int element) {
    
        if (index < 0 || index >= this.nbElements) {

            System.out.println("Index invalide");
            return;

        }
    
        this.liste[index] = element;
    }

    public int size() {
        return this.nbElements;
    }

    public boolean contient(int element) {
        
        for (int i = 0; i < this.nbElements; i++) {

            if (this.liste[i] == element) {

                return true;

            }

        }
        
        return false;
    }

    public void reverse() {
        
        int[] listeTemp = new int[this.nbElements];
        
        for (int i = 0; i < this.nbElements; i++) {

            listeTemp[i] = this.liste[this.nbElements - i - 1];

        }
        
        this.liste = listeTemp;
    }

}