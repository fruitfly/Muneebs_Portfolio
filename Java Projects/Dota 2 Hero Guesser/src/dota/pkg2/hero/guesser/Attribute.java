package dota.pkg2.hero.guesser;

public class Attribute {
    
    //declaration of fields
    boolean attributeValue = false;
    String attributeDescription;
    String question;
    
    //constructs an attribute object with a description and a question
    public Attribute (String description){
        
        this.attributeDescription = description;
         
        deriveQuestion(this.attributeDescription);
        
    }
    
    //prints out the question field of the attribute object
    public void askQuestion (){
        System.out.println(question);
    }
    
    //sets the attribute's value to true
    public void setToTrue(){
        this.attributeValue = true;
    }
    
    //creates and formats question based on the attribute's description
    public void deriveQuestion(String description){
        String first,rest;
        
        first = this.attributeDescription.substring(0, description.indexOf(' '));
        rest = description.substring(description.indexOf(' '), description.length());
                
        if (first.equalsIgnoreCase("has") ){
            question = "Does the hero have" +  rest + "?";
        }
        else if (first.equalsIgnoreCase("is")){
            question = "Is the hero" + rest + "?";
        }       
        else {
            question = "Does the hero" + rest + "?";
        }
    }
    
}
