/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package circle;

import java.awt.Graphics;

/**
 *
 * @author ahmem9877
 */
public class CircleTester {
    
   
    public static void main(String[] args) {
        // TODO code application logic here
        
        Circle c1 = new Circle(500,500,100);
        System.out.println(c1.getArea());
        System.out.println(c1.containsPoint(600, 700));
        
        
    }
}
