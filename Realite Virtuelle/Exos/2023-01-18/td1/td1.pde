/****************************************************************************/
/*  MESNARD Emmanuel                                              ISIMA     */
/*                                                                          */
/*              T D 1   d e   R e a l i t e   V i r t u e l l e             */
/*        Creation d'images, par souris, generees par la mecanique des      */
/*        fluides (librairie MSA : https://github.com/memo/p5-MSAFluid)     */
/*                         (http://www.memo.tv/msafluid_for_processing)     */
/*                                                                          */
/* MouseFluid.pde                                      Processing 3.5.1     */
/****************************************************************************/

// *************************  MODE d'EMPLOI **********************************
//
//         Brassage d'un fluide colore par souris
//
// ***************************************************************************

// Importation des librairies
import msafluid.*;            // MSAFluid

// Declaration des variables globales
// **********************************
float invWidth, invHeight; // Inverse des dimensions de la fenetre
float aspectRatio, aspectRatio2;

float colorFactor = 30.0f; // Facteur de conversion en couleur RGB

// ** Mecanique des fluides et particules
// Constantes sur les caracteristiques du solveur 2D et de son fluide 
final float FADE_SPEED = 0.003; // Vitesse d'effacement du fluide (0.003);
final float DELTA_T = 0.5; // Periode de calcul du solveur (0.5)
final float VISC = 0.0001; // Viscosite du fluide (0.0001)
// Dimensions de la zone de calcul du fluide par le solveur
final int FLUID_WIDTH = 120; // Largeur de la zone de calcul pour le fluide (120)
int FLUID_HEIGHT; // La hauteur est proportionnelle au ratio de la fenetre


MSAFluidSolver2D fluidSolver;  // Solveur de calcul du fluide
ParticleSystem particleSystem; // Systeme de particules

PImage imgFluid; // Image generee

// Fonction d'initialisation de l'application - executee une seule fois
void setup() {
    //Initialisation des parametres graphiques utilises
    size(640, 480, P2D);
    surface.setTitle("MouseFluid : Fluide par Souris - E. Mesnard / ISIMA");
    //Calcul de l'aspect de la fenetre et des ratios
    invWidth = 1.0f / width;
    invHeight = 1.0f / height;
    aspectRatio = width * invHeight;
    aspectRatio2 = aspectRatio * aspectRatio;
    
    //Creation du fluide avec ses parametres
    //Solveur travaillant sur une zone plus petite (mais de meme ratio que la fenetre)
    //La hauteur est proportionnelle au ratio de la fenetre
    FLUID_HEIGHT = (int)(FLUID_WIDTH / aspectRatio); 
    fluidSolver = new MSAFluidSolver2D(FLUID_WIDTH, FLUID_HEIGHT);
    fluidSolver.enableRGB(true)
       .setFadeSpeed(FADE_SPEED)
       .setDeltaT(DELTA_T)
       .setVisc(VISC);
    
    //Creation d'une image (buffer) pour contenir le fluide
    imgFluid = createImage(fluidSolver.getWidth(), 
        fluidSolver.getHeight(), RGB);
    
    //Creation du systeme de particules
    particleSystem = new ParticleSystem();
}


// Fonction de re-tracage de la fenetre - executee en boucle
void draw() {
    //Declaration des variables locales
    int i; // indice des boucles
    int facteurCouleur; // facteur de conversion en couleur RGB
    
    //Initialisation 
    facteurCouleur = 5;
    
    //Mise a jour des fluides
    fluidSolver.update();
    
    // Creation de l'image du fluide
    // On ajoute le coefficient de conversion en couleur
    // Il permet de varier la couleur du fluide
    // On utilise le module 255 pour eviter les valeurs trop grandes
    for (i = 0; i < fluidSolver.getNumCells(); i++) {
        imgFluid.pixels[i] = color(
            (fluidSolver.r[i] * colorFactor) % 255,
            (fluidSolver.g[i] * colorFactor) % 255,
            (fluidSolver.b[i] * colorFactor) % 255);
    }  
    imgFluid.updatePixels();
    
    //Affichage de cette image, avec zoom pour remplir la fenetre
    image(imgFluid, 0, 0, width, height);
    
    //Mise a jour et trace du systeme de particules
    particleSystem.updateAndDraw();
    
    //Prise en compte possible du redimensionnement "Full Screen"
    invWidth = 1.0f / width; // Recalcul des ratios pour la souris
    invHeight = 1.0f / height;
    
    text("Color Factor : " + colorFactor, 10, 20);
}

// intégrer le clic droit : flag de gestion du tracé couleur
void mousePressed() {
    
    if (mouseButton == RIGHT) {
        
        addForce(mouseX * invWidth, mouseY * invHeight, 0, 0);
        
    }
    
}

// Gestion du clavier
void keyPressed() {
    switch(key) { // Lors d'un appui sur la barre espace
        case' ' : println(frameRate); // Affichage de la vitesse (Nb images / seconde)
        break;
    }
}

// Gestion de la souris
void mouseMoved() {
    float mouseNormX = mouseX * invWidth;
    float mouseNormY = mouseY * invHeight;
    float mouseVelX = (mouseX - pmouseX) * invWidth;
    float mouseVelY = (mouseY - pmouseY) * invHeight;
    
    addForce(mouseNormX, mouseNormY, mouseVelX, mouseVelY);
}



void mouseWheel(MouseEvent event) { // La valeur de la molette doit modifier le facteurCouleur
    
    // On récupère la valeur de la molette et on l'ajoute au facteurCouleur ([-1, 1])
    colorFactor += event.getCount();
    
    // On s'assure que le facteurCouleur reste dans l'intervalle [1, 255] (pour éviter les divisions par 0)
    colorFactor = (colorFactor < 1) ? 1 : (colorFactor > 255) ? 255 : colorFactor;
    
}


// add force and dyeto fluid, and create particles
void addForce(float x, float y, float dx, float dy) {
    float speed = (dx * dx  + dy * dy) * aspectRatio2;    // balance the x and y components of speed with the screen aspect ratio
    
    if (speed > 0) {
        if (x < 0) x = 0; 
        else if (x > 1) x = 1;
        if (y < 0) y = 0; 
        else if (y > 1) y = 1;
        
        int index = fluidSolver.getIndexForNormalizedPosition(x, y);
        
        color drawColor;
        
        colorMode(HSB, 360, 1, 1);
        float hue = ((x + y) * 180 + frameCount) % 360;
        drawColor = color(hue, 1, 1);
        colorMode(RGB, 1);  
        
        fluidSolver.rOld[index]  += red(drawColor) * colorFactor;
        fluidSolver.gOld[index]  += green(drawColor) * colorFactor;
        fluidSolver.bOld[index]  += blue(drawColor) * colorFactor;
        
        particleSystem.addParticles(x * width, y * height, 10);
        fluidSolver.uOld[index] += dx * colorFactor;
        fluidSolver.vOld[index] += dy * colorFactor;
    }
}
