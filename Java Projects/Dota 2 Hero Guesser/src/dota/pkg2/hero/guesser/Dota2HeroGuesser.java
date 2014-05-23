/* Programmers: Muneeb Ahmed, Octavio Harris, Qianshu Wang
 ** Date Last Modified: April 18, 2014
 ** Description: This program is designed to guess which hero from the game 
 **              Dota 2 based on the user's response to the questions asked.
 */
package dota.pkg2.hero.guesser;

//necessary imports
import java.io.*;
import java.util.*;

public class Dota2HeroGuesser {

    //declaration of fields 
    static final int numQuestions = 23;
    static final int numHeroes = 107;
    
    static int remainingCandidates = numHeroes;
    static Attribute[] attributes = new Attribute[numQuestions];
    static Hero[] heroes;

    public static void main(String[] args) throws IOException {

        getAttributes();
        
        //creats an array of all heroes
        heroes = Hero.getHeroes();
        
        play();
    }

    //question picking/asking and hero selection algorithm
    public static void play() {
        Scanner in = new Scanner(System.in);
        int questionNum = 0;
        String s;
        boolean response;

        while (questionNum < numQuestions && remainingCandidates > 1) {

            //if the question will eliminate candidates, ask the question
            if (questionIsUseful(questionNum)) {

                attributes[questionNum].askQuestion();

                response = getResponse();

                eliminateCandidates(questionNum, response);
                
            }
            //proceed to next question
            questionNum++;
        }

        outputHero();

    }

    //outputs the name of all heroes that are still candidates for selection    
    public static void outputHero() {
        for (int heroNum = 0; heroNum < numHeroes; heroNum++) {
            if (heroes[heroNum].isCandidate) {
                System.out.println("Your hero is " + heroes[heroNum].heroName + ".");
            }
        }
    }

    //eliminates candidates and counts number of remaining candidates
    public static void eliminateCandidates(int attributeIndex, boolean response) {
       
        remainingCandidates = 0;
        
        for (int heroNum = 0; heroNum < numHeroes; heroNum++) {
            if (heroes[heroNum].myAttributes[attributeIndex].attributeValue != response) {
                heroes[heroNum].eliminate();
            }
        }
        
        
        
        for (int heroNum = 0; heroNum < numHeroes; heroNum++) {
            if (heroes[heroNum].isCandidate) {
                remainingCandidates++;
            }
        }
        
    }

    //gets all the possible attributes from a text file and loads them up into an array
    public static void getAttributes() throws IOException {
        String file = "Attributes.txt";
        FileReader f = new FileReader(file);
        Scanner s = new Scanner(f);

        for (int i = 0; i < Dota2HeroGuesser.numQuestions; i++) {
            attributes[i] = new Attribute(s.nextLine());
        }
    }

    //checks to make sure the question will eliminate candidates
    public static boolean questionIsUseful(int questionNum) {

        int numWithAttribute = 0;

        //counts the number of heroes with the attribute
        for (int heroNum = 0; heroNum < numHeroes; heroNum++) {
            if (heroes[heroNum].isCandidate) {
                if (heroes[heroNum].myAttributes[questionNum].attributeValue) {
                    numWithAttribute++;
                }
            }
        }

        //if all the heroes have or do not have that attribute, skip the question
        if (numWithAttribute == remainingCandidates || numWithAttribute == 0) {
            return false;
        } 
        else {
            return true;
        }
    }

    public static boolean getResponse() {
        Scanner in = new Scanner(System.in);
        String s;
        boolean response;

        s = in.next();

        if (s.charAt(0) == 'y' || s.charAt(0) == 'Y') {
            response = true;
        } else {
            response = false;
        }
        return response;
    }

}
