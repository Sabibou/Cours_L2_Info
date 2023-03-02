// On va faire un jeu (comme le dinosore de chrome)
class Monstre {

    private float x;
    private float y;

    public Monstre(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public void afficher() {
        fill(0);
        ellipse(x, y, 50, 50);
    }

    float getX() {
        return x;
    }

    float getY() {
        return y;
    }

}

ArrayList<Monstre> monstres = new ArrayList<Monstre>();

float g = 0.5; // gravité
float v = 0; // vitesse
float y = 0; // position

float speed;

float ticks = 0;
float timeBeforeNextMonstre = 3;

boolean saut = false;

int score = 0;

void setup() {

    fullScreen(P2D);

    y = height/2;

}

void draw() {

    background(255);

    if (saut) {
        v = -10;
        saut = false;
    }

    v += g;
    y += v;

    if (y > height/2) {
        y = height/2;
        v = 0;
    }

    fill(0);
    ellipse(width/4, y, 50, 50);

    // On fait apparaître un monstre toutes les 3s
    ticks += 1/frameRate;
    if (ticks > timeBeforeNextMonstre) {
        timeBeforeNextMonstre = random(0.2, 2);
        monstres.add(new Monstre(width, height/2));
        ticks = 0;

        score += 1;
    }

    for (int i = 0; i < monstres.size(); i++) {
        Monstre m = monstres.get(i);
        m.afficher();
        m.x -= speed;

        if (score%3==0) {
            speed += 0.4;
        }


        // Check collision  
        if (dist(m.getX(), m.getY(), width/4, y) < 50) {
            // On perd
            println("Perdu");
            exit();
        }

        if (m.x == 0) {
            // On supprime le monstre
            monstres.remove(i);
        }

    }

    fill(0);
    textSize(32);
    text("Score : " + score, 10, 30);

}

void mousePressed() {
    saut = true;
}