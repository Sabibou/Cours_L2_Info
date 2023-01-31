package TP2.Exercice1.src;

public class Dog extends Animal {
    
    public Dog(String name) {
        super(name);
    }

    public void woof() {
        System.out.println("Woof!");
    }


    @Override
    public String toString() {
        return "Dog " + super.toString();
    }
    

}
