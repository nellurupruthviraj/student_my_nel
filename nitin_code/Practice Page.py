###Concatination
'''
frst_name=input("enter frist name: ")
Lst_name=input("enter last name: ")

print(frst_name +" "+ Lst_name)
print(f"{frst_name} Both are same {Lst_name}")


A="Nitin", 20, "Kannur"
print(A*3)
print(A*10)

A=6454
B=866346
C=(A-B)
print(C)

A=645
B=866346
C=abs(A-B)
print(C)

A= "  nitin hOw aRe You  "
print(A.upper())
print(A.lower())
print(A.strip())

A=("Those grapes are probably sour anyway! But deep down are")
print(A.replace("are","The"))


A=("Those grapes are probably sour anyway! But deep down are")
S=(A.replace("probably","Mostly"))
print(S)

S=("Those grapes are probably sour anyway! But deep down are")
print(len(S))

A=("Name Nitin, Lets Start")
a=A[3]
print(a)

Name="Nitin Kannur"
print(Name[-2])
print(Name[3:])
print(Name[-2])
print(Name[-5])

A=("Name Nitin, Lets Start")
print(A[::2])
print(A[::3])

A="Bangalore \n is a Good City"
print(A)

#Next line
S=("Those grapes are probably \n sour anyway! \n But deep down are")
print(S)

#tab space
S=("Those grapes are probably \t sour anyway! \t But deep down are")
print(S)

#print one backslash

S=("Those grapes are probably \\ sour anyway! \\ But deep down are")
print(S)

a=None
print(type(a))

#### Operaters

A=23
A+=100
print(A)


a=10
b=100
print(a==b)
print(a!=b)
print(a>b)
print(a<b)


a=(1>2 and 2>1)
print(a)

a=(1>2 or 2>1)
print(a)

a=(not(1>2))
print(a)

a=(not(2>1))
print(a)

lst=[1,2,3,5,6]
a=("Bangalore city")

print(5 in lst)
print(7 in lst)
print("B" in a)
print("t" in a)
print("r" not in a)

a="Sharan kumar"
b="nitin kumar"

print("u" in a) and ("a" in b)

print("a" in a) and ("4" in b)

print("a" in a) or ("a" in b)

import random
print(random.randrange(1,10))

print(random.randrange(2,20,1))

l1=[100,200,300,400,500]
l2=l1[1:3]
print(l2)

l=["orange","Apple","Banana","milk","Bru","Sugar"]
a=(l[5])
print(a)
print(l[2])




a=[10,20,30,40,50,60,70,80]
a.append(90)
print(a)

a=[10,20,30,40,50,60]
a.insert(4,50)
print(a)

a=[122,4,566,8,9,9,0,8,7666,5,554,4332]
a.append(2000)
print(a)
a.insert(6,1000)
print(a)


l1=[1,2,3,5,6,7]
l2=[7,8,9,0,0,8,8]
l1.extend(l2)
print(l1)



def myfn():

    a=[122,4,566,8,9,9,0,8,7666,5,554,4332]
    a.pop()
    print(a)
    a.pop(0)
    print(a)

myfn()

def myfnc():
    l1=[100,200,300,400,500]
    l2=[600,700,500,300,200]
    l1.append(1000)
    print(l1)

    l2.insert(2,800)
    print(l2)

    l1.extend(l2)
    print(l1)

myfnc()

'''

def myfcn():
    l1=[111,222,333,444,555,666,777]
    l1.pop()
    print(l1)

    l1.pop(0)
    print(l1)

    l1.remove(222)
    print(l1)

myfcn()

a=2000
b=4000
s=abs(a-b)
print(s)

A=("If you get up in the morning and "
   "think the future is going to be better,"
   " it is a bright day. "
   "Otherwise, it's not.")
S=("and" in A)
print(S)

print("evening," in A)

a=("Otherwise" not in A)
print(a)

A=("If you get up in the morning and "
   "think the future is going to be better,"
   " it is a bright day. ")

def myfn():
    if "geet" in A:
        print("Yes")
    elif "morning" not in A:
        print("morning not present")
    else:
        print("Both are not present")

myfn()


A=(" If you get up in the morning ")

print(len(A))
print(A.lower())
print(A.upper())
print(A.strip())
print(A.lstrip())
print(A.rstrip())

A=(" If you get up in the morning ")

S=A[10]
print(S)

S=A[2:20]
print(S)

S=A[2:20:5]
print(S)

l1=[100,200,300,400,500]
l2=[600,700,500,300,200]

print(f"{l1},both Are Same {l2}")

A=(" If you get up in the morning ")
S=A.replace("morning", "Evening")
print(S)

B="sunday"
A=(" If you get up in {} the {} morning")
print(A.format(B,"fri"))

A=("In bangalore city cold climet {}")
C="and heavy traffic"


A=("If you get up in the morning and "
   "think the future is going to be better,"
   " it is a bright day. "
   "Otherwise, it's not.")
s=len(A)
a=A[56]
print(a)

print(A.index("is"))
print(len(A))


A=["Nitin","Sharan","Rahul","Rohit"]
print(len(A))

print(A[0][3])
print(A.index("Nitin"))
print(A.index("Rahul"))

A=[10,20,10,20,30,40,20,30,40,50,60,70,50,60,70,80,80,90,100]
print(A.count(30))
print(sorted(A))

A=[10,20,10,20,30,40,20,30,40,50,60,70,100,100,100]
s=A.count(100)
print(s)
print(A.count(100))

a=(sum(A))
print(a)
print(sum(A))

s=A.index(70)
print(s)
print(A.index(60))

a=sorted((A))
print(A)
print(sorted(A))

A=[1,2,3,45,2,2,3,3,45,67,8,8,8,6,5,5,4,]

print(sorted(A))
a=A.reverse()
print(a)

a="monday"
b="Good morning {}"
print(b.format (a), "Have Nice Day")

a="monday"
c="Day"
b="Good morning {} Have Nice {}"
print(b.format(c,a))

Name="Nitin"
age=26
address="Bangalore Right"

Details=("Hii {} ,\n How are you, \n your age is {}, \n and your Address is {}")

print(Details.format(Name,age,address))

A= "If you xsjknknjibijniu"
a = len(A)//2
g=A[:a]
print(g)