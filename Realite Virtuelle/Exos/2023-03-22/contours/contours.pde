// On ouvre la webcam
// Convertir l'image en Noir et Blanc
// On va calculer le gradient

import processing.video.*;

Capture webCam;      // Declaration de la Capture par Camera
String[] cameras;    // Liste textuelle des webCams disponibles


float[][] convolutionMatrix; // Matrice du gradient

PImage bnwImage; // Image en noir et blanc

void setup() {
    
    size(640, 480);
    
    //On liste les webCams disponibles
    cameras = Capture.list();
    
    //On ouvre la premiere webCam
    webCam = new Capture(this, cameras[0]);
    webCam.start();

	//On initialise l'image en noir et blanc
	bnwImage = createImage(width, height, RGB);
    
}

void draw() {
    
    // On affiche l'image de la webcam
	if (webCam.available() == true) {
		webCam.read();
	}

	// On convertit l'image en noir et blanc et le stock dans bnwImage
	bnwImage = convertToBNW(webCam);


    // On initialise la matrice du gradient avec des valeurs pour un gradient en croix
    convolutionMatrix = new float[][]{
		{0, 1, 0},
		{1, -4, 1},
		{0, 1, 0}
	};

	bnwImage = seuillage(bnwImage, 140);

	bnwImage = stretching(bnwImage);

	// On applique le gradient
	bnwImage = convolution(bnwImage, convolutionMatrix);

	// // On fait un seuillage
	bnwImage = seuillage(bnwImage, 50);


	// On affiche l'image en noir et blanc
	image(bnwImage, 0, 0);

}
PImage stretching(PImage img) {

	int min = 255;
	int max = 0;

	// On parcourt l'image
	for (int x = 0; x < img.width; x++) {
		for (int y = 0; y < img.height; y++) {
			
			// On recupere la couleur de l'image d'origine
			int c = img.get(x, y);
			
			// On recupere les composantes RVB de la couleur
			float r = red(c);
			float g = green(c);
			float b = blue(c);
			
			// On calcule la moyenne des composantes RVB
			float moyenne = (r + g + b) / 3;

			if (moyenne < min) {
				min = (int) moyenne;
			}

			if (moyenne > max) {
				max = (int) moyenne;
			}
		}
	}
	
	// On cree une image de meme taille que l'image d'origine
	PImage stretchingImage = createImage(img.width, img.height, RGB);
	
	// Tout ce qui est en dessous de min devient noir, tout ce qui est au dessus de max devient blanc
	for (int x = 0; x < img.width; x++) {
		for (int y = 0; y < img.height; y++) {
			
			// On recupere la couleur de l'image d'origine
			int c = img.get(x, y);
			
			// On recupere les composantes RVB de la couleur
			float r = red(c);
			float g = green(c);
			float b = blue(c);
			
			// On calcule la moyenne des composantes RVB
			float moyenne = (r + g + b) / 3;
			
			// On cree une couleur avec la moyenne des composantes RVB
			int c2;
			if (moyenne < min) {
				c2 = color(0, 0, 0);
			} else if (moyenne > max) {
				c2 = color(255, 255, 255);
			} else {
				c2 = color(moyenne, moyenne, moyenne);
			}
			
			// On affecte la couleur a l'image en noir et blanc
			stretchingImage.set(x, y, c2);
		}
	}

	// On retourne l'image en noir et blanc
	return stretchingImage;

}

PImage seuillage(PImage img, int seuil) {
	
	// On cree une image de meme taille que l'image d'origine
	PImage seuillageImage = createImage(img.width, img.height, RGB);
	
	// On parcourt l'image
	for (int x = 0; x < img.width; x++) {
		for (int y = 0; y < img.height; y++) {
			
			// On recupere la couleur de l'image d'origine
			int c = img.get(x, y);
			
			// On recupere les composantes RVB de la couleur
			float r = red(c);
			float g = green(c);
			float b = blue(c);
			
			// On calcule la moyenne des composantes RVB
			float moyenne = (r + g + b) / 3;
			
			// On cree une couleur avec la moyenne des composantes RVB
			int c2;
			if (moyenne > seuil) {
				c2 = color(255, 255, 255);
			} else {
				c2 = color(0, 0, 0);
			}
			
			// On affecte la couleur a l'image en noir et blanc
			seuillageImage.set(x, y, c2);
		}
	}
	
	// On retourne l'image en noir et blanc
	return seuillageImage;
}


PImage convolution(PImage img, float[][] filter) {
	
	// On cree une image de meme taille que l'image d'origine
	PImage convolutionImage = createImage(img.width, img.height, RGB);
	
	// On calcule la convolution à partir de la matrice
	for (int x = filter.length / 2; x < img.width - filter.length / 2; x++) {
		for (int y = filter[0].length / 2; y < img.height - filter[0].length / 2; y++) {

			int norme = 0;

			for (int i = 0; i < filter.length; i++) {
				for (int j = 0; j < filter[i].length; j++) {
					int c = img.get(x + i - filter.length / 2, y + j - filter[i].length / 2);
					float r = red(c);
					float g = green(c);
					float b = blue(c);
					float moyenne = (r + g + b) / 3;
					norme += moyenne * filter[i][j];
				}
			}

			norme = abs(norme);

			// On cree une couleur avec la moyenne des composantes RVB
			int c2 = color(norme, norme, norme);

			// On affecte la couleur a l'image en noir et blanc
			convolutionImage.set(x, y, c2);

		}
	}
	
	// On retourne l'image en noir et blanc
	return convolutionImage;
}

// Fonction qui convertit une image en noir et blanc
PImage convertToBNW(PImage img) {
	
	// On cree une image de meme taille que l'image d'origine
	PImage bnwImage = createImage(img.width, img.height, RGB);
	
	// On parcourt l'image
	for (int x = 0; x < img.width; x++) {
		for (int y = 0; y < img.height; y++) {
			
			// On recupere la couleur de l'image d'origine
			int c = img.get(x, y);
			
			// On recupere les composantes RVB de la couleur
			float r = red(c);
			float g = green(c);
			float b = blue(c);
			
			// On calcule la moyenne des composantes RVB
			float moyenne = (r + g + b) / 3;
			
			// On cree une couleur avec la moyenne des composantes RVB
			int c2 = color(moyenne, moyenne, moyenne);
			
			// On affecte la couleur a l'image en noir et blanc
			bnwImage.set(x, y, c2);
		}
	}
	
	// On retourne l'image en noir et blanc
	return bnwImage;
}