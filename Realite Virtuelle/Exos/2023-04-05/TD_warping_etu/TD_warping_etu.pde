import java.util.*;

// Images 
PImage source;    // Source image
PImage warpedmarker;
PImage img_lissee;  // image lissée
PImage contours; //image seuillée des contours
PImage gradient;  // image de la norme du gradient
PImage gradnms;  // image du gradient après nms

String[] markersNames = {
    "Marqueur_ISIMA2.jpg",
    "Marqueur_ISIMA.jpg",
    "Marqueur_ISIMA3.jpg",
    "Marqueur_ISIMA4.jpg",
};

PImage[] markers = new PImage[markersNames.length];

// Paramètres hysteresis
int seuil_haut = 100;
int seuil_bas = 60;
// Paramètres hough
int thresholdHough = 80;
int stept = 1;
int stepr = 1;
// précalcul des sinus et cosinus pour gagner du temps :
int nt = int(180 / stept);
float[] costab = new float[nt];
float[] sintab = new float[nt];

//Taille marqueur
int markerWidth = 302;
int markerHeight = 302;


//**********************************************************
void setup() {
    size(640, 480);
    source = loadImage("./marqueur.jpg"); 

    for (int i = 0; i < markersNames.length; i++) {
        markers[i] = loadImage(markersNames[i]);
    }

    img_lissee = createImage(source.width, source.height, RGB);
    gradient = createImage(source.width, source.height, RGB);
    contours = createImage(source.width, source.height, RGB);
    gradnms = createImage(source.width, source.height, RGB);  
    //Opencv
    opencv = new OpenCV(this, source);
    warpedmarker = createImage(markerWidth, markerHeight, ARGB);  
    
    //précalcul des sinus et cosinus pour gagner du temps
    float theta = 0;
    for (int idt = 0; idt < nt;idt++) {
        theta = radians( -90 + idt * stept);
        costab[idt] = cos(theta);
        sintab[idt] = sin(theta);
    }
    
}


