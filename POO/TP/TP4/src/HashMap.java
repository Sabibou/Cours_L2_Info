package TP4.src;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Objects;

public class HashMap<K, V> {
    
    // On stock les éléments dans un tableau de listes
    private int size;
    private ArrayList<Pair>[] table;

    class Pair {
        private K key;
        private V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    @SuppressWarnings("unchecked")
    public HashMap(int size) {
        this.size = size;
        table = new ArrayList[size];

        for (int i = 0; i < size; i++) {
            table[i] = new ArrayList<Pair>();
        }
    }

    public void put(K key, V value) {

        if (key == null) {
            throw new IllegalArgumentException("Key cannot be null");
        }

        int hash = key.hashCode() % size;

        if (Objects.isNull(table[hash])) {
            table[hash] = new ArrayList<Pair>();
        }

        table[hash].add(new Pair(key, value));
    }
    
    public V get(K key) {
        // getEntry
        int hash = key.hashCode() % size;

        if (Objects.isNull(table[hash])) {
            return null;
        }

        for (Pair pair : table[hash]) {
            if (pair.getKey().equals(key)) {
                return pair.getValue();
            }
        }

        return null;
    }

    public boolean contains(K key) {
        int hash = key.hashCode() % size;

        return !(Objects.isNull(table[hash]) || Objects.isNull(get(key)));
    }

    public boolean containsValue(V value) {
        for (ArrayList<Pair> list : table) {
            for (Pair pair : list) {
                if (pair.getValue().equals(value)) {
                    return true;
                }
            }
        }

        return false;
    }
    
    public void delete(K key) {
        int hash = key.hashCode() % size;

        if (Objects.isNull(table[hash])) {
            throw new IllegalArgumentException("Key not found");
        }

        table[hash].remove(key.hashCode() % size);
    }

    public int size() {

        return this.size();

    }

}
