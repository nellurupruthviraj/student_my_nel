### Lambda Function
from functools import reduce

s=(lambda x,y: x*y)
print(s(10,20))

s=(lambda x:x)
print(s(10*3))

s=(lambda i,x: i-x)
print(s(25,20))

s=(lambda x,y:x>y)
print(s(20,30))

s=(lambda x: x**2)
print(s(5))


####MAP
l=[1,2,3,4,5,6,7,8,9]
s=list(map(lambda x: x-100,l))
print(s)

A=[1,2,3,4,5,6,6,7,7,8,9,10]
ADD=list(map(lambda x:x+10,A))
print(ADD)

A=[1,2,3,4,5,6,6,7,7,8,9,10]
SUB=tuple(map(lambda x:x-5,A))
print(SUB)

A=[1,2,3,4,5,6,6,7,7,8,9,10]
MUL=list(map(lambda x:x*2,A))
print(MUL)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
DIV=list(map(lambda x:x/2,item))
print(DIV)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
DIV=list(map(lambda x:x//2, item))
print(DIV)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
MOD=list(map(lambda x:x%2,item))
print(MOD)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
Dobsr=list(map(lambda x:x**2,item))
print(Dobsr)


item=[1,2,3,4,5,6,6,7,7,8,9,10]
DIV=list(map(lambda x:x<2,item))
print(DIV)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
les=list(map(lambda x:x>=5,item))
print(les)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
EVN=list(map(lambda x:x%2==0,item))
print(EVN)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
ODD=list(map(lambda x:x%2==1,item))
print(ODD)

####FILTER

item=[1,2,3,4,5,6,6,7,7,8,9,10]
EVN=list(filter(lambda x: x%2==0,item))
print(EVN)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
ODD=list(filter(lambda x:x%2==1,item))
print(ODD)


item=[1,2,3,4,5,6,6,7,7,8,9,10]
GRT=list(filter(lambda x:x>=6,item))
print(GRT)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
EQL=list(filter(lambda x: x<=4,item))
print(EQL)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
EQL=list(filter(lambda x:x==6,item))
print(EQL)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
NQL=list(filter(lambda x:x!=7,item))
print(NQL)


#### REDUCE
item=[1,2,3,4,5,6,6,7,7,8,9,10]
RED=reduce(lambda x,y:x+y, item)
print(RED)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
REd=reduce(lambda x,t:x*t,item)
print(REd)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
red=reduce(lambda x,s:x-s,item)
print(red)

item=[111,3456,776,888799,997,9986,59,3310]
ADD=reduce(lambda A,B:A+B,item)
print(ADD)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
Ind=list(filter(lambda x:x,item[0:5]))
print(Ind)

item=[1,2,3,4,5,6,6,7,7,8,9,10]
ind=list(filter(lambda x:x, item[::-1]))
print(ind)



