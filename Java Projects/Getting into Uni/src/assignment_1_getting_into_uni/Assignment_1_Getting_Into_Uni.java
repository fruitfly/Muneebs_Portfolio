/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment_1_getting_into_uni;

import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileWriter;
/**
 *
 * @author ahmem9877
 */

/* this program does not output anything to the console.There are two text files names Acceptances and 
 Applicants in the directory that are the only things that get changed*/
public class Assignment_1_Getting_Into_Uni{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        FileReader applicants = new FileReader("Applicants.txt");
        Scanner scan = new Scanner(applicants);
        PrintWriter out = new PrintWriter(new FileWriter("Acceptances.txt"));
        
        while (scan.hasNext()){
            Boolean Accepted = false;
            String Firstname = scan.next();
            String Lastname = scan.next();
            int Average = scan.nextInt();
            int extracurriculars = scan.nextInt();
            int scoreontest = scan.nextInt();
            String Gr12Phy = scan.next();
            String Gr12Adv = scan.next();
            String Gr12eng =scan.next();
            String Gr12CS = scan.next();
            String MathContest = scan.next();
            
            if ((Average >= 90)){
                Accepted = true;                 
            }
            
            else if ((Average >= 85 && extracurriculars >=1)){
                Accepted = true;
                
                
            }
            else if (Average>=70 && scoreontest >= 5 && Gr12Phy.equals("yes")){
                Accepted = true;
            }
            else if ((Average>=60 && Gr12Adv.equals("yes")&& MathContest.equals("yes") && extracurriculars>=4)){
                Accepted = true;
            }
            if (Accepted){
                out.println("Congratulations " + Firstname + " " + Lastname + ", you have been accepted into the University of Awesome!");
            }
            else if (Accepted==false) {
                out.println("Sorry " + Firstname + " " + Lastname + ", you have been rejected from the University of Awesome.");
            }
        } out.close();
    }
}
