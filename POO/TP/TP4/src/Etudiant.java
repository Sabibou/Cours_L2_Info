package TP4.src;

public class Etudiant {
    
    private String nom;
    private String prenom;
    private int age;
    private int numeroEtudiant;
    private int note;

    public Etudiant(String nom, String prenom, int age, int numeroEtudiant, int note) {
        this.nom = nom;
        this.prenom = prenom;
        this.age = age;
        this.numeroEtudiant = numeroEtudiant;
        this.note = note;
    }

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public int getAge() {
        return age;
    }

    public int getNumeroEtudiant() {
        return numeroEtudiant;
    }

    public int getNote() {
        return note;
    }

}
