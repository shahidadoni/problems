import java.util.*;
   
   public class Main{
   
   public static void main(String[] args) {
     // write your code here  
     Scanner scn = new Scanner(System.in);
     int n = scn.nextInt();
     int k = scn.nextInt();

     int temp = n;
     int length = 0;
     while(temp>0){
       temp /= 10;
       length++;
     }

     k = k % length;
     if(k<0){
       k = k + length;
     }

     int divisor = 1;
     int mult = 1;

     for(int i = 1; i<= length;i++){
       if(i<=k){
         divisor *= 10;
       }else{
         mult *= 10;
       }
     }

     int quotient = n / divisor;
     int remainder = n % divisor;

     int rotatedNumber = remainder * mult + quotient;

     System.out.println(rotatedNumber);



    }
   }