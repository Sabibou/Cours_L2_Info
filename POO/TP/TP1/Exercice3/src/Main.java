package TP1.Exercice3.src;


/**
 * Main
 */
class Main {

    public static void main(String[] args) {
        
        Date date = new Date(2019, 12, 31);

        date.afficheDate();

        Date date2 = new Date(2019, 11, 31);

        // Comparer
        System.out.println(date.compareTo(date2));


    }
}
