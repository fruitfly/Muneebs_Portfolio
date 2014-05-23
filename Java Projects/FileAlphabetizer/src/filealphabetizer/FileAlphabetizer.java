/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package filealphabetizer;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;

/**
 *
 * @author ahmem9877
 */
/* this program takes ina bunch of strings from a text file and orders them alphabetically */
public class FileAlphabetizer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {
        // TODO code application logic here
        FileReader file = new FileReader("Input.txt");
        Scanner s = new Scanner(file);
        int numwords  = s.nextInt();
        String[] array  = new String[numwords];
        for (int i=0; i<array.length;i++){
            array[i] = s.next();
            
            
        }
        bubbleSort(array);
        for (int i=0; i<array.length;i++){
            System.out.println(array[i]);
            
            
        }
        
        
        
        
    }
    
    public static String[] bubbleSort( String[] a ){
        String s1;
        String s2;
        for (int i = 1; i <a.length;i++){
            for (int j = 0;j<a.length-i;j++){
                s1 = a[j];
                s2 = a[j+1];
                if (s1.compareTo(s2)>0){
                    swap(j,j+1,a);
                    
                }
            }
        }
        return a;
    }
    public static String[] swap (int i , int j, String[] a){
        String temp  = a[i];
        a[i] = a[j];
        a[j] = temp;
        return a;
        
    }
}
