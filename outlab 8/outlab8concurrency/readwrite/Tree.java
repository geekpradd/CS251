package readwrite;

public class Tree {
    private int value;
    private Tree left;
    private Tree right; 
    private boolean is_empty;
    
    public Tree(){
        left = null;
        right = null;
        is_empty = true;
    }

    public void write(int n){
        if (is_empty){
            value = n;
            is_empty = false;
        }
        else {
            if (n < value){
                if (left == null){
                    left = new Tree();
                }
                left.write(n);
            }
            else if (n > value){
                if (right == null){
                    right = new Tree();
                }
                right.write(n);
            }
        }
    }

    public int read(int n){
        if (value == n){
            return value;
        }
        else if (n < value){
            if (left == null){
                return value;
            }
            return left.read(n);
        }
        else {
            if (right == null){
                return value;
            }
            return right.read(n);
        }
    }

}