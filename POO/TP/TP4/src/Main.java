package TP4.src;

import java.util.ArrayList;
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
        // HashMap<String, Integer> map = new HashMap<String, Integer>(10);

        // map.put("a", 1);
        // map.put("b", 2);
        // map.put("c", 3);

        // System.out.println(map.get("a"));

        // ------------------------ Exercice 4 ------------------------
        // On va faire une Liste, un HashMap et un tableau
        // On va faire n insertions de 100 Étudiants dans les 3 structures, et comparer le temps d'exécution        
        
        
        
        long n = 10000000;

        // On créer un tableau de 100 étudiants
        Etudiant[] tableau = new Etudiant[100];

        Random random = new Random();

        for (int i = 0; i < 100; i++) {

            String nomAlea = "Nom" + random.nextInt(100);
            String prenomAlea = "Prenom" + random.nextInt(100);
            int ageAlea = random.nextInt(100);
            int numeroEtudiantAlea = random.nextInt(100);
            int noteAlea = random.nextInt(100);

            tableau[i] = new Etudiant(nomAlea, prenomAlea, ageAlea, numeroEtudiantAlea, noteAlea);

        }

        // Maintenant on va faire les tests
        Etudiant[] testTableau = new Etudiant[100];
        Liste<Etudiant> testListe = new Liste<Etudiant>();
        HashMap<Integer, Etudiant> testMap = new HashMap<Integer, Etudiant>(100);

        long debut, fin;

        // On remplit le tableau
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {


            testTableau = new Etudiant[100];

            for (int j = 0; j < 100; j++) {

                testTableau[j] = tableau[j];

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour remplir le tableau : " + (fin - debut) + "ms");

        // On remplit la liste
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {


            testListe = new Liste<Etudiant>();

            for (int j = 0; j < 100; j++) {

                testListe.ajouter(tableau[j]);

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour remplir la liste : " + (fin - debut) + "ms");

        // On remplit le HashMap
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {


            testMap = new HashMap<Integer, Etudiant>(100);

            for (int j = 0; j < 100; j++) {

                testMap.put(tableau[j].getNumeroEtudiant(), tableau[j]);

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour remplir le HashMap : " + (fin - debut) + "ms");

        // On récupère un élément du tableau
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            Etudiant a = testTableau[50];

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour récupérer un élément du tableau : " + (fin - debut) + "ms");

        // On récupère un élément de la liste
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            Etudiant a = testListe.get(50);

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour récupérer un élément de la liste : " + (fin - debut) + "ms");

        // On récupère un élément du HashMap
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            Etudiant a = testMap.get(50);

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour récupérer un élément du HashMap : " + (fin - debut) + "ms");


        Etudiant target = new Etudiant("Nom50", "Prenom50", 50, 50, 50);

        // On recherche un élément du tableau
        debut = System.currentTimeMillis();

        for (int i = 0; i < n; i++) {

            for (int j = 0; j < 100; j++) {

                // Si l'étudiant est target
                if (testTableau[j].equals(target)) {

                    Etudiant a = testTableau[j];

                }

            }

        }

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour rechercher un élément du tableau : " + (fin - debut) + "ms");

        // On recherche un élément de la liste
        debut = System.currentTimeMillis();

        boolean found = testListe.contient(target);

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour rechercher un élément de la liste : " + (fin - debut) + "ms");

        // On recherche un élément du HashMap
        debut = System.currentTimeMillis();

        found = testMap.containsValue(target);

        fin = System.currentTimeMillis();

        System.out.println("Temps d'exécution pour rechercher un élément du HashMap : " + (fin - debut) + "ms");


    }
    
    

}
