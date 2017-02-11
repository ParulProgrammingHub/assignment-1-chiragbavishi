math=input("Marks Obtained in maths")
java=input("Marks Obtained in java")
pyth=input("Marks Obtained in Python")
co=input("Marks Obtained in Co")
ooa=input("Marks Obtained in OOAD")
total = math + java + co + ooa + pyth
avg= total/5.0
print "The mean is %s" % (avg)
per=(total*100)/250
if per<=35 :
    print "YOU HAVE FAILED AND YOU HAVE SCORED %s PERCENTAGE" % (per)

else :
    print "CONGRATULATIONS ! YOU HAVE PASSED THE EXAM AND YOUR SCORE IS %s PERCENTAGE" % (per)
