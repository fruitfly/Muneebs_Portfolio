#This program takes coordinates of four points and determines what
#Shape the points make

import math

x1 = int(input("please input the value of point x1"))
x2 = int(input("please input the value of point x2"))
x3 = int(input("please input the value of point x3"))
x4 = int(input("please input the value of point x4"))
y1 = int(input("please input the value of point y1"))
y2 = int(input("please input the value of point y2"))
y3 = int(input("please input the value of point y3"))
y4 = int(input("please input the value of point y4"))

AB = math.sqrt((x2 -x1)**2 + (y2-y1)**2)
BC = math.sqrt((x3 -x2)**2 + (y3-y2)**2)
CD = math.sqrt((x4 -x3)**2 + (y4-y3)**2)
DA = math.sqrt((x4 -x1)**2 + (y4-y1)**2)


if x2-x1 == 0:
    mAB == "undefined"
else:
    mAB = (y2-y1) / (x2-x1)
if x3-x2 == 0:
    mBC == "undefined"
else:
    mBC = (y3-y2) / (x3-x2)
if x4-x3==0:
    mCD== "undefined"
else:
    mCD = (y4-y3) / (x4-x3)
if x1-x4 == 0:
    mAD=="undefined"
else:
    mAD = (y4-y1) / (x4-x1)


if AB == BC == CD == DA:
    if (mAB=="undefined" and mBC==0) or (mBC=="undefined" and mAB==0) or (mCD=="undefined" and mAD==0) or (mAD== "undefined" and mCD==0) or mAB*mBC==-1:
        print ("square")
    else:
        print ("rhombus")
elif AB == CD and BC == DA:
    if (mAB=="undefined" and mBC==0) or (mBC=="undefined" and mAB==0) or mAB*mBC==-1:
        print ("rectangle")
    elif mAB==mCD and mBC==mAD:
        print ("parallelogram")
elif mBC==mAD:
    print ("trapezoid")
elif AB==DA and BC==CD:
    print ("kite")
else:
    print ("quadrilateral")
