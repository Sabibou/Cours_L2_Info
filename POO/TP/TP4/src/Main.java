package TP4.src;

import java.util.Random;

public class Main {
    
    public static void main(String[] args) {

        // ------------------------ Exercice 1 ------------------------
        // Matrice matrice1 = new Matrice(3, 3);
        // Matrice matrice2 = new Matrice(3, 3);

        // matrice1.remplirMatrice();
        // matrice2.remplirMatrice();

        // matrice1.afficheMatrice();
        // System.out.println();
        // matrice2.afficheMatrice();
        // System.out.println();

        // Matrice matriceResultat = matrice1.addition(matrice2);
        // matriceResultat.afficheMatrice();
        // System.out.println();

        // matriceResultat = matrice1.multiplication(matrice2);
        // matriceResultat.afficheMatrice();
        // System.out.println();

        // Matrice triangulaire = Matrice.matriceTriangulaire(3);
        // triangulaire.afficheTriangulaire();

        // ------------------------ Exercice 2 ------------------------
        // Liste<Integer> liste = new Liste<Integer>();

        // liste.ajouter(1);
        // liste.ajouter(2);
        // liste.ajouter(3);

        // liste.afficher();

        // liste.reverse();
        // liste.afficher();

        // ------------------------ Exercice 3 ------------------------
        // HashMap<String, Integer> map = new HashMap<String, Integer>();

        // map.put("a", 1);
        // map.put("b", 2);
        // map.put("c", 3);

        // System.out.println(map.get("a"));

        // ------------------------ Exercice 4 ------------------------
        // On va faire une Liste, un HashMap et un tableau
        // On va faire n insertions de 100 Étudiants dans les 3 structures, et comparer le temps d'exécution

        long n = 1000000;

        Liste<Etudiant> liste;
        HashMap<Integer, Etudiant> map;
        Etudiant[] tableau;

        long debut, fin;

        String nomAlea, prenomAlea;
        int ageAlea, numeroEtudiantAlea, noteAlea;

        Random random = new Random();

        // On remplit la liste
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            liste = new Liste<Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                liste.ajouter(new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'insertion pour la liste: " + (double) (fin - debut) / 1000 + "s");

        // On remplit le HashMap
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            map = new HashMap<Integer, Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                map.put(j, new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'insertion pour le HashMap: " + (double) (fin - debut) / 1000 + "s");

        // On remplit le tableau
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            tableau = new Etudiant[100];

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                tableau[j] = new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea);

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'insertion pour le tableau: " + (double) (fin - debut) / 1000 + "s");





        long tempsTotal; // On va calculer le temps QUE pour le calcul de la moyenne



        // On calcule la moyenne des notes des étudiants (on regénère les étudiants à chaque fois)

        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            liste = new Liste<Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                liste.ajouter(new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }

            debut = System.currentTimeMillis();

            for (int j = 0; j < 100; j++) {

                liste.get(j).getNote();

            }

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }


        System.out.println("Temps de calcul de la moyenne pour la liste: " + (double) tempsTotal / 1000 + "s");

        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            map = new HashMap<Integer, Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                map.put(j, new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }


            debut = System.currentTimeMillis();

            for (int j = 0; j < 100; j++) {

                map.get(j).getNote();

            }

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }

        System.out.println("Temps de calcul de la moyenne pour le HashMap: " + (double) tempsTotal / 1000 + "s");

        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            tableau = new Etudiant[100];

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                tableau[j] = new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea);

            }

            debut = System.currentTimeMillis();

            for (int j = 0; j < 100; j++) {

                tableau[j].getNote();

            }

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }

        System.out.println("Temps de calcul de la moyenne pour le tableau: " + (double) tempsTotal / 1000 + "s");



        // Maintenant on va  rechercher un étudiant dans la liste
        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            liste = new Liste<Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                liste.ajouter(new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }

            debut = System.currentTimeMillis();

            liste.contient(new Etudiant("Nom50", "Prenom50", 50, 50, 50));

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }

        System.out.println("Temps de recherche pour la liste: " + (double) tempsTotal / 1000 + "s");


        // Maintenant on va  rechercher un étudiant dans le HashMap
        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            map = new HashMap<Integer, Etudiant>();

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                map.put(j, new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea));

            }

            debut = System.currentTimeMillis();

            map.containsValue(new Etudiant("Nom50", "Prenom50", 50, 50, 50));

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }

        System.out.println("Temps de recherche pour le HashMap: " + (double) tempsTotal / 1000 + "s");

        // Maintenant on va  rechercher un étudiant dans le tableau
        tempsTotal = 0;

        for (int i = 0; i < n; i++) {

            tableau = new Etudiant[100];

            for (int j = 0; j < 100; j++) {

                nomAlea = "Nom" + random.nextInt(100);
                prenomAlea = "Prenom" + random.nextInt(100);
                ageAlea = random.nextInt(100);
                numeroEtudiantAlea = random.nextInt(100);
                noteAlea = random.nextInt(100);

                tableau[j] = new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea);

            }

            debut = System.currentTimeMillis();

            for (int j = 0; j < 100; j++) {

                if (tableau[j].equals(new Etudiant("Nom50", "Prenom50", 50, 50, 50))) {

                    break;

                }

            }

            fin = System.currentTimeMillis();

            tempsTotal += fin - debut;

        }

        System.out.println("Temps de recherche pour le tableau: " + (double) tempsTotal / 1000 + "s");

        

    }
    
    

}
