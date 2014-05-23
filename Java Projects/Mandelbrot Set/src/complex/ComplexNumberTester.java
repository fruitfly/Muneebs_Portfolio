/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package complex;

/**
 *
 * @author ahmem9877
 */
public class ComplexNumberTester {
    
    public static void main(String args[]){
        
        Complex f1 = new Complex(2,0);
        f1.display();
        Complex f2 = f1.multbyScalar(4);
        f2.display();
        
        Complex f3 = f1.addorsubtract(f2, false);
        f3.display();
        
        f1.multiplication(f2).display();
        System.out.println(f1.absoluteValue());
        f1.conjugate().display();
        
        Complex f4 =f1.complexpow(6);
        f4.display();
        
        
        
       
    }
}
