#program to calculate third angle using function
ang1=input("Enter the 1st angle")
ang2=input("Enter the 2nd angle")
def thirdangle(ang1,ang2):
    angle=180-(ang1+ang2)
    return  angle
print "The third angle is %s" %(thirdangle(ang1,ang2))






