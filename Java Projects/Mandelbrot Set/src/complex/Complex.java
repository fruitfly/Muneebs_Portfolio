/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package complex;

/**
 *
 * @author ahmem9877
 */
public class Complex {
    
    
    double coefficient;
    double constant;
    public Complex(double a, double b){
        constant =a;
        coefficient= b;
        
    }
    
    public void display(){
        if (coefficient>0){
        
            System.out.println(constant + "+" + coefficient + "i");
        }
        else{
            System.out.println(constant + "-" + Math.abs(coefficient) + "i");
        }
    }
    
    public Complex multbyScalar(double s){
        
        double newcoefficient = coefficient * s;
        double newconstant = constant*s;
        Complex n = new Complex(newconstant,newcoefficient);
        return n;
        
    }
    
    public Complex addorsubtract (Complex f, boolean addorsubtract){
        //if you are adding, set addorsubtract to true
        double a1 = this.constant;
        double b1 = this.coefficient;
        double a2 = f.constant;
        double b2 = f.coefficient;
        
        double a3;
        double b3;
        if (addorsubtract){
             a3 = a1 + a2;
             b3 = b1+b2;
        }
        else{
             a3 = a1 - a2;
             b3 = b1-b2;
        }
        
        
        Complex n = new Complex (a3,b3);
        return n;
    }
    
    public Complex multiplication (Complex f){
        double a1 = this.constant;
        double b1 = this.coefficient;
        double a2 = f.constant;
        double b2 = f.coefficient;
        
        double a3 = (a1*a2) + (b1*b2)*(-1);
        double b3 = (a1*b2)+(a2*b1);
        
        Complex n = new Complex(a3,b3);
        return n;
        
     
          
        
    }
    
    public double absoluteValue (){
        return (Math.sqrt(Math.pow(constant, 2)+Math.pow(coefficient, 2)));
        
    }
    
    public Complex conjugate (){
        Complex n = new Complex (constant, coefficient*-1);
        return n;
        
        
    }
    public Complex complexpow (int pow){
        Complex z = this;
        for (int i=1;i<pow;i++){
            z = z.multiplication(this);
            
        }
        return z;
        
    }
    
}
