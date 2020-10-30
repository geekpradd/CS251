package readwrite;
import java.io.*;
import java.util.Scanner;

public class ReaderWriter implements Runnable {
    private ProtectedTree tree;
    private String fname;
    private boolean isWriter;

    public ReaderWriter(String FILENAME, ProtectedTree ptree, boolean iswriter) {
        tree = ptree;
        fname = FILENAME;
        isWriter = iswriter;
    }
    public void run(){
        try{
            FileInputStream fs = new FileInputStream(fname);
            Scanner sc = new Scanner(fs);

            while (sc.hasNextLine()){
                if (isWriter){
                    tree.write(sc.nextInt());
                }
                else {
                    try {
                        tree.read(sc.nextInt());
                    }
                    catch (Exception e){
                        e.printStackTrace();
                    }
                    
                }
            }
            sc.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}