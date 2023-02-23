/****************************************************************************/
/*  MESNARD Emmanuel                                              ISIMA     */
/*                                                                          */
/*          Exemple 8 : Realite Augmentee par ARtoolkit et Webcam           */
/*                      Trace d'un cube 3D a la place du marqueur           */
/*                                                                          */
/* Exemple_8_RA_Cube.pde                               Processing 3.5.2     */
/****************************************************************************/

// Importation des librairies
import processing.video.*;     // Bibliotheque de controle camera
import jp.nyatla.nyar4psg.*;   // ARToolKit (version 3.0.7)

// Parametres de taille de la capture video
final int widthCapture = 640;  // largeur capture
final int heightCapture = 480; // hauteur capture
final int numPixels = widthCapture * heightCapture; // nombre de pixels d'une image video
final int fpsCapture = 30;     // taux d’images/secondes

import MD2Importer.*; // Librairie d'acces aux fichiers MD2

MD2_Loader chargeurOiseau;  // Espace memoire pour charger/decoder le fichier
MD2_Model Oiseau;           // Objet MD2 lu
MD2_ModelState[] animation; // Animations disponibles pour ce modele
float pourcentAnimation = 1; // Vitesse sur le rendu de l'animation  
float rotX, rotZ;           // Rotation de l'objet

// Declaration des variables globales
String[] cameras;    // Liste des cameras dispos
Capture webCam;      // Camera 
MultiMarker sceneMM; // Scene de recherche de "multi-marqueur"

// Fonction d'initialisation de l'application - executee une seule fois
void setup() {
    //Initialisation des parametres graphiques utilises
    size(640, 480, P3D); // ouverture en mode 3D
    surface.setTitle("Exemple 8 - RA Cube - E. Mesnard / ISIMA");
    strokeWeight(3); // Epaisseur du trait
    stroke(#EA0C7B); // Couleur pourtour par defaut : rose violace
    noFill(); // Sans remplissage
    
    //Creation du chargeur pour acceder au fichier MD2
    chargeurOiseau = new MD2_Loader(this);
    
    //Chargement effectif du modele texture
    Oiseau = chargeurOiseau.loadModel("Oiseau.md2", "Oiseau.jpg");
    
    //Recherche d'une webcam 
    cameras = Capture.list();
    if (cameras.length == 0) {
        println("Pas de Webcam sur cet ordinateur !");
        exit();
    } else {
        // Initialisation de la webcam par defaut
        webCam = new Capture(this, widthCapture, heightCapture, cameras[0], fpsCapture);
        webCam.start(); // Mise en marche de la webCam
    }
    
    if (Oiseau == null) {
        println("Probleme de chargement de ce fichier MD2");
        exit();
    } else {
        
        // Affichage(eventuel) de diverses informations pour le DEBUG
        
        // chargeurOiseau.displayHeader(); // Informations sur le modele charge
        // chargeurOiseau.displayGLcommands(); // Affichage des commandes OPENGL
        // correspondantes
        // chargeurOiseau.displayModelStates(); // Affiche le nom des animations
        // et les frames associees
        // chargeurOiseau.displayFrameNames(); // Affiche le nom des frames 
        
        chargeurOiseau = null; // Liberation de l'espace memoire
        
        // Recuperation de toutes les animations disponibles
        animation = Oiseau.getModelStates();
        
        // Affichaged'informations pour le DEBUG
        // for(int i= 0; i < animation.length; i++){
        //  println("Animation["+i+"]= "+ animation[i].name);
    // }
        //println("Espace memoire utilise (sans texture)"+Oiseau.memUsage());
        
        // Recentrage de l'objet pour avoir un repere en (0,0,0)
        // Vector3 Decalage = new Vector3();
        // Decalage = Oiseau.getModOffset();
        // println("Decalage d'origine = " +Decalage);
        Oiseau.centreModel();
        // Decalage = Oiseau.getModOffset();
        // println("Decalage corrige (normalement =[0,0,0]) = " +Decalage);
        
        
        // Mise a l'echelle souhaitee de l'objet MD2
        Vector3 dimensionOiseau = new Vector3();
        dimensionOiseau = Oiseau.getModSize();
        // println("Taille de l'oiseau : " + dimensionOiseau);
        Oiseau.scaleModel((0.8 * height) / dimensionOiseau.y);
        // ou bien, mise a l'echelle manuelle : Oiseau.scaleModel(0.1);
        // dimensionOiseau = Oiseau.getModSize();
        // println("Taille reduite : " + dimensionOiseau);
        
        // Selectionde l'animation (par exemple, la derniere !)
        Oiseau.setState(animation.length - 1); // Une seule pour cet exemple = 0
        
        // Calcul (eventuel) d'une vitesse d'evolution dans les animations
        pourcentAnimation = constrain(4 / (frameRate + 0.01), 0.01, 1);
        
        // Initialisation des variables globales
        rotX = radians(70); rotZ = radians(15);
    } 	
    
    //Declaration dela scene de recherche avec parametres par defaut :
    //calibration decamera et systeme de coordonnees
    sceneMM = new MultiMarker(this,widthCapture, heightCapture,
        "camera_para.dat",
        NyAR4PsgConfig.CONFIG_PSG);
    
    //Declaration dumarqueur a rechercher, avec sa dimension en mm
    sceneMM.addARMarker("Marqueur_ISIMA.patt", 80); // Marqueur numero 0
    println(MultiMarker.VERSION); // Affichage numero version en console
} // Fin de Setup


// Fonction de re - tracage de la fenetre - executee en boucle
void draw() {
    if (webCam.available() == true) { // Verification de presence d'une nouvelle frame
        
        webCam.read(); // Lecture du flux sur la camera... lecture d'une frame
        
        sceneMM.detect(webCam);   // Recherche du marqueur dans la scene
        webCam.updatePixels();    // Mise a jour des pixels
        
        
        // Effacer la fenetre avant de dessiner l'image video "reelle"
        background(0); 
        image(webCam, 0, 0);// Affiche l'image prise par la webCam
        
        // Incrustation de l'image virtuelle si marqueur trouve
        if (sceneMM.isExist(0)) { // Marqueur ISIMA
            // Le marqueur est detecte dans le flux video
            // Changement de repere pour tracer en coordonnees "Marqueur"
            sceneMM.beginTransform(0); // Modification graphique sur marqueur 0
            // trace d'un rectangle 2D : rect(-40,-40,80,80);
            // ...ou mieux, traced'un cube 3D :
			// Affichage de l'oiseau
			Oiseau.update(pourcentAnimation);
  			Oiseau.render();
			// Retour au repere "monde"
            sceneMM.endTransform();
        }
    }
}
