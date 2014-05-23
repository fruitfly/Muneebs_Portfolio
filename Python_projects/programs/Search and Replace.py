sentence = "Goofus is my cat.  He is the dumbest cat who has ever lived."

wordList = sentence.split()

searchWord = "cat"
searchWord1 = "cat."
replacementWord = "dog"
replacementWord1 = "dog."

newSentence = ""

for i in range(0, len( wordList ) ):
    if wordList[i] == searchWord1:
       wordList[i] = replacementWord1 
    if wordList[i] == searchWord  :
        wordList[i] = replacementWord

    newSentence = newSentence + " " + wordList[i]


##print( wordList )

print( newSentence )



        
