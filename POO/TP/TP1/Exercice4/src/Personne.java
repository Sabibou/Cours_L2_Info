package TP1.Exercice4.src;

class Personne implements Comparable<Personne> {

    private String nom;
    private String prenom;
    private Date dateNaissance;
    private Boolean celibat;
    private Date dateMarriage;
    private Personne partenaire;

    public Personne(String nom, String prenom, Date dateNaissance) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setCelibat(true);
        setPartenaire(null);
    }

    public Personne(String nom, String prenom, Date dateNaissance, Boolean celibat, Personne partenaire, Date dateMarriage) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setCelibat(celibat);
        setPartenaire(partenaire);
        setDateMarriage(dateMarriage);
    }

    public void marier(Personne partenaire, Date dateMariage) {

        if (this.celibat == false) {
            throw new Error("La personne est déjà mariée.");
        }

        if (dateMariage.compareTo(this.dateNaissance) < 0) {
            throw new Error("La date de marriage ne peut pas être inférieure à la date de naissance.");
        }

        setDateMarriage(dateMariage);
        setCelibat(true);
        setPartenaire(partenaire);
    }

    private void setPartenaire(Personne partenaire) {

        this.partenaire = partenaire;

    }


    private void setDateMarriage(Date dateMarriage) {

        // On regarde si la date de marriage est supérieure à la date de naissance
        if (dateMarriage.compareTo(this.dateNaissance) < 0) {
            throw new Error("La date de marriage ne peut pas être inférieure à la date de naissance.");
        }

        this.dateMarriage = dateMarriage;

    }

    private void setCelibat(Boolean celibat) {

        this.celibat = celibat;

    }

    public void setnom(String nom) {

        this.nom = nom;

    }

    private void setprenom(String prenom) {

        this.prenom = prenom;

    }

    private void setDateNaissance(Date dateNaissance) {

        this.dateNaissance = dateNaissance;

    }

    public Personne getPartenaire() {

        return this.partenaire;

    }

    public Date getDateMarriage() {

        return this.dateMarriage;

    }

    public Boolean getCelibat() {

        return this.celibat;

    }

    public String getNom() {
        return this.nom;
    }

    public Date getDateNaissance() {
        return this.dateNaissance;
    }

    public String getPrenom() {
        return this.prenom;
    }

    @Override
    public int compareTo(Personne o) {
        
        return 0;
    }

}