class InstantTD {

    private int heures; // 0 <= heure < 24
    private int minutes; // 0 <= minute < 60
    private int secondes; // 0 <= seconde < 60

    // Constructeur
    InstantTD(int heures, int minutes, int secondes) {

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
    public void setHeures(int heures) {

        // Regarde si les heures sont valides
        if (0 > heures || heures >= 24) {
            throw new IllegalArgumentException("Heures invalides");
        }

        this.heures = heures;
    }
    
    public void setMinutes(int minutes) {

        // Regarde si les minutes sont valides
        if (0 > minutes || minutes >= 60) {
            throw new IllegalArgumentException("Minutes invalides");
        }

        this.minutes = minutes;
    }
    
    public void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (0 > secondes || secondes >= 60) {
            throw new IllegalArgumentException("Secondes invalides");
        }

        this.secondes = secondes;
    }
    
    public String stringify() {

        return String.format("%02d:%02d:%02d",
                this.heures,
                this.minutes,
                this.secondes
        );
    }

}