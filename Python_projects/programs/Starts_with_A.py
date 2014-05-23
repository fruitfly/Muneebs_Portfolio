myZoo = [ "sheep","aardvark","lemur","anteater","bear","frog","antelope"]



def numWordsThatStartWithA (words):
    numWordsThatStartWithA = 0
    for i in range (0,len(words)):
        if words[i][0]=="a":
            numWordsThatStartWithA = numWordsThatStartWithA +1
    return numWordsThatStartWithA

print( numWordsThatStartWithA ( myZoo ) )   #should print 3
