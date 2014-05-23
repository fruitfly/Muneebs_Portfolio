/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package complex;

import java.awt.Color;
import java.awt.Graphics;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import javax.swing.JFrame;
import static javax.swing.JFrame.EXIT_ON_CLOSE;

/**
 *
 * @author ahmem9877
 */
public class MandelBrot_Set extends JFrame{
    static double x1range;//must be larger than x2range
    static double y1range;//must be larger than y2range
    static double xaxissize;
    static double x2range;
    static double y2range;
    static double yaxissize;
    static int iterations;
    static int width=1024;
    static int height=1024;
    static double scaleX;
    static double scaleY;
    static int ab;
    static double zoomFactor = 2.5;
    
    
    public void getInfofromfile (String filename) throws IOException{
        File f = new File(filename);
        Scanner s = new Scanner(f);
        x2range = s.nextDouble();
        x1range = s.nextDouble();
        y2range = s.nextDouble();
        y1range = s.nextDouble();
        iterations = s.nextInt();
        xaxissize = Math.abs(x1range-x2range);//size of the x and y axis determined by the user input
        yaxissize = Math.abs(y1range-y2range);
        scaleX= (width/xaxissize);//used to scale the coordinates on the screen
        scaleY = (height/yaxissize);
        
        
        
        
    }
    public int isInMandelbrotSet (Complex c){
       Complex z = c;
        ab = iterations;
       while(Math.pow(z.coefficient, 2)+Math.pow(z.constant, 2) <4 ){
           z = z.complexpow(2).addorsubtract(c,true);
           ab--;
           if (ab==0){
                return ab;
            } 
       
            }
       return ab;
    }
    
    //draws the current generation of living cells on the screen
    
    public void paint(Graphics g) {
        int x,y;
        int tries;
        for (double i=x2range; i<=x1range;i+=0.001){
            
            for (double a = y2range; a<=y1range;a+=0.001){
                
                Complex r = new Complex (i,a);
                tries = isInMandelbrotSet(r);
                if (tries>255){
                    tries=255;
                }
                Color RGB  = new Color(tries,tries,tries);   //sets the color based on how many tries the isInMandelbrotSet method went through
                x= (int)(scaleX*zoomFactor*(i)+(width/2));//translating the coordinates onto the screen
                y = (int)(scaleY*zoomFactor*(a))+(height/2);
                g.setColor(RGB);//drawing the line
                g.drawLine(x,y , x+1, y+1);
                    
                
                
                    
                    
                    
                    
                    
                    
                
                
                /*else if ((ab/iterations)*100<=10){
                    x= (int)(scaleX*(i)+(width/2));//translating the coordinates onto the screen
                    y = (int)(scaleY*(a))+(height/2); 
                    g.setColor(Color.LIGHT_GRAY);
                    g.drawLine(x,y , x+1, y+1);
                }*/
            }
        }

    }


    //sets up the JFrame screen
    public void initializeWindow() {
        
        setTitle("MandelBrot Set");
        setSize(width, height);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setBackground(Color.white);
        setVisible(true);
    }
    public static void main(String args[]) throws IOException{
        MandelBrot_Set newset = new MandelBrot_Set();
        newset.getInfofromfile("Input.txt");
        System.out.println(y2range);
        System.out.println(x2range);
        System.out.println(x1range);
        System.out.println(y1range);
        System.out.println(scaleX);
        System.out.println(scaleY);
        newset.initializeWindow();
        
        
        
    }
    
}
