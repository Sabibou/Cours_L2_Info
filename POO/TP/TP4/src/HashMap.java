package TP4.src;

import java.util.ArrayList;

public class HashMap<K, V> {
    
    private int size;
    private ArrayList<K> keys;
    private ArrayList<V> values;

    public HashMap() {

        this.size = 0;
        this.keys = new ArrayList<K>();
        this.values = new ArrayList<V>();

    }
    
    public void put(K key, V value) {

        if (this.keys.contains(key)) {

            int index = this.keys.indexOf(key);
            this.values.set(index, value);

        } else {

            this.keys.add(key);
            this.values.add(value);
            this.size++;

        }

    }
    
    public V get(K key) {

        if (this.keys.contains(key)) {

            int index = this.keys.indexOf(key);
            return this.values.get(index);

        } else {

            return null;

        }

    }

    public void remove(K key) {

        if (this.keys.contains(key)) {

            int index = this.keys.indexOf(key);
            this.keys.remove(index);
            this.values.remove(index);
            this.size--;

        }

    }

    public int size() {

        return this.size;

    }

    public boolean containsKey(K key) {

        return this.keys.contains(key);

    }

    public boolean containsValue(V value) {

        return this.values.contains(value);

    }

    // Si c'est un int, on autorise le get
    public int getObject(K key) {

        // On vérifie le type
        if (this.values.get(0) instanceof Integer) {

            // On vérifie si la clé existe
            if (this.keys.contains(key)) {

                int index = this.keys.indexOf(key);
                return (int) this.values.get(index);

            } else {

                return -1;

            }

        } else {

            return -1;

        }

    }

}
