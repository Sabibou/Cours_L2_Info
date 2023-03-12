public class Indecision {

    
    public static void main(String[] args) {
        System.out.println(decision());
    }

    static String decision() {
        try {
            return "to be";
        } finally {
            return "not to be";
        }
    }
}