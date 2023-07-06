from math import *

a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

delta=(b**2)-(4*a*c)

if delta>0:
    print('The equation has two real roots')
    x1=((-b)+sqrt(delta))/(2*a)
    x2=((-b)-sqrt(delta))/(2*a)
    print('x1= ',x1)
    print('x2= ',x2)
elif delta==0:
    print('The equation has one real roots')
    x=(-b)/(2*a)
    print('x= ',x)
else:
    prin('The equation has no real roots')
    
