/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package divide_by_3;

import java.util.Scanner;

/**
 *
 * @author ahmem9877
 */
public class Divide_By_3 {

    /**
     * @param args the command line arguments
     */
    
    
    public static boolean isDivby3 (int n){
        
        if (n>10){
            if (n==6||n==9||n==3){
                    return true;
             }
             else{
                 return false;
                }
        }
        
        else{
            int sumDigits = sumDigits(n);
            
            return isDivby3(sumDigits);
        }
    }
    
    public static int sumDigits (int n){
        
        String num = Integer.toString(n);
        int sum=0;
        for (int i = 0; i<num.length();i++){
            sum+= Integer.valueOf(num.substring(i, i+1));
        }
        
        return sum;
        
        
        
    }
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number that you think can be divisible by 3: ");
        int i = s.nextInt();
        System.out.println(isDivby3(i));
        
    }
}
