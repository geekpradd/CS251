import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.List;
import java.util.stream.Collectors;
public class Sieve{
    static IntStream num;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        num = IntStream.range(2,n+1);
        IntStream num2 = IntStream.range(2,n+1);
        num2.map(p -> {
            num = num.filter(i -> (i%p!=0)||(i==p));
            return p;
        }).reduce(0, (x,y) -> x=x);
        String prime = num.mapToObj(p->Integer.toString(p)).collect(Collectors.joining(" "));
        System.out.println(prime);
    }
}