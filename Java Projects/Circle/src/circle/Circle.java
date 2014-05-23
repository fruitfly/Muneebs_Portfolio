/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package circle;

import javax.swing.JFrame;
import java.io.*;
import java.awt.*;
 
/**
 *
 * @author ahmem9877
 */
public class Circle extends JFrame{

    
    int xCenter;
    int yCenter;
    int radius;
    
    public Circle (int x , int y, int r){
        xCenter= x;
        yCenter = y;
        radius = r;
        
        
    }
    
    public double getArea(){
        double area = Math.PI*Math.pow(this.radius, 2);
        return area;
        
    }
    
    public void drawMe (Graphics g, Color c){
        
        g.setColor(c);
        g.drawOval(this.xCenter-radius, this.yCenter-radius, radius*2, radius*2);
    }
    
    public boolean containsPoint (int x, int y){
        double distancefromcenter = Math.sqrt(Math.pow(this.xCenter-x, 2)+Math.pow(this.yCenter-y, 2));
        if (distancefromcenter>this.radius){
            return false;
        }
        else{
            return true;
        }
    }
    public boolean containsCircle (Circle c2){
        return true;
        
    }
    
//    public Point pointAtAngle (double theta){
//           return; 
//    }
    
    public double getCircumference (){
        return 2*Math.PI*this.radius;
    }
   
}
