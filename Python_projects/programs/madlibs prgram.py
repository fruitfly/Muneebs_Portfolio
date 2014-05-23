name = input("please enter the name of your character ")
gender = input ("please input the gender of the character (must be male/female)")
noun1= input ("please input the first noun")
noun2 = input("please input the second noun")
noun3=input("please input the third noun")

if gender == 'male':
    print (" Today," + name + " went to the zoo and saw a " + noun1 + ". He stared at it long and hard and decided to touch it. Just then a " + noun2 + " walked up to him. The " + noun2 + " asked him what he was doing. Then " + noun3 + " came up to him." + name + " smacked them all")


if gender == 'female':
    print (" Today," + name + " went to the zoo and saw a " + noun1 + ". She stared at it long and hard and decided to touch it. Just then a " + noun2 + " walked up to her. The " + noun2 + " asked her what she was doing. Then " + noun3 + " came up to her." + name + " smacked them all")
    
