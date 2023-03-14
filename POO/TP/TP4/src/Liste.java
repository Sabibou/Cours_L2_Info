package TP4.src;

import java.util.Arrays;

class Liste<T> {
    private T[] liste;
    private int nbElements;

    public Liste() {
        this.liste = newArray(10);
        this.nbElements = 0;
    }

    public Liste(int taille) {
        this.liste = newArray(taille);
        this.nbElements = 0;
    }

    public Liste(Liste<T> liste) {
        this.liste = newArray(liste.liste.length);
        this.nbElements = liste.nbElements;

        for (int i = 0; i < liste.nbElements; i++) {

            this.liste[i] = liste.liste[i];
        
        }
    }

    public Liste(T[] liste) {
        this.liste = newArray(liste.length);
        this.nbElements = liste.length;

        for (int i = 0; i < liste.length; i++) {
        
            this.liste[i] = liste[i];
        
        }
    }

    public void ajouter(T element) {
        if (this.nbElements == this.liste.length) {

            T[] listeTemp = newArray(this.liste.length * 2);

            for (int i = 0; i < this.liste.length; i++) {

                listeTemp[i] = this.liste[i];

            }

            this.liste = listeTemp;
        
        }

        this.liste[this.nbElements] = element;
        this.nbElements++;
    }

    public void ajouter(int index, T element) {
        if (index < 0 || index > this.nbElements) {

            return;

        }
        
        if (this.nbElements == this.liste.length) {

            T[] listeTemp = newArray(this.liste.length * 2);

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

            return;

        }
        
        for (int i = index; i < this.nbElements - 1; i++) {

            this.liste[i] = this.liste[i + 1];

        }
        
        this.nbElements--;

        // Comme une ArrayList, on réduit la taille du tableau si il y a trop de place vide
        if (this.nbElements < this.liste.length / 2) {

            T[] listeTemp = newArray(this.liste.length / 2);

            for (int i = 0; i < this.nbElements; i++) {

                listeTemp[i] = this.liste[i];

            }

            this.liste = listeTemp;

        }

    }

    public void afficher() {
        
        for (int i = 0; i < this.nbElements; i++) {

            System.out.print(this.liste[i] + " ");

        }
        
        System.out.println();
    }

    public T get(int index) {

        if (index < 0 || index >= this.nbElements) {

            return null;

        }
    
        return this.liste[index];
    }
    

    public void set(int index, T element) {
    
        if (index < 0 || index >= this.nbElements) {

            return;

        }
    
        this.liste[index] = element;
    }

    public int size() {
        return this.nbElements;
    }

    public boolean contient(T element) {
        
        for (int i = 0; i < this.nbElements; i++) {

            if (this.liste[i] == element) {

                return true;

            }

        }
        
        return false;
    }

    public void reverse() {

        T[] listeTemp = newArray(this.nbElements);

        for (int i = 0; i < this.nbElements; i++) {

            listeTemp[i] = this.liste[this.nbElements - i - 1];

        }

        this.liste = listeTemp;
    }
    
    @SafeVarargs
    static <T> T[] newArray(int length, T... array) {
        return Arrays.copyOf(array, length);
    }

}