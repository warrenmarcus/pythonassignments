# Warren Green
# 006314031

import math

angle = int(input("enter an angle: "))
# incase the angle entered is above 360. used for finding quadrant.
x = angle%360

#converting to radians
radx = (angle*math.pi)/180

print("The angle", angle, "in radians:", radx)

#finding the quadrant
if x > 0 and x <= 90:
    print("The angle", angle, "is in the first quadrant")
elif x > 90 and x <= 180:
    print("The angle", angle, "is in the second quadrant")
elif x > 180 and x <= 270:
    print("The angle", angle, "is in the third quadrant")
elif x > 270 and x <= 360:
    print("The angle", angle, "is in the fourth quadrant")



#using degrees for trig functions
print("\nTrig functions using degrees")
print("\tcosine:", math.cos(x))
print("\tsine:", math.sin(x))
print("\ttangent:", math.tan(x))


#using radians for the trig funtions
print("\nTrig functions using radians")
print("\tcosine:", math.cos(radx))
print("\tsine:", math.sin(radx))
print("\ttangent:", math.tan(radx))
