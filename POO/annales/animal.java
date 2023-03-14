/**
 * test
 */
public interface animal {

    public void crier();

    public void manger();

    public void dormir();

}

public class chat implements animal {

    public void crier() {
        System.out.println("Miaou");
    }

    public void manger() {
        System.out.println("Je mange du poisson");
    }

    public void dormir() {
        System.out.println("Je dors dans un panier");
    }

}