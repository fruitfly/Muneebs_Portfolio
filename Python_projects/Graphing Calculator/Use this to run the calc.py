from graphing_calculator_package import *
print("Before you input your function, make sure that there are no spaces in between characters and that the exponent symbol is '*' (e.g. x*2)")
function = input("Please input the function you would like to graph")
xMax = input("Please input the maximum x-value")
xMin = input("Please input the minimum x-value")

print(drawFunction(function,xMax,xMin))
