package TP2.Exercice2.src;

class Mot {
    
    private String mot;

    public Mot(String mot) {
        this.mot = mot;
    }

    public String getMot() {
        return this.mot;
    }

    public void afficheVoyelles() {
        for (int i = 0; i < this.mot.length(); i++) {

            char c = this.mot.charAt(i);

            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y') {
                System.out.print(c);
            }

        }

        System.out.println();

    }

    public Boolean estPalindrome() {
        
        Boolean isPalindrome = true;

        int index = 0;
        int length = this.mot.length();

        while (isPalindrome && index < length / 2) {

            if (this.mot.charAt(index) != this.mot.charAt(length - index - 1)) {
                isPalindrome = false;
            }

            index++;

        }
        
        return isPalindrome;

    }

    public Boolean estContenu(Mot mot) {
        return this.mot.contains(mot.getMot());
    }

    public String trieMot() {


        String sortie = "";

        // On trie toute les lettres du mot
        for (int i = 0; i < this.mot.length(); i++) {

            char c = this.mot.charAt(i);

            // On cherche la position de la lettre dans le mot
            int index = 0;
            while (index < sortie.length() && c > sortie.charAt(index)) {
                index++;
            }

            // On insère la lettre à la bonne position
            sortie = sortie.substring(0, index) + c + sortie.substring(index);

        }

        return sortie;

    }    

    @Override
    public String toString() {
        return this.mot;
    }

}