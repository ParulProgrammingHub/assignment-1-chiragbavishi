day=input('Enter the days:')
yr=day/360
num=day%360
mon=num/30
day=num%30
print '%syear %smonths %sdays'%(yr,mon,day)
