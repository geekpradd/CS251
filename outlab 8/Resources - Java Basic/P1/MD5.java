import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.io.File;
import java.math.BigInteger;

class MD5 {
    public static void main(String args[]) throws Exception {
        File file = new File("MD5sums");
        Scanner sc = new Scanner(file);
        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            int lastIndex = s.lastIndexOf("-");
            // String hash = s.substring(lastIndex + 1).trim();
            // String actual = s.substring(0, lastIndex).trim();
            String hash = s.substring(lastIndex + 2);
            String actual = s.substring(0, lastIndex-1);

            // System.out.println(hash);
            // System.out.println(actual);
            // System.out.println(getHash(actual));
            if(hash.equals(getHash(actual))){
                System.out.println("verified");
            }
            else 
                System.out.println("not verified");
        }
        sc.close();
    }

    public static String getHash(String actual) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] md5 = md.digest(actual.getBytes());
        BigInteger a = new BigInteger(1,md5);
        return String.format("%1$32s", a.toString(16));
    }
}