// On va recréer paint pour android

color c = color(0, 255, 0);

color[] colors;

// On va créer 10 couleurs aléatoires


void setup() {
    
    fullScreen(P2D);
    
    
    // On met comme fond blanc
    background(255);
    
    noStroke();
    
    colors = new color[10];
    
    for (int i = 0; i < colors.length; i++) {
        
        colors[i] = color(random(255), random(255), random(255));
        
    }
    
}   

// Quand on touche l'écran, on dessine un cercle
void draw() {
    
    
    // On ajoute des touches pour changer la couleur
    // On affiche 10 cercles avec les couleurs aléatoires
    for (int i = 0; i < colors.length; i++) {
        
        fill(colors[i]);
        
        ellipse(50 + i * 50, 50, 40, 40);
        
    }
    
    // On rajoute un cercle noir pour effacer
    fill(0);
    
    ellipse(50 + 10 * 50, 50, 40, 40);
    
    
}

// Quand on presse l'écran, on relie le point précédent au point actuel
void mouseDragged() {
    
    if (mouseY > 100) {
        
        stroke(c);
        
        strokeWeight(10);
        
        line(mouseX, mouseY, pmouseX, pmouseY);
        
    }
    
}

// Si on touche un cercle, on change la couleur
void mousePressed() {
    
    for (int i = 0; i < colors.length; i++) {
        
        if (dist(mouseX, mouseY, 50 + i * 50, 50) < 20) {
            
            c = colors[i];
            
        }
        
    }
    
    // Si on touche le cercle noir, on efface
    if (dist(mouseX, mouseY, 50 + 10 * 50, 50) < 20) {
        
        background(255);
        
    }
    
}
