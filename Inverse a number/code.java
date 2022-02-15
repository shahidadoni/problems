import java.util.*;

public class Main{

 public static void main(String[] args) {
  // write your code here  
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();

    int inverse = 0;
    int index = 1;
    while(n != 0){
        int last_digit = n % 10;
        int inverse_digit = index;
        int inverse_index = last_digit;

        inverse = inverse + index * (int)Math.pow(10,last_digit-1);

        index++;
        n = n/10;
    }

    System.out.println(inverse);
 }
}