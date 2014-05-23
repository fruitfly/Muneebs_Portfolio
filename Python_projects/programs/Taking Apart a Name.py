namestring = input("Please Input your name. Your name must include a middle initial with a period after the initial")

firstname = namestring[0:namestring.index(" ")]

print ("Your First Name is : " + firstname)

middleinitial = namestring[namestring.index(" ")+1:namestring.index(".")]

print("Your Middle Initial is : " + middleinitial)

lastname = namestring[namestring.index(".")+2:len(namestring)]

print ("Your Last Name is : " + lastname)
