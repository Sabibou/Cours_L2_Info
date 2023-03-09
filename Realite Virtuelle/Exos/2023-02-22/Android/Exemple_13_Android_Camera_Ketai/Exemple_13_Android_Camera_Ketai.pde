class Plateforme {
    
    private float plateformeSizeX;
    private float plateformeSizeY;
    private float plateformePosX;
    private float plateformePosY;
    private float layer;
    private int direction;
	private float[] ocolor;
    
    private final float CENTER_MARKER_SIZE = 80; // <=> 8cm
    
    public Plateforme(int direction, float layer) {
        
        this.plateformeSizeX = 80;
    	this.plateformeSizeY = 80;
    	this.plateformePosX = 0;
    	this.plateformePosY = 0;
        
        this.direction = direction;
        this.layer = layer;

		ocolor = new float[3];

		ocolor[0] = random(255);
		ocolor[1] = random(255);
		ocolor[2] = random(255);
        
    }

	public Plateforme(int direction, float layer, float plateformeSizeX, float plateformeSizeY, float plateformePosX, float plateformePosY) {
		this.plateformeSizeX = plateformeSizeX;
		this.plateformeSizeY = plateformeSizeY;
		this.plateformePosX = plateformePosX;
		this.plateformePosY = plateformePosY;
		this.direction = direction;
		this.layer = layer;


		ocolor = new float[3];

		ocolor[0] = random(255);
		ocolor[1] = random(255);
		ocolor[2] = random(255);
	}
    
    public void draw() {
        
        // Height est le numéro de la couche (une couche = 3cm = 30u)
        // On va placer la plateforme à la bonne hauteur et à la bonne position
        // (en3 dimensions)
        
        // D'abord on se déplace à la bonne hauteur, puis on se déplace à la bonne position
        	translate(0, 0, layer * 3);
        	translate(plateformePosX, plateformePosY, 0);
        
        // On dessine la plateforme

		fill(this.ocolor[0], this.ocolor[1], this.ocolor[2]);

        box(plateformeSizeX, plateformeSizeY, 3);
        
    }
    
    public void update() {
        
        // On a 4 directions possibles, x+, x-, y+, y-
        // On déplace la plateforme 
        // Si la direction est 0 ou 1 on fera sur l'axe X, sinon sur l'axe Y
        // Si la direction est 0 ou 2 on fera un déplacement positif, sinon négatif
        	if (direction == 0 || direction == 1) {
            		plateformePosX += (direction == 0 ? 1 : - 1) * 2;
        	} else{
            		plateformePosY += (direction == 2 ? 1 : - 1) * 2;
        	}
        
        // Si la position est située à 10u du centre du marqueur, on change de direction
        	if (plateformePosX > CENTER_MARKER_SIZE / 2 || plateformePosX < - CENTER_MARKER_SIZE / 2) {
            		if (direction == 0) {
                			direction = 1;
            		} else if (direction == 1) {
                			direction = 0;
            		} else if (direction == 2) {
                			direction = 3;
            		} else if (direction == 3) {
                			direction = 2;
            		}
        	} else if (plateformePosY > CENTER_MARKER_SIZE / 2 || plateformePosY < - CENTER_MARKER_SIZE / 2) {
            		if (direction == 0) {
                			direction = 1;
            		} else if (direction == 1) {
                			direction = 0;
            		} else if (direction == 2) {
                			direction = 3;
            		} else if (direction == 3) {
                			direction = 2;
            		}
        	}
        	
    }

	public float getPlateformeSizeX() {
		return plateformeSizeX;
	}

	public void setPlateformeSizeX(float plateformeSizeX) {
		this.plateformeSizeX = plateformeSizeX;
	}

	public float getPlateformeSizeY() {
		return plateformeSizeY;
	}

	public void setPlateformeSizeY(float plateformeSizeY) {
		this.plateformeSizeY = plateformeSizeY;
	}

	public float getPlateformePosX() {
		return plateformePosX;
	}

	public void setPlateformePosX(float plateformePosX) {
		this.plateformePosX = plateformePosX;
	}

	public float getPlateformePosY() {
		return plateformePosY;
	}

	public void setPlateformePosY(float plateformePosY) {
		this.plateformePosY = plateformePosY;
	}

	public float getLayer() {
		return layer;
	}

    
    
}

// On va faire une classe qui contient le jeu
class Jeu {
    //On va définir les variables de la classe
    private int score;
    private ArrayList<Plateforme> plateformes;
	private final float CENTER_MARKER_SIZE = 80; // <=> 8cm
    
