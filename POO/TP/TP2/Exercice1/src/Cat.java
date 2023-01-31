package TP2.Exercice1.src;

public class Cat extends Animal {
    
    public Cat(String name) {
        super(name);
    }

    public void meow() {
        System.out.println("Meow!");
    }

    @Override
    public String toString() {
        return "Cat " + super.toString();
    }

}
