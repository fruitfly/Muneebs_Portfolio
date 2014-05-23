# -*- coding: cp1252 -*-
q1 = "What is Mr. Schattman's dog's name?"
q2 = "What is 8 x 5?"
q3 = "The second highest mountain in the world is known by two different names. What are they?"
q4 = "How many consecutive years did bicyclist Lance Armstrong win the Tour De France?"
q5 = "What's the brand name of the product, a strong stick with footrests and a heavy spring on which people can hop around?"
q6 = "Can you give the first names of the four remaining Spice Girls since Geri Halliwell left the group?"
q7 = "What word can refer to a place of transition for lost souls, or a Carribbean dance?"
q8 = "Which South American city is named “River of January”."
q9 = "Name a country which contains each of these four-letter words, in the same order: a. Many b. Hail c. Done"
q10= "The length of one earth day is approximately 24 hours. Which planet in our solar system has the longest day, equivalent to about 244"

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

#You fill this out
correctAnswers = ["Pythagoras", "40", "K2 and GODWIN-AUSTIN", "Seven", "POGO STICK", "EMMA Bunton, VICTORIA Beckham, MELANIE Chisholm, MELANIE Gulzar", "LIMBO", "RIO DE JANEIRO", "a.GERMANY b. THAILAND c. INDONESIA", "VENUS"]

usersAnswers = ["", "", "", "", "", "", "", "", "", ""]

for i in range (0,10):
    print (questions[i])
    usersAnswers[i] = raw_input("")

mark = 10    
    
for i in range (0,10):
    if usersAnswers[i] != correctAnswers[i]:
        mark = mark-1
        
p = (float(mark)/float(10))*100
print ("Your mark was " + str(mark) + " out of 10. Your percentage was " + str(p) + "%")
#REPORT THE RESULTS
