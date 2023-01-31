package TP1.Exercice5.src;

class Personne implements Comparable<Personne> {

    private String nom;
    private String prenom;
    private Date dateNaissance;
    private Boolean celibat = true;
    private Date dateMarriage = null;
    private Personne partenaire = null;
    private Personne parentA = null;
    private Personne parentB = null;
    private Boolean estHomme = true;

    public Personne(String nom, String prenom, Date dateNaissance, Boolean estHomme) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setEstHomme(estHomme);
    }

    public Personne(String nom, String prenom, Date dateNaissance, Personne parentA, Personne parentB, Boolean estHomme) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setParentA(parentA);
        setParentB(parentB);
        setEstHomme(estHomme);
    }

    public Personne(String nom, String prenom, Date dateNaissance, Boolean celibat, Personne partenaire,
            Date dateMarriage, Boolean estHomme) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setCelibat(celibat);
        setPartenaire(partenaire);
        setDateMarriage(dateMarriage);
        setEstHomme(estHomme);
    }
    
    public Personne(String nom, String prenom, Date dateNaissance, Boolean celibat, Personne partenaire,
            Date dateMarriage, Personne parentA, Personne parentB, Boolean estHomme) {
        setnom(nom);
        setprenom(prenom);
        setDateNaissance(dateNaissance);
        setCelibat(celibat);
        setPartenaire(partenaire);
        setDateMarriage(dateMarriage);
        setParentA(parentA);
        setParentB(parentB);
        setEstHomme(estHomme);
    }

    public Boolean estFrereOuSoeur(Personne personne) {

        if (this.parentA == personne.parentA || this.parentA == personne.parentB
                || this.parentB == personne.parentA || this.parentB == personne.parentB) {
            return true;
        }

        return false;

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

    private void setParentA(Personne parentA) {

        this.parentA = parentA;

    }

    private void setParentB(Personne parentB) {

        this.parentB = parentB;

    }

    public Personne getParentA() {

        return this.parentA;

    }

    public Personne getParentB() {

        return this.parentB;

    }

    private void setCelibat(Boolean celibat) {

        this.celibat = celibat;

    }

    public void setnom(String nom) {

        if (getEstHomme() == true) {

            // Il ne peut pas changer
            throw new Error("Le nom ne peut pas être changé car c'est un homme.");
        
        }

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

    public Boolean getEstHomme() {
        return this.estHomme;
    }

    public void setEstHomme(Boolean estHomme) {
        this.estHomme = estHomme;
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
        
        if (this.nom.compareTo(o.getNom()) == 0) {
            return this.prenom.compareTo(o.getPrenom());
        } else {
            return this.nom.compareTo(o.getNom());
        }

    }

}