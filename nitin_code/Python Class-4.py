'''
x="what is the best way to get to the airport?"
print(x.capitalize())

x="what is the best way to get to the airport?"
print(x.count("t"))

x="what is the best way to get to the airport?"
print(x.endswith("?"))
print(x.endswith("t"))

x="what is the best way to get to the airport?"
print(x.find("r"))
print(x.find("h"))

x="what is the best way to get to the airport?"
print(f"{x}, \n \\This sentence is good")

x="what is the best way to get to the airport?"
print(x.index ("t",35))
print(len(x))

x#="12.44,33.32"
#print(x.isdecimal())

x="288"
y = x.isdigit()
print(y)

x="20.4533,65.4654"
print(x.isdecimal())

x="123456"
print(x.isalnum())

x="what is the best way to get to the airport?"
print(x.islower())

x="what is the best way to get to the airport?"
print(x.istitle())

x="what is the best way to get to the airport?"
print(x.isupper())

x="what is the best way to get to the airport?"
print(x.title())

x="what is the best way to get to the airport?"
s=x.split()
x=" ".join(reversed(s))
print(x)

x="what is the best way to get to the airport?"
a=x.split()
for i in a:
    d=i[::-1]
    print(d,end=" ")

x="nitin how are you"
a=x.split()
print(a)
c=" ".join(reversed(a))
print(c)

x="what is thE bEst Way To gEt tO tHe aiRport?"
print(len(x))
print(x.lower())

x="   what is the best way to get to the airport?  "
print(x)
print(x.lstrip())

x="   what is the best way to get to the airport?  "
print(x.rstrip())

x="   what is the best way to get to the airport?  "
print(x.strip())


x="what is the best way to get to the airport?"
a=x.replace("airport","Bus Stop")
print(a)

x="what is the best way to get to the airport?"
a=x.rpartition("3")
print(a)

x="what is the best way to get to the airport?"
print(x.rsplit())
print(x.split())

x="what is the best way to get to the airport? hello how is the days"
print(x.splitlines())

x="what is the best way to get to the airport?"
print(x.startswith("w"))

x="whAt is The best Way to get to The Airport?"
print(x.swapcase())

x="whAt is The best Way to get to The Airport?"
print(x.title())

x="whAt is The best Way to get to The Airport?"
print(x.upper())

print(10>9)
print(9>10)

A=250
B=150
print(A+B)

A=250
B=150
print(A-B)

A=250
B=150
print(A*B)

A=250
B=150
print(A/B)

A=250
B=150
print(A//B)

A=10
B=20
print(A%B)

A=2
B=6
print(A**B)

x=5
print(x)

x=5
x+=3
print(x)

x=5
x-=3
print(x)

x=5
x*=3
print(x)

x=5
x/=3
print(x)

x=5
x//=3
print(x)

x=5
x%=3
print(x)

x=5
x**=3
print(x)

x=5
x&=3
print(x)

x=5
x|=3
print(x)

x=5
x^=3
print(x)

x=5
x>>=3
print(x)

x=3
x<<=3
print(x)

print(x :=3)

A=["Hello", "good", "morning", "How", "are", "you"]

for i in A:
    if i=="morning":
        print(i)

A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    for j in A:
        print(i,j,end=" ")


A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i==20:
        print(i)

A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i!=20:
        print(i,end=" ")

A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i>=20:
        print([i])

A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i<=20:
        print(i)


A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i>50:
        print(i)

A=[10,20,30,40,50,50,60,70,80,90]
for i in A:
    if i<50:
        print(i,end=' ')


A="Hello good morning How are you"
x=A.split()
a=" ".join(reversed(x))
print(a)

A="Hello good morning How are you"
x=A.split()
for i in x:
    a=i[::-1]
    print(a,end=' ')

A="Hello good morning How are you"
for i in A:
    if i == "H":
        print("Hello is present")


A=[1,2,3,4]
B=[1,2,3,4]
X=A
print(A is X)

A=None
print(A is None)

A=None
print(A is not None)



A="Hello good morning How are you"
if "Hello" in A:
    print("present")
else:
    print("Not Present")

A="Hello good morning How are you"
if "How" not in A:
    print("Not Present")
else:
    print("present")

A="Hello good morning How are you"
print("How" in A)

A="Hello good morning How are you"
print("you" not in A)

A="Hello good morning How are you"
print("Yes" not in A)

###List Methods

A=[10,20,30,40,50,60,70,80,90,100]
A[2]=111
print(A)

A=[10,20,30,40,50,60,70,80,90,100]
A.insert(2,111)
print(A)

A=[10,20,30,40,50,60,70,80,90,100]
B=[10,203,40405,506,60]
A.extend(B)
print(A)

A=["Nitin","Kannur","Bang"]
B=["HYD","Pune","Delhi"]
A.extend(B)
print(A)

A=["Nitin","Kannur","Bang"]
A.clear()
print(A)

A=["Nitin","Kannur","Bang"]
A.copy()
print(A)

A=["Nitin","Kannur","Bang"]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
z=A.count(50)
print(z)

A=[10,20,30,40,50,50,60,60,70,80,90,100]
print(A.count(100))

A=[10,20,30,40,50,50,60,60,70,80,90,100]
print(A.index(80))

A=["Nitin","Kannur","Bang"]
print(A.index("Bang"))

A=["Nitin","Kannur","Bang"]
print(A.pop())

A=["Nitin","Kannur","Bang"]
print(A.pop(1))

A=[10,20,30,40,50,50,60,60,70,80,90,100]
print(A.pop(2))

A=[10,20,30,40,50,50,60,60,70,80,90,100]
A.remove(20)
print(A)


A=["Nitin","Kannur","Bang"]
a=" ".join(reversed(A))
print(a)

A=["Nitin","Kannur","Bang"]
for i in A:
    a=i[::-1]
    print(a,end=" ")

A=[10,20,30,40,50,50,60,60,70,80,90,100]
A.remove(100)
print(A)

A=[10,20,30,40,50,50,60,60,70,80,90,100]
A.reverse()
print(A)

A=[10100,240,320,402,89,1000,60,60,70,880,90,100]
A.sort()
print(A)

A=[10100,240,320,402,89,1000,60,60,70,880,90,100]
A.sort(reverse=A)
print(A)

A=[1,26,34,42,5,6,7,6,4,5,6,8,9,10,20,22,24]
L=[]
for i in A:
    if i%2==0:
        L.append(i)
        L.sort()
        print(L)'''



stud=["Nitin","Sharan","Rahul"]
marks=[40,45,50]
stud_mark={}

for index, student in enumerate(stud):
    stud_mark[student] =marks[index]

print(stud_mark)


stud=["Nitin","Sharan","Rahul"]
marks=[40,45,50]
stud_mark={}

for i in range(3):
    stud_mark[stud[i]] =marks[i]

print(stud_mark)


stud=["Nitin","Sharan","Rahul","Suresh"]
marks=[40,45,50,70]
stud_mark={}

for i in range(len(stud)):
    stud_mark[stud[i]]=marks[i]
print(stud_mark)


l=[1,2,3,4,5]
dl=[item*2 for item in l]
print(dl)


l=[x for x in range(1,11)]
el=[x*2 for x in l if x%2==0]
print(el)

l=[a for a in range(1,15,2)]
on=[a*2 for a in l if a%2==0]
print(on)

stud=["Nitin","Sharan","Rahul","Suresh"]
A=[x[1] for x in stud]
print(A)

stud=["Nitin","Sharan","Rahul","Suresh"]
print([x[3] for x in stud])

l=[x for x in range(1,11)]
l1=[x for x in l if x%2==0]
print(l1)