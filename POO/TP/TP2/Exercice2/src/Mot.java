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
        return this.mot.equals(new StringBuilder(this.mot).reverse().toString());
    }

    public Boolean estContenu(Mot mot) {
        return this.mot.contains(mot.getMot());
    }

    public String trieMot() {


        // Trie par ordre alphabétique le mot
        char[] motTrie = this.mot.toCharArray();

        for (int i = 0; i < motTrie.length; i++) {

            for (int j = i + 1; j < motTrie.length; j++) {

                if (motTrie[i] > motTrie[j]) {

                    char temp = motTrie[i];
                    motTrie[i] = motTrie[j];
                    motTrie[j] = temp;

                }

            }
            
        }

        // Convertion du tableau de char en String
        String motTrieString = new String(motTrie);

        return motTrieString;

    }    

    @Override
    public String toString() {
        return this.mot;
    }

}