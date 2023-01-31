package TP1.Exercice3.src;

class Date implements Comparable<Date> {
    
    private int annee;
    private int mois;
    private int jour;

    public Date(int annee, int mois, int jour) {

        if (annee < 0) {
            throw new IllegalArgumentException("L'année ne peut pas être négative");
        }

        if (mois < 1 || mois > 12) {
            throw new IllegalArgumentException("Le mois doit être compris entre 1 et 12");
        }

        if (jour < 1 || jour > 31) {
            throw new IllegalArgumentException("Le jour doit être compris entre 1 et 31");
        }

        this.annee = annee;
        this.mois = mois;
        this.jour = jour;

    }

    @Override
    public String toString() {
        return this.annee + "-" + this.mois + "-" + this.jour;
    }

    public void afficheDate() {

        System.out.println(this.toString());

    }


    @Override
    public int compareTo(Date date) {

        if (this.annee > date.annee) {
            return 1;
        } else if (this.annee < date.annee) {
            return -1;
        } else {
            if (this.mois > date.mois) {
                return 1;
            } else if (this.mois < date.mois) {
                return -1;
            } else {
                if (this.jour > date.jour) {
                    return 1;
                } else if (this.jour < date.jour) {
                    return -1;
                } else {
                    return 0;
                }
            }
        }

    }



    public int getAnnee() {
        return this.annee;
    }

    public int getMois() {
        return this.mois;
    }

    public int getJour() {
        return this.jour;
    }

}