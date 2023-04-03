// // Importation des librairies
// import processing.video.*; // Bibliotheque de controle camera

// /*

// L'espace des paramètres est quantifié (on discrétise r et theta) ● Pour chaque point de l'image binaire des contours
// ● Pour chaque possible theta
// ● Calculer le r correspondant
// ● Incrémenter la case Hough(r,theta)
// ● Rechercher les maximums locaux de Hough(r,theta)

// On va rajouter l'implémentation de la transformation de Hough pour la détection de lignes

// */

// class Point {

// 	int x;
// 	int y;

// 	public Point(int x, int y) {
// 		this.x = x;
// 		this.y = y;
// 	}

// }

// // Parametres de taille de la capture video
// final int widthCapture = 640;  // largeur capture
// final int heightCapture = 480; // hauteur capture
// final int numPixels = widthCapture * heightCapture; // nombre de pixels d'une image video
// final int fpsCapture = 30;     // taux d’images/secondes

// // Quelques couleurs...
// final int noir  = color(0,0,0); 
// final int blanc = color(255,255,255);

// // Declaration des variables globales
// String[] cameras;    // Liste des cameras dispos
// Capture webCam;      // Declaration de la Capture par Camera

// PImage img_lissee;  // image lissée
// PImage contours; //image seuillée des contours
// PImage gradient;  // image de la norme du gradient
// PImage gradnms;  // image du gradient après nms

// int rMax = (int) Math.sqrt(widthCapture * widthCapture + heightCapture * heightCapture);

// int[][] hough = new int[rMax * 2 + 1][181];

// ArrayList<Point> maxLocaux = new ArrayList<Point>();


// //**********************************************************************
// // Fonction d'initialisation de l'application - executee une seule fois
// void setup() {
//     //Initialisation des parametres graphiques utilises
//     size(640,480); // Ouverture en mode normal 640 * 480
//     surface.setTitle("Exemple extraction de contours");
//     colorMode(RGB, 255,255,255); 
//     noFill(); // pas de remplissage
//     background(noir); // couleur fond fenetre
    
//     //Recherche d'une webcam 
//     cameras = Capture.list();
//     if (cameras.length == 0) {
//         println("Pas de Webcam sur cet ordinateur !");
//         exit();
//     } else {
//         // Initialisation de la webcam Video par defaut
//         webCam = new Capture(this, widthCapture, heightCapture, cameras[0], fpsCapture);
//         webCam.start(); // Mise en marche de la webCam
//     }
    
//     //Initialisation des images
//     img_lissee = createImage(webCam.width, webCam.height, RGB);
//     gradient = createImage(webCam.width, webCam.height, RGB);
//     contours = createImage(webCam.width, webCam.height, RGB);
//     gradnms = createImage(webCam.width, webCam.height, RGB);
    
// } // Finde Setup



// //** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
// // Fonction de re - tracage de la fenetre - executee en boucle
// void draw() {

// 	background(0);

// 	hough = new int[rMax * 2 + 1][181];

//     if (webCam.available() == true) { // Verification de presence d'une nouvelle frame
//         webCam.read(); // Lecture du flux sur la camera... lecture d'une frame
//         image(webCam, 0, 0); // Restitution de l'image captee sur la webCam   
        
//         // Calcul des gradients et contours : exemple avec seuillage simple sur gradient nms
//         compute_contours(webCam, img_lissee, gradient, gradnms, contours, 80);
        
//         if (mousePressed && (mouseButton == RIGHT)) { // Test clic droit de la souris...
//             // Affichage de l'image des gradients
//             image(gradnms,0,0);
//         }
//         else if (mousePressed && (mouseButton == LEFT)) {// Test clic gauche de la souris...
//             // Affichage de l'image des contours
//             image(contours,0,0);
//         }
//         else{
//             // Affichagede l'image de la Webcam
//             image(webCam,0,0);
//         }
//     }
    
//     // On explore les pixels
// 	for (int x = 0; x < widthCapture; x++) {
		
// 		for (int y = 0; y < heightCapture; y++) {

// 			if (contours.get(x, y) == blanc) {

// 				for (float theta = 0; theta < Math.PI; theta += 0.1) {

// 					float r = x * cos(theta) + y * sin(theta);

// 					hough[(int) (r + rMax)][radianToDegree(theta)]++;

// 				}

// 			}

// 		}

// 	}

// 	// // On cherche les maximums locaux
// 	// maxLocaux.clear();

// 	// On calcule le maximum de la matrice et la moyenne
// 	int max = 0;
// 	int moyenne = 0;
// 	int n = 0;

// 	for (int r = 0; r < hough.length; r++) {
// 		for (int theta = 0; theta < hough[0].length; theta++) {
// 			if (hough[r][theta] > 10) {
// 				if (hough[r][theta] > max) {
// 					max = hough[r][theta];
// 				}
// 				moyenne += hough[r][theta];
// 				n++;
// 			}
// 		}
// 	}

// 	moyenne /= n;


// 	float seuil = max - (max - moyenne) / 2;

// 	// println("Seuil : " + seuil, "Moyenne : " + moyenne, "Max : " + max);

// 	// On cherche les maximums locaux (au dessus du seuil)
// 	maxLocaux.clear();

// 	for (int r = 1; r < hough.length - 1; r++) {
// 		for (int theta = 1; theta < hough[0].length - 1; theta++) {
// 			if (hough[r][theta] > seuil) {
// 				maxLocaux.add(new Point(r, theta));
// 			}
// 		}
// 	}

// 	// On affiche les maximums locaux
// 	for (Point p : maxLocaux) {
// 		stroke(255, 0, 0);
// 		if (p.y == 0) {
// 			// Line vertical, cas d'erreur pour éviter la division par 0
// 			line(0, p.x - rMax, widthCapture, p.x - rMax);
// 		} else {
// 			line(0, (p.x - rMax) / sin(degreeToRadian(p.y)), widthCapture, (p.x - rMax - widthCapture * cos(degreeToRadian(p.y))) / sin(degreeToRadian(p.y)));
// 		}
// 	}

// }


// int radianToDegree(float radian) {
// 	return (int) (radian * 180 / Math.PI);
// }

// float degreeToRadian(int degree) {
// 	return (float) (degree * Math.PI / 180);
// }