class Instant {

    private int heures; // 0 <= heure < 24
    private int minutes; // 0 <= minute < 60
    private int secondes; // 0 <= seconde < 60

    // Constructeur
    Instant(int heures, int minutes, int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this.setHeures(heures);
        this.setMinutes(minutes);
        this.setSecondes(secondes);

    }

    // Getters
    public int getHeures() {
        return this.heures;
    }
    
    public int getMinutes() {
        return this.minutes;
    }
    
    public int getSecondes() {
        return this.secondes;
    }
    
    
    // Setters
    private void setHeures(int heures) {

        // Regarde si les heures sont valides
        if (0 > heures || heures >= 24) {
            throw new IllegalArgumentException("Heures invalides");
        }

        this.heures = heures;
    }
    
    private void setMinutes(int minutes) {

        // Regarde si les minutes sont valides
        if (0 > minutes || minutes >= 60) {
            throw new IllegalArgumentException("Minutes invalides");
        }

        this.minutes = minutes;
    }
    
    private void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (0 > secondes || secondes >= 60) {
            throw new IllegalArgumentException("Secondes invalides");
        }

        this.secondes = secondes;
    }
    
    public String stringify() {

        return String.format("%02d:%02d:%02d",
                this.getHeures(),
                this.getMinutes(),
                this.getSecondes());
    }
    
    @Override
    public String toString() {
        return this.stringify();
    }


    public static Instant minus(Instant instant1, Instant instant2) {

        // On convertit les 2 instants en secondes
        int secondes1 = instant1.getHeures() * 3600 + instant1.getMinutes() * 60 + instant1.getSecondes();
        int secondes2 = instant2.getHeures() * 3600 + instant2.getMinutes() * 60 + instant2.getSecondes();

        // On calcule la différence
        int difference = secondes1 - secondes2;

        // On convertit la différence en heures, minutes et secondes
        int heures = difference / 3600;
        int minutes = (difference % 3600) / 60;
        int secondes = (difference % 3600) % 60;

        // On retourne un nouvel instant
        return new Instant(heures, minutes, secondes);

    }

    public Instant minus(Instant instant) {

        int secondes1 = this.getHeures() * 3600 + this.getMinutes() * 60 + this.getSecondes();
        int secondes2 = instant.getHeures() * 3600 + instant.getMinutes() * 60 + instant.getSecondes();

        int difference = secondes1 - secondes2;

        int heures = difference / 3600;
        int minutes = (difference % 3600) / 60;

        // On retourne un nouvel instant
        return new Instant(heures, minutes, difference % 60);

    }
    
    public int compareTo(Instant instant) {

        int secondes1 = this.getHeures() * 3600 + this.getMinutes() * 60 + this.getSecondes();
        int secondes2 = instant.getHeures() * 3600 + instant.getMinutes() * 60 + instant.getSecondes();

        return Integer.compare(secondes1, secondes2);

    }

    @Override
    public boolean equals(Object obj) {

        if (obj == null) {
            return false;
        }

        if (obj == this) {
            return true;
        }

        if (!(obj instanceof Instant)) {
            return false;
        }

        Instant instant = (Instant) obj;

        return this.compareTo(instant) == 0;

    }
    
    
    @Override
    public int hashCode() {
        return Integer.hashCode(this.getHeures() * 3600 + this.getMinutes() * 60 + this.getSecondes());
    }


}
