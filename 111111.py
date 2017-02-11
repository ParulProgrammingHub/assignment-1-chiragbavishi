p=input('Enter the principle amount:')
t=input('Enter teh time:')
r=input('Enter the rate in percentage:')
def compound(p,t,r):
    cmpo=p*(((1+float(r)/100)**t)-1)
    return cmpo
print 'compund interest is :%s'%(compound(p,t,r))