    public Jeu() {
        
        plateformes = new ArrayList<Plateforme>();
		plateformes.add(new Plateforme(0, 0));
        plateformes.add(new Plateforme(0, 1));
        
    }
    
    public void update() {
        
        // On a 4 directions possibles, x+, x-, y+, y-
        // On déplace la plateforme 
        // On déplace que la dernière
        	plateformes.get(plateformes.size() - 1).update();
        
    }
    
    public void draw() {
        	
        	// On dessine la plateforme
        	for (Plateforme p : plateformes) {
            		p.draw();
        	}
        	
    }

	public void placePlateforme() {
        
		// Il faut crop la dernière plateforme pour qu'elle puisse être empilée avec son antécédent
		// On va donc récupérer la dernière plateforme
		Plateforme currentPlateforme = plateformes.get(plateformes.size() - 1);
		Plateforme previousPlateforme = plateformes.get(plateformes.size() - 2);


		// On va créer une nouvelle plateforme de la même taille que la dernière
		// mais à une position différente
		int newDir = (int) random(4);
		Plateforme newPlateforme = new Plateforme(newDir, currentPlateforme.getLayer() + 1, currentPlateforme.getPlateformeSizeX(), currentPlateforme.getPlateformeSizeY(), currentPlateforme.getPlateformePosX(), currentPlateforme.getPlateformePosY());

		// On ajoute la nouvelle plateforme à la liste
		plateformes.add(newPlateforme);
        
    }
    
}


/****************************************************************************/
/*  MESNARD Emmanuel                                              ISIMA     */
/*                                                                          */
/*        Utilisation d'une des cameras (avec Ketai) sous Android           */
/*  infos supplementaires : http://ketai.org/reference/camera/ketaicamera/  */
/*                                                                          */
/* Exemple_13_Android_Camera_Ketai.pde         Processing 3.5.4 - ANDROID   */
/****************************************************************************/

// Import bibliotheques
import ketai.camera.*;

// Declaration des variables globales
KetaiCamera cam; // Camera
int nbCamera;
Boolean plusieursCamera;
PImage ImageCourante;

import jp.nyatla.nyar4psg.*;   // ARToolKit (version 3.0.7)

// Declaration des variables globales
MultiMarker sceneMM; // Scene de recherche de "multi-marqueur"

Jeu jeu;

// Fonction d'initialisation de l'application - executee une seule fois
void setup() {
    fullScreen(P3D);
    orientation(LANDSCAPE); // Forcage du mode
    
    //Gestion du mode d'affichage
    imageMode(CENTER); // Mode centre pour garantir que l’image sera visible
    textAlign(CENTER, CENTER);
    textSize(displayDensity * 25); // Parametrage de la police pour etre lisible
    
    //Ouverture du systeme de gestion des cameras a 24 fps 
    cam = new KetaiCamera(this, 1280, 720, 30);
    if (cam != null) {
        nbCamera = cam.getNumberOfCameras();
        plusieursCamera = (nbCamera>1);
    }
    
    
    sceneMM = new MultiMarker(this, 1280, 720,
        "camera_para.dat",
        NyAR4PsgConfig.CONFIG_PSG);
    
    //Declaration du marqueur a rechercher, avec sa dimension en mm
    sceneMM.addARMarker("Marqueur_ISIMA.patt", 80); // Marqueur numero 0
    
    jeu = new Jeu();
}

void draw() {
    if (cam != null && cam.isStarted()) {
        // La camera fonctionne correctement
        image(cam, width / 2, height / 2, width, height); // restitution en plein ecran, centree 
        
        
        
        
        if (sceneMM.isExist(0)) { // Marqueur ISIMA
            // Le marqueur est detecte dans le flux video
            // Changement de repere pour tracer en coordonnees "Marqueur"
            sceneMM.beginTransform(0); // Modification graphique sur marqueur 0
            // trace d'un rectangle 2D : rect(-40,-40,80,80);
            // ...ou mieux, trace d'un cube 3D :
            jeu.update();
            jeu.draw();
            
            sceneMM.endTransform();
        }
        
    } else {
        //Elle est eteinte (ou absente...)
        background(#D16363);
        text("!!Camera eteinte !!", width / 2, height / 2);
    }
}

void onCameraPreviewEvent() {
    cam.read(); // Lecture d'une image
	sceneMM.detect(cam);   // Recherche du marqueur dans la scene
}

void mousePressed() {
    //Analyse des boutons appuyes
    
    if (mouseY < 100) {
        // On ne regarde quedans le bandeau Haut
        if (cam.isStarted()) {
            cam.stop();
        } else {
            cam.start();
        }
    } else {
		jeu.placePlateforme();
	}

}