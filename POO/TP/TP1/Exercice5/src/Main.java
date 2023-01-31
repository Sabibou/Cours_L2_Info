package TP1.Exercice5.src;

public class Main {
    
    public static void main(String[] args) {
        
        Personne p1 = new Personne("Dupont", "Jean", new Date(1990, 1, 1), true);
        Personne p2 = new Personne("Durand", "Marie", new Date(1990, 1, 1), true);

        p1.marier(p2, new Date(2010, 1, 1));

        p1.setnom("Eheh");

        System.out.println(p1.getNom() + " " + p1.getPrenom() + " est marié à " + p1.getPartenaire().getNom() + " " + p1.getPartenaire().getPrenom() + " depuis le " + p1.getDateMarriage().toString());

    }


}
