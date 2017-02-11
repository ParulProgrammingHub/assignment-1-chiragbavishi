p=input('Enter the principle amount:')
t=input('Enter teh time:')
r=input('Enter the rate in percentage:')
def inter(p,t,r):
    interest=(p*t*r)/100
    return interest
print 'simple interest is :%s'%(inter(p,t,r))




