package TP2.Exercice1.src;

public class Main {
    
    public static void main(String[] args) {
        
        Dog medor = new Dog("Medor");
        Cat felix = new Cat("Felix");

        medor.woof();
        felix.meow();

        ((Cat) felix).meow(); // Ew
        ((Dog) medor).woof(); // Ew

    }

}
