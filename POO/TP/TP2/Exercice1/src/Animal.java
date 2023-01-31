package TP2.Exercice1.src;

public abstract class Animal {
    
    private String name;

    public Animal(String name) {
        this.name = name;
    }
    
    @Override
    public String toString() {
        return name;
    }

    public String getName() {
        return name;
    }

}
