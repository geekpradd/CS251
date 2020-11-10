package readwrite;

public class tester {
    public static void main(String[] args) {
        ProtectedTree t = new ProtectedTree(new Tree());
        int x = 0;
        try {

        t.write(10);
        t.write(10);
        t.write(10);
        t.write(10);
        t.write(12);
        t.write(9);
        x  = t.read(10);
        System.out.println(x);
        x  = t.read(12);
        System.out.println(x);
        x  = t.read(12);
        System.out.println(x);
        x  = t.read(12);
        System.out.println(x);
        x  = t.read(12);
        System.out.println(x);
        x  = t.read(12);
        x  = t.read(15);
        } catch(InterruptedException e) {
            // Thread.currentThread().interrupt();
            e.printStackTrace();
        }
    } 
}
