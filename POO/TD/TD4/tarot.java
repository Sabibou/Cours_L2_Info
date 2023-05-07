// Jeu de tarot
/* 

Les TODO sont à remplacer par du code,
Mais actuellement ce ne sont pas les algorithmes qui sont évalués
Donc on peut laisser vider.

*/


/**
 * Classe principale du Deck de cartes
 */
class Deck {

    private Card[] cards;
    private int nbCards;
    private int score;

    private final int BASE_CARDS = 78;

    /**
     * Constructeur par défaut
     */
    public Deck() {
        this.cards = new Card[BASE_CARDS];
        this.nbCards = 0;
        this.score = 0;
    }


    /**
     * Constructeur avec nombre de cartes
     * @param nbCards
     */
    public Deck(int nbCards) {
        
        if (nbCards > BASE_CARDS) {
            throw new IllegalArgumentException("Too many cards");
        } else if (nbCards < 0) {
            throw new IllegalArgumentException("Negative number of cards");
        }

        this.cards = new Card[nbCards];
        this.nbCards = 0;
        this.score = 0;
    }


    /**
     * Constructeur avec tableau de cartes
     * @param cards
     */
    public void addCard(Card card) {
        if (this.nbCards >= this.cards.length) {
            throw new IllegalStateException("Deck is full");
        }

        this.cards[this.nbCards] = card;
        this.nbCards++;

        this.score += card.getValue();
    }


    /**
     * Ajoute une carte au deck
     * @param card
     * @return la carte enlevée
     */
    public Card removeCard(int index) {
        if (index < 0 || index >= this.nbCards) {
            throw new IllegalArgumentException("Invalid index");
        }

        Card card = this.cards[index];

        for (int i = index; i < this.nbCards - 1; i++) {
            this.cards[i] = this.cards[i + 1];
        }

        this.nbCards--;

        this.score += card.getValue();

        return card;
    }


    /**
     * Retourne la carte à l'index donné
     * @param index
     * @return la carte
     */
    public Card getCard(int index) {
        if (index < 0 || index >= this.nbCards) {
            throw new IllegalArgumentException("Invalid index");
        }

        return this.cards[index];
    }

    /**
     * Retourne le nombre de cartes
     * @return le nombre de cartes
     */
    public int getNbCards() {
        return this.nbCards;
    }

    /**
     * Retourne le score du deck
     * @return le score
     */
    public int getScore() {
        return this.score;
    }


    /**
     * Mélange le deck (modifie le tableau)
     */
    public void shuffle() {
        // TODO
    }


    /**
     * Trie le deck (modifie le tableau)
     */
    public void sort() {
        // TODO
    }

    /**
     * Retourne le deck sous forme de chaîne de caractères
     */
    @Override
    public String toString() {
        // TODO
        return "";
    }

}

/**
 * Classe abstraite d'une carte
 */
public abstract class Card {

    private int value;

    /**
     * Constructeur par défaut
     * @param value
     */
    public Card(int value) {
        this.value = value;
    }

    /**
     * Retourne la valeur de la carte
     * @return la valeur
     */
    public int getValue() {
        return this.value;
    }

    /**
     * Retourne la version String de la carte
     * @return la version String
     */
    @Override
    public String toString() {
        // TODO
        return "";
    }

}

/**
 * Classe d'une carte à couleur
 * @see Suit
 */
public class SuitCard extends Card {

    /**
     * Enumération des couleurs
     */
    public final static enum SUIT {
        CLUBS, DIAMONDS, HEARTS, SPADES
    };

    private SUIT suit;


    /**
     * Constructeur par défaut
     * @param value
     * @param suit
     * @see Card
     */
    public SuitCard(int value, SUIT suit) {
        super(value);
        this.suit = suit;
    }

    /**
     * Retourne la couleur de la carte
     * @return la couleur
     */
    public SUIT getSuit() {
        return this.suit;
    }

    /**
     * Retourne la version String de la carte
     * @return la version String
     */
    @Override
    public String toString() {
        // TODO
        return "";
    }

}

/**
 * Classe d'une carte d'atout
 * @see Trump
 */
public class TrumpCard extends Card {

    /**
     * Enumération des atouts
     */
    public final static enum TRUMP {
        EXCUSE, TRUMP_1, TRUMP_21, TRUMP_20, TRUMP_19, TRUMP_18, TRUMP_17, TRUMP_16, TRUMP_15, TRUMP_14, TRUMP_13, TRUMP_12, TRUMP_11, TRUMP_10, TRUMP_9, TRUMP_8, TRUMP_7, TRUMP_6, TRUMP_5, TRUMP_4, TRUMP_3, TRUMP_2
    };

    private TRUMP trump;


    /**
     * Constructeur par défaut
     * @param value
     * @param trump
     * @see Card
     */
    public TrumpCard(int value, TRUMP trump) {
        super(value);
        this.trump = trump;
    }

    /**
     * Retourne l'atout de la carte
     * @return l'atout
     */
    public TRUMP getTrump() {
        return this.trump;
    }

    /**
     * Retourne la version String de la carte
     * @return la version String
     */
    @Override
    public String toString() {
        // TODO
        return "";
    }

}

/**
 * Classe d'une carte d'excuse
 * @see TrumpCard
 * @see Card
 */
public class FoolCard extends TrumpCard {

    /**
     * Constructeur par défaut
     * @param value
     * @see TrumpCard
     * @see Card
     */
    public FoolCard(int value) {
        super(value, TRUMP.EXCUSE);
    }

    /**
     * Retourne la valeur de la carte
     */
    @Override
    public int getValue() {
        return 0;
    }

    /**
     * Retourne la version String de la carte
     * @return la version String
     */
    @Override
    public String toString() {
        // TODO
        return "";
    }

}