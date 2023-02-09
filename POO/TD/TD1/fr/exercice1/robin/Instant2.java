class Instant2 {

    private int secondes;
    private static final int SECONDES_PAR_HEURE = 3600;
    private static final int SECONDES_PAR_MINUTE = 60;
    private static final int SECOND_MAX = SECONDES_PAR_HEURE * 24;
    private static final int SECOND_MIN = 0;

    // Constructeur
    Instant2(int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this.setSecondes(secondes);

        // Permet d'utiliser des secondes seulement plutôt que des heures, minutes et secondes

    }

    Instant2(int heures, int minutes, int secondes) {

        // Assignation des valeurs
        // On utilise les setters pour vérifier les valeurs
        // (pour ne pas faire de la duplication de code)
        this(heures * SECONDES_PAR_HEURE + minutes * SECONDES_PAR_MINUTE + secondes);

    }

    // Getters
    public int getHeures() {
        return this.secondes / SECONDES_PAR_HEURE;
    }

    public int getMinutes() {
        return (this.secondes / SECONDES_PAR_MINUTE) % SECONDES_PAR_MINUTE;
    }

    public int getSecondes() {
        return this.secondes % SECONDES_PAR_MINUTE;
    }


    // Setters
    private void setSecondes(int secondes) {

        // Regarde si les secondes sont valides
        if (SECOND_MIN >= secondes || secondes >= SECOND_MAX) {
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

    public int compareTo(Instant2 instant) {

        if (this.secondes < instant.secondes) {
            return -1;
        } else if (this.secondes > instant.secondes) {
            return 1;
        } else {
            return 0;
        }

    }


    @Override
    public boolean equals(Object obj) {

        if (obj == null) {
            return false;
        }

        if (obj == this) {
            return true;
        }

        if (!(obj instanceof Instant2)) {
            return false;
        }

        Instant2 instant = (Instant2) obj;

        return this.compareTo(instant) == 0;

    }

    @Override
    public int hashCode() { // On utilise le hashcode de la classe Integer
        return Integer.hashCode(this.secondes);
    }

    

}