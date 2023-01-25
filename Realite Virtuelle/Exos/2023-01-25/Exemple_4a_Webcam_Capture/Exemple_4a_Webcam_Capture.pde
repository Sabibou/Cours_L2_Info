/****************************************************************************/
/*  MESNARD Emmanuel                                              ISIMA     */
/*                                                                          */
/*      Gestion d'une Webcam via le mode "Capture" de la bibliotheque       */
/*      standard de Processing  "processing.video.*" basee sur GStreamer    */
/*                                                                          */
/* Exemple_4a_Webcam_Capture.pde                       Processing 3.5.4     */
/****************************************************************************/

// Importation des librairies
import processing.video.*; // Bibliotheque de controle camera

Capture webCam;      // Declaration de la Capture par Camera
String[] cameras;    // Liste textuelle des webCams disponibles

boolean reverseCam = false; // Flag de changement de sens de la camera

PImage tux; // Image à afficher

float lastX = 0;
float lastY = 0;

boolean initialized = false;
// Nombre de fois où on n'a pas trouvé de point vert d'affilée
int noGreen = 0;

int REGION_SIZE = 10;

// Fonction d'initialisation de l'application - executee une seule fois
void setup() {
    size(640, 480);
    
    surface.setTitle("Exemple 4a - WebCam Capture Standard - E. Mesnard / ISIMA");
    
    //Recherche des webCams disponibles, par interrogation du systeme d'exploitation
    cameras = Capture.list(); 
    
    
    if (0 == cameras.length) {
        println("Pas de Webcam sur cet ordinateur !");
        exit();
    } else {
        // Affichage console de la liste des webcams disponibles
        printArray(cameras); 
        // Par exemple, deux cameras :
        // [0] "Integrated Webcam"
        // [1] "Logitech HD Webcam C310"
        
        // Initialisation de la webcam Video 
        webCam = new Capture(this, 640, 480); // Webcam; valeurs par defaut
        
        // ou encore, en choisissant explicitement la premiere de la liste :
        //  webCam = new Capture(this, cameras[0]);
        // ou en precisant un peu :
        //  webCam = new Capture(this, 640, 480, cameras[0], 30);
        // ou en precisant beaucoup !
        //  webCam = new Capture(this, 640, 480, "Logitech HD Webcam C310", 30);
        
        webCam.start(); // Mise en marche de la webCam

		tux = loadImage("Tux.png");
		// redimensionner l'image à 60 pixels de large
		tux.resize(300, 0);


    }


} // Finde Setup


// Fonction de re - tracage de la fenetre - executee en boucle
void draw() {
    if (webCam.available() == true) { // Verification de presence d'une nouvelle frame
        webCam.read(); // Lecture du flux sur la camera... lecture d'une frame
        
        if (reverseCam == true) {
			// Inversion de l'image captee par la webCam
			loadPixels();
			webCam.loadPixels();
			
			// Inversion de l'image captee par la webCam
			

			updatePixels();

			// Affichage de l'image captee par la webCam
			image(webCam, 0, 0);

		} else {

			// Restitution de l'image captee par la webCam
			image(webCam, 0, 0);

		}
    }

	// On cherche les coordonnées du point le plus vert (grâce au canal vert de HSB)
	float maxGreen = 0;
	float maxGreenX = 0;
	float maxGreenY = 0;

	// for (int x = 0; x < width; x++) {
	// 	for (int y = 0; y < height; y++) {
	// 		int loc = x + y * width;
	// 		int c = webCam.pixels[loc];
	// 		float h = hue(c);
	// 		float s = saturation(c);
	// 		float b = brightness(c);
	// 		if (h > 180 && h < 270) {
	// 			if (b > maxGreen) {
	// 				maxGreen = b;
	// 				maxGreenX = x;
	// 				maxGreenY = y;
	// 			}
	// 		}
	// 	}
	// }

	
	if (initialized == true) {

		// Chercher le point le plus vert autour du point précédent
		for (int x = (int)lastX - REGION_SIZE; x < lastX + REGION_SIZE; x++) {
			for (int y = (int)lastY - REGION_SIZE; y < lastY + REGION_SIZE; y++) {
				int loc = x + y * width;

				if (loc < 0 || loc >= webCam.pixels.length) {
					continue;
				}

				int c = webCam.pixels[loc];
				float h = hue(c);
				float s = saturation(c);
				float b = brightness(c);
				if (h > 180 && h < 270) {
					if (b > maxGreen) {
						maxGreen = b;
						maxGreenX = x;
						maxGreenY = y;
					}
				}
			}
		}

		

		// Vérifie qu'on a bien trouvé un point vert
		if (maxGreen > 0) {
			// Afficher l'image du Tux
			lastX = maxGreenX;
			lastY = maxGreenY;
		} else {

			// On n'a pas trouvé de point vert, on cherche dans toute l'image
			initialized = false;
			noGreen++;
			if (noGreen > 10) {
				// On n'a pas trouvé de point vert depuis 10 frames, on réinitialise
				initialized = false;
			}

		}

	} else {

		// Chercher le point le plus vert dans toute l'image
		for (int x = 0; x < width; x++) {
			for (int y = 0; y < height; y++) {
				int loc = x + y * width;
				int c = webCam.pixels[loc];
				float h = hue(c);
				float s = saturation(c);
				float b = brightness(c);
				if (h > 180 && h < 270) {
					if (b > maxGreen) {
						maxGreen = b;
						maxGreenX = x;
						maxGreenY = y;
					}
				}
			}
		}

		if (maxGreen > 0) {
			// On a trouvé un point vert, on initialise
			initialized = true;
			lastX = maxGreenX;
			lastY = maxGreenY;
		}

	}

	// On dessine un cercle autour du point le plus vert
	stroke(255, 0, 0);
	strokeWeight(4);
	noFill();
	ellipse(lastX, lastY, 20, 20);

	// Placer l'image dans data "Tux.png" au point (maxGreenX, maxGreenY)
	image(tux, lastX - tux.width/2, lastY - tux.height / 2);



}

// Quand touche du clavier tapée, on inverse la camera
void keyPressed() {
	if (key == ' ') {
		reverseCam = !reverseCam;
	} else if (key == 'r') {
		initialized = false;
	}
}

// Fonction appelee lorsde la fermeture de la fenetre windows
// par un clic sur la croix de fermeture de la fenetre...
void exit() {
    println("ATTENTION : Le programme s'arrete, donc cloture WebCam !!");
    webCam.stop(); // Arret "propre" de la webcam
    super.exit();
}