//**********************************************************
void draw() {  
    image(source,0,0);
    
    compute_contours(source, img_lissee, gradient, gradnms, contours); 
    
    //Transformée de Hough
    int[][] tab = compute_hough(contours,1,1);
    //Parcours de l'accumulateur pour récupérer les principales lignes
    Vector<droite> lines = compute_hough_lines(tab, thresholdHough);
    
    //********************************************
    ////Get the four contour lines
    //********************************************
    //A COMPLETER !
    
    droite[] markerLines = new droite[4];
    for (int k = 0;k < 4;k++) {
        //look for best line
        Iterator itr = lines.iterator(); 
        droite my_line = lines.get(0);
        
        markerLines[k] = my_line;
        
        while(itr.hasNext()) {
            my_line = (droite)itr.next();
            
            // On récupère les 4 meilleures droites (on compare par leur accumulateur "acc")
            if (my_line.acc > markerLines[k].acc) {
                markerLines[k] = my_line;
            }
            
            
        }
        
        //remove the line from the list
        lines.remove(markerLines[k]);
        
        color c = color(255, 0, 0);
        
        markerLines[k].display(c, source.width, source.height);
        
    }  
    
    
    
    //****************************************
    //Compute intersections to get corners
    //****************************************
    //ArrayList<PVector> points = new ArrayList<PVector>
    PVector[] corners = new PVector[4];    
    for (int k = 0;k < 4;k++) {    
        
        droite l1 = markerLines[k];
        droite l2 = markerLines[(k + 1) % 4];
        
        corners[k] = l1.intersection(l2);
        
    }
    
    // On affiche les coins
    for (int k = 0;k < 4;k++) {
        fill(255, 0, 0);
        ellipse(corners[k].x, corners[k].y, 10, 10);
        println(corners[k].x + " " + corners[k].y);
    }
    
    
    //*****************************************************************
    //Calcul du warping :
    //*****************************************************************
    
    PVector[] arranged_corners = new PVector[4]; 
    //A COMPLETER
    // opencv.toPImage(warpPerspective(arranged_corners, markerWidth, markerHeight), warpedmarker);
    // On a 4 points, on doit trouver les 4 coins dans l'ordre

    // On cherche le coin en haut à gauche
    for (int k = 0;k < 4;k++) {
        if (corners[k].x < source.width / 2 && corners[k].y < source.height / 2) {
            arranged_corners[1] = corners[k];
        }
    }

    // On cherche le coin en haut à droite
    for (int k = 0;k < 4;k++) {
        if (corners[k].x > source.width / 2 && corners[k].y < source.height / 2) {
            arranged_corners[0] = corners[k];
        }
    }

    // On cherche le coin en bas à droite
    for (int k = 0;k < 4;k++) {
        if (corners[k].x > source.width / 2 && corners[k].y > source.height / 2) {
            arranged_corners[3] = corners[k];
        }
    }

    // On cherche le coin en bas à gauche
    for (int k = 0;k < 4;k++) {
        if (corners[k].x < source.width / 2 && corners[k].y > source.height / 2) {
            arranged_corners[2] = corners[k];
        }
    }


    opencv.toPImage(warpPerspective(arranged_corners, markerWidth, markerHeight), warpedmarker);
    
    //*****************************************************************
    //Affichage
    //*****************************************************************
    //Wechanged the pixels in destination
    gradient.updatePixels();
    contours.updatePixels();
    // if (mousePressed && (mouseButton == RIGHT)) { // Si clic droit de la souris
    //     // Affiche le marqueur redressé
    //     image(contours,0,0);
    // }
    // else if (mousePressed && (mouseButton == LEFT)) { //Si clic gauche de la souris
    //     // Affiche les contours, les 4 droites principales et les coins
    //     image(warpedmarker,0,0);
    //     // ACOMPLETER
        
    // }

    warpedmarker = convertBNW(warpedmarker, 128);
    

    // On va comparer les différents marqueurs avec warpedmarker
    // On doit d'abord retailler les autres images pour qu'elles aient la même taille que warpedmarker
    for (int i = 0; i < 4; i++) {
        
        markers[i].resize(warpedmarker.width, warpedmarker.height);

        markers[i] = convertBNW(markers[i], 128);
    }

    // On va comparer les différents marqueurs avec warpedmarker
    PImage bestMarker = markers[0];
    float bestScore = 0;
    int index = 0;
    for (int i = 0; i < 4; i++) {
        float score = compareImages(warpedmarker, markers[i]);
        if (score < bestScore || bestScore == 0) {
            bestScore = score;
            bestMarker = markers[i];
            index = i;
        }
    }

    if (bestScore < 10) {

        // On affiche
        image(bestMarker, 0, 0);

        // On affiche le marqueur redressé
        image(warpedmarker, bestMarker.width, 0);

        println("Marqueur trouvé : " + bestScore + " " + markersNames[index]);

    }


}

PImage convertBNW(PImage im, int seuil) {

    PImage im1 = createImage(im.width, im.height, RGB);

    for (int i = 0; i < im.width; i++) {
        for (int j = 0; j < im.height; j++) {
            int c = im.get(i, j);
            int r = (int) (0.299 * red(c) + 0.587 * green(c) + 0.114 * blue(c));
            im1.set(i, j, color(r, r, r));
        }
    }

    return seuil(im1, seuil);

}

PImage seuil(PImage im1, int seuil) {

    for (int i = 0; i < im1.width; i++) {
        for (int j = 0; j < im1.height; j++) {
            int c = im1.get(i, j);
            if (red(c) > seuil) {
                im1.set(i, j, color(255, 255, 255));
            }
            else {
                im1.set(i, j, color(0, 0, 0));
            }
        }
    }

    return im1;

}

float compareImages(PImage im1, PImage im2) {

    // On calcule la différence entre les deux images
    // Les deux images sont en noir et blanc
    // On va calculer la moyenne des pixels dans une zone de 10x10
    float diff = 0;
    float moyenne = 0;
    float valIm1 = 0;
    float valIm2 = 0;

    for (int i = 5; i < im1.width - 5; i++) {
        for (int j = 5; j < im1.height - 5; j++) {
            
            moyenne = 0;

            for (int x = -5; x < 5; x++) {
                for (int y = -5; y < 5; y++) {

                    valIm1 = red(im1.get(i + x, j + y));
                    valIm2 = red(im2.get(i + x, j + y));

                    moyenne += sqrt(sq(valIm1 - valIm2));
                }
            }

            diff += moyenne / 100;

        }
    }

    diff = diff / (im1.width * im1.height);

    return diff;

}