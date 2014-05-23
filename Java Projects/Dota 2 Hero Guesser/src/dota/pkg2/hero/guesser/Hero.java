package dota.pkg2.hero.guesser;

//necessary imports
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Hero {

    //declaration of fields
    Attribute[] myAttributes = new Attribute[Dota2HeroGuesser.numQuestions];
    String heroName;
    boolean isCandidate = true;
    
    //creates a hero object and an array of attributes, all of which are set to false 
    public Hero(String name) throws IOException {
        heroName = name;

        setupAttributes();
    }
    
    //loads up the attribute array by getting information from a text file
    public void setupAttributes() throws IOException {
        String file = "Attributes.txt";
        FileReader f = new FileReader(file);
        Scanner s = new Scanner(f);

        for (int i = 0; i < Dota2HeroGuesser.numQuestions; i++) {
            myAttributes[i] = new Attribute(s.nextLine());
        }
    }
    
    //creates an array of hero objects with all their corresponding attributes, based on info from a txt file
    public static Hero[] getHeroes() throws IOException {
        String file = "heroes.txt";
        FileReader f = new FileReader(file);
        Scanner s = new Scanner(f);
        
        Hero[] heroes = new Hero[Dota2HeroGuesser.numHeroes];
        int numAttributes = Dota2HeroGuesser.numQuestions;
        String attribute, name;

        name = s.nextLine();
        
        for (int hero = 0; hero < heroes.length; hero++) {

            heroes[hero] = new Hero(name);

            attribute = s.nextLine();

            while (!(attribute.charAt(0) == '#') && s.hasNext()) {

                for (int attIndex = 0; attIndex < numAttributes; attIndex++) {
                    if (attribute.equalsIgnoreCase(heroes[hero].myAttributes[attIndex].attributeDescription)) {
                        heroes[hero].myAttributes[attIndex].setToTrue();
                    }
                }
                
                attribute = s.nextLine();
                
                //ignores empty lines
                while (attribute.length() == 0) {
                    attribute = s.nextLine();
                }
            }
            name = attribute.substring(2);

        }
        return heroes;
    }

    //prints out all the relevant information of a hero
    public void displayHero() {
        System.out.println(this.heroName);
        for (int i = 0; i < this.myAttributes.length; i++) {
            if (this.myAttributes[i].attributeValue) 
            {
                System.out.println(this.heroName + this.myAttributes[i].attributeDescription);
            }
        }
    }
    
    //eliminates the hero from the list of possible candidates
    public void eliminate() {
        this.isCandidate = false;
    }
}
