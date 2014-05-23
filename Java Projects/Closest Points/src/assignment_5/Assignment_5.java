/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment_5;

import java.awt.Point;

/**
 *
 * @author ahmem9877
 */

/* This program generates an array of random points and then determines the two points that are 
 the closest together*/
public class Assignment_5 {
    
    
    
    public static void  printFarthestApart (Point[] a){
        double maxDistance = 0;
        int comparisions = 0;
        double Dist;
        int index1 = 0;
        int index2  = 0;
        for(int i =1; i<a.length ; i++){
            for (int j =0; j<a.length-i; j++){
                Dist = getDist(a[i], a[j]);
                if (Dist>maxDistance){
                        maxDistance = Dist;
                        index1 = i;
                        index2 = j;
                }
                comparisions += 3;
                
            }
        }
        
        System.out.println("The Points that are the farthest apart are " + "(" + a[index1].x + "," + a[index1].y +  ")" + " and " + "(" +  a[index2].x + "," + a[index2].y + ")" +  " at  a distance of " + maxDistance);
        System.out.println("The number of comparisions done: " + comparisions);
        
    }
    
    public static double  getDist (Point a, Point b){
        double x1 = a.getX();
        double y1 = a.getY();
        double x2 = b.getX();                                                                                                                                                                                                                                                                                                                   
        double y2 = b.getY();
        
        double dist = Math.sqrt(Math.pow(x2-x1,2) + Math.pow(y2-y1, 2));
        
        
        
        return dist;
        
    }
    
    public  static Point[] generateRandPoints (Point[] a){
        for (int i = 0; i<a.length; i++){
            int newX =  (int)(Math.random()*200);
            int newY =  (int)(Math.random()*200);
            Point p = new Point( newX, newY);
            a[i]= p;
            
            
        }
        return a;
    }
    
   
    public static void main(String[] args) {
        
        
        Point[] orderedPairs = new Point[300];
        
        
         
        orderedPairs = generateRandPoints(orderedPairs);
        
        printFarthestApart(orderedPairs);
        
        
        
        
        
    }
}
