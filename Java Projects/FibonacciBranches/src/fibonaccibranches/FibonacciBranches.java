// The "BinaryTree" class.
package fibonaccibranches;

import java.awt.*;
import javax.swing.*;

public class FibonacciBranches extends JFrame
{
    static double degToRad = Math.PI / 180;
    static int width=800, height=600;
    static int currLevel = 1;
   
    static double lengthDecayRatio = 0.85;
    static double angleDecayRatio = 0.95;
    static double initialBranchingAngle = 30; //angle in degrees
    static double initialBranchLength = 100;   //pixels
 
    static int maxLevel = 30;
    static int millisecondsBetweenFrames = 500;

    
    public static void drawBinaryTree (Graphics g, double xStart, double yStart, double length, double angleDeg, double angleBranchDeg, int level)
    {
	double angleRad = degToRad * angleDeg;
	double angleBranchRad = degToRad * angleBranchDeg;

	double xEnd1 = (xStart + length * Math.cos (angleRad - angleBranchRad));
	double yEnd1 = (yStart - length * Math.sin (angleRad - angleBranchRad));  // subtract length*sin(A) because y points down

	double xEnd2 = (xStart + length * Math.cos (angleRad + angleBranchRad));
	double yEnd2 = (yStart - length * Math.sin (angleRad + angleBranchRad));  // subtract length*sin(A) because y points down

	if (level == 1) // BASE CASE: DRAW 1 LEFT BRANCH AND 1 RIGHT BRANCH
	{
	    g.drawLine ((int) xStart, (int) yStart, (int) xEnd1, (int) yEnd1);
	    g.drawLine ((int) xStart, (int) yStart, (int) xEnd2, (int) yEnd2);
	}

	else // RECURSIVE CALL:  DRAW 1 LEFT BRANCH AND 1 RIGHT BRANCH, AND THEN DRAW A NEW BINARY TREE WHERE THOSE LINES LEFT OFF, REDUCING THE LEVEL BY 1
	{
	    g.drawLine ((int) xStart, (int) yStart, (int) xEnd1, (int) yEnd1);
	    g.drawLine ((int) xStart, (int) yStart, (int) xEnd2, (int) yEnd2);
	    drawBinaryTree (g,xEnd1, yEnd1, length, angleDeg, 0.5*angleBranchDeg, level - 1);
	    drawBinaryTree (g,xEnd2, yEnd2, length, angleDeg, 0.5*angleBranchDeg, level - 1);
	}
    }
    
    
    public static void drawFibonacciTree (Graphics g, int age, double xStart, double yStart, double length, double currentAngleDegrees, double branchingAngleDegrees, int level)
    {
	double currentAngle = degToRad * currentAngleDegrees;
	double branchingAngle = degToRad * branchingAngleDegrees;

	double angleLeft = currentAngle + branchingAngle;
	double angleRight = currentAngle - branchingAngle;

	double xStraight =  xStart + length * Math.cos (currentAngle);
	double yStraight =  yStart - length * Math.sin (currentAngle); // subtract because y points down
	
        double xLeft =      xStart + length * Math.cos (angleLeft);
	double yLeft =      yStart - length * Math.sin (angleLeft);  
	
        double xRight =     xStart + length * Math.cos (angleRight);
	double yRight =     yStart - length * Math.sin (angleRight); 

	if (level == 1) // BASE CASE: DRAW 1 STRAIGHT BRANCH (IMMATURE) OR 2 SPLIT BRANCHES (MATURE)
	{
	    if (age >= 2)
	    {
		g.drawLine ((int) xStart, (int) yStart, (int) xLeft, (int) yLeft);
		g.drawLine ((int) xStart, (int) yStart, (int) xRight, (int) yRight);
	    }
	    else
		g.drawLine ((int) xStart, (int) yStart, (int) xStraight, (int) yStraight);

	}

	else // RECURSIVE CALL:  DRAW 1 STRAIGHT BRANCH (IMMATURE) OR 2 SPLIT BRANCHES (MATURE),
	     //                  AND THEN DRAW A NEW FIBONACCI TREE WHERE THOSE BRANCHES LEFT OFF, REDUCING THE LEVEL BY 1
	     //                  AND INCREASING THE AGE BY 1 (OR SETTING AGE BACK TO 0 FOR A NEW BABY BRANCH)
	    {
		if (age == 2)
		{
		    g.setColor (Color.pink);
		    g.drawLine ((int) xStart, (int) yStart, (int) xLeft, (int) yLeft);

		    g.setColor (Color.green );
		    g.drawLine ((int) xStart, (int) yStart, (int) xRight, (int) yRight);

		    drawFibonacciTree (g, 2, xLeft,  yLeft,  length * lengthDecayRatio, currentAngleDegrees + branchingAngleDegrees, branchingAngleDegrees * angleDecayRatio, level - 1);
		    drawFibonacciTree (g, 0, xRight, yRight, length * lengthDecayRatio, currentAngleDegrees - branchingAngleDegrees, branchingAngleDegrees * angleDecayRatio, level - 1);
		}
                
		else
		{
		    g.setColor (Color.blue);
		    g.drawLine ((int) xStart, (int) yStart, (int) xStraight, (int) yStraight);

		    drawFibonacciTree (g, age + 1, xStraight, yStraight, length * lengthDecayRatio, currentAngleDegrees, branchingAngleDegrees * angleDecayRatio, level - 1);
		}
	    }
    }


    public void paint( Graphics g) {
        
        g.setColor( Color.black );
        g.fillRect(0,0,width,height);
         g.setColor( Color.red );
        drawFibonacciTree (g, 0, 500, 500, initialBranchLength, 90, initialBranchingAngle, currLevel);
        
   }
    
    
    public static void main(String[] args) {
        
        FibonacciBranches fb = new FibonacciBranches();
        
        fb.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fb.setSize( width, height );
        fb.setBackground(Color.black);
        fb.setVisible(true);
        
        for (int i=2; i<=maxLevel; i++) {
            sleep( millisecondsBetweenFrames );
            currLevel++;
            fb.repaint();
            
        }  
        
    }

    
    
    public static void sleep( int duration ) {
        try {
              Thread.sleep( duration );
            }
        catch (Exception e) {
            }
    }
 
}
