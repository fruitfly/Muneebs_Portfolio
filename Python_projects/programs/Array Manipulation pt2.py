temperatures = [25, 27, 30, 28, 22, 29, 33, 31, 30, 27, 27, 19, 18, 17, 16, 12, 18,30,56,76,11,26,27,21]

maxtemp = 0
mintemp = 100

for i in range(0,24):
    if temperatures[i]< mintemp:
        mintemp=temperatures[i]
    if temperatures[i]> maxtemp:
        maxtemp = temperatures[i]
print (mintemp)
print (maxtemp)
