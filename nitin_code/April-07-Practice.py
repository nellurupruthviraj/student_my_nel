
print("hello world")

x=2
print(x)

x="Nitin"
print(x)

#### Camel Case
nitinKannur="Nitin"
print(nitinKannur)

#### Pascal Case
NitinKannur="Nitin"
print(NitinKannur)

#### Snake Case
nitin_kannur="Nitin"
print(nitin_kannur)


a,b,c="Bangalore","Delhi","Pune"
print(b)
print(a)
print(c)


a=b=c="Bangalore","Delhi","Pune"
print(b)
print(a)
print(c)


x="magic"
print("python is" ,x)



x="hard"

def my_fn():
    x="Magic"
    print("Python is ",x)
my_fn()
print("Python is ", x)

#### Global variable
x="hard"

def my_fn():
    global x
    x="Magic"
    print("Python is ",x)
my_fn()
print("Python is ", x)


x="Hello Good Morning, Nice to meet you "
print(type(x))

x=400
print(type(x))

x=200.77
print(type(x))

x=2+3j
print(type(x))

x=[1,2,3,4,"Nitin", "Bangalore"]
print(type(x))

x=(10,203,1,2,3,4,"Nitin", "Bangalore")
print(type(x))

x={10,203,1,2,3,4,"Nitin", "Bangalore"}
print(type(x))

x={"Name":"Nitin","Age":27,"address":"Bangalore"}
#{"Name":"Sharan","Age":28,"Address":"Kalaburagi"},
#{"Name":"Naveen","Age":29,"Address":"delhi"}

print(type(x))

x=frozenset((10,203,1,2,3,4,"Nitin", "Bangalore"))
print(type(x))

import random
print(random.randrange(1,20))

#### Python Casting
##INT
x=int(1)
y=int(2.6)
z=int("3")
print(x)
print(y)
print(z)


#### Float
x=float(1)
y=float(2.6)
z=float("3")
print(x)
print(y)
print(z)

#### STR
x=str(1)
y=str(2.6)
z=str("3")
print(x)
print(y)
print(z)

##### INDEXING AND  SLICING

x="10,203,1,2,3,4,Nitin, Bangalore"
print(x[20])
print(x[22])

x="10,203,1,2,3,4,Nitin, Bangalore"
print(len(x))

x="10,203,1,2,3,4,Nitin, Bangalore"
print(x[2:])

x="10,203,1,2,3,4,Nitin, Bangalore"
print(x[:-1])

x="10,203,1,2,3,4,Nitin, Bangalore"
print(x[::2])

x="Hello Good Morning, Nice to meet you "
if "Nice" in x:
    print("yes 'Nice' is present")


x="Hello Good Morning, Nice to meet you "
if "Nice" not in x:
    print("yes 'Nice' Not in x")
else:
    print("Ok")


#### Python Modify String
x="Hello Good Morning, Nice to meet you "
print(x.upper())


x="Hello Good Morning, Nice to meet you "
print(x.lower())

x="Hello Good Morning, Nice to meet you "
print(x.strip())

x="Hello Good Morning, Nice to meet you "
print(x.lstrip())

x="Hello Good Morning, Nice to meet you "
print(x.rstrip())

x="Hello Good Morning, Nice to meet you "
print(x.split())

x="Hello Good Morning, Nice to meet you "
print(x.replace("Hello", "Hii"))

x="Hello Good Morning, Nice to meet you "
print(len(x))

x="Hello Good Morning, Nice to meet you "
print(x.count("o"))

x=[12,3,4,23,4,56,6,7,8,8,99,6,6,5,4,43,2]
print(sum(x))

x=[12,3,4,23,4,56,6,7,8,8,99,6,6,5,4,43,2]
print(max(x))

x=[12,3,4,23,4,56,6,7,8,8,99,6,6,5,4,43,2]
print(min(x))

x="hello good morning"
x1="welcome to india"
print(x+","+x1)


#### Python Escape Characters:
x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x)

x="Hello Good Morning,\\ Nice to meet you,\\ it\'s a greate Day"
print(x)

x="Hello Good Morning, \nNice to meet you, it\'s a greate Day"
print(x)

x="Hello Good Morning, \tNice to meet you, it\'s a greate Day"
print(x)

x="Hello Good Morning, \bNice to meet you, it\'s a greate Day"
print(x)

x="Hello Good Morning, Nice to meet you,\r it\'s a greate Day"
print(x)


#### Python string methods
x="hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.capitalize())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.count("e"))

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.endswith("y"))

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.find("y"))

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(f"Nice words",{x})

x="123443"
print(x.isalnum())

x="123443"
print(x.isdecimal())

x="123443"
print(x.isdigit())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.islower())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.isupper())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.isspace())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.istitle())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.join("\n hello"))

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.splitlines())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.split())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.startswith("H"))

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.swapcase())

x="Hello Good Morning, Nice to meet you, it\'s a greate Day"
print(x.title())



##### LIST METHOS
x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
a=x[6]
print(a)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[2:3])

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[::2])

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[2:7])

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[-7:-1])

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[-7:-1:2])

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print(x[::-1])

##### LIST INCREASE
x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x.append("good night")
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x[1]=1232
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x[3]="HIII"
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x.insert(0,111)
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x1=(11,22,3,44,55,66)
x.extend(x1)
print(x)

#### DECREASE LIST

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x.pop()
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x.pop(1)
print(x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
x.remove("to")
print(x)


#### TUPLE

x=(12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you")
a=x[::-1]
print(a)

x=(12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you")
print(x[2:8])

x=(12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you")
print(x[4])

x=(12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you",)
print(x[-7:-1])

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.add(24)
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.add("Nitin")
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x1={1,2,3,4,6,12,123}
x.update(x1)
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.pop()
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.remove("meet")
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.remove((12))
print(x)

x={12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"}
x.discard(12)
print(x)

#### DICTONARY
x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
print(x)

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
del x["Add"]
print(x)

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
x.pop("Class")
print(x)

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
x.popitem()
print(x)

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
x.clear()
print(x)

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
print(x.keys())

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
print(x.values())

x={"name":"Sandy","Age":35,"Class": "A","Add":"germany"}
print(x.items())


num1=eval(input("Enter a num1: "))
num2=eval(input("Enter a num2: "))
num3=eval(input("Enter a num3: "))

if num2>num1 and num2>num3:
    print("Num2 is grater: ", num2)

elif num3>num1 and num3>num2:
    print("Num3 is grater: ", num3)

else:
    print("Num1 is grater: ",num1)


num1=eval(input("Enter a list"))

for i in num1:
    if i%2==0:
        print(i,end=' ')


x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
if "Good" in x:
    print("Good is present")
else:
    print("good is not present")

x = [12, 123, 12234, "Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print("Good" in x)

x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
print("hii" not in x)


x=[12,123,12234,"Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
if "Good" not in x:
    print("Good is not present")
else:
    print("good is present")

#### TRANSFER STATEMENT

x="Bangalore karnataka"
for i in x:
    if i=="n":
        break
    print(i)



x="Bangalore karnataka"
for i in x:
    if i=="t":
        break
    print(i,end=" ")


x="Bangalore karnataka"
for i in x:
    if i=="t":
        continue
    print(i,end=" ")

x="Bangalore karnataka"
for i in x:
    if i=="a":
        continue
    print(i, end=' ')


x="Bangalore karnataka"
for i in x:
    if i=="o":
        pass
    print(i,end=" ")
from functools import reduce

#### LIST COMPREHENSION
l=[1,2,3,4,5,6,7,8,9,10]
[print(i,end=" ") for i in l if i>=5]

l=[1,2,3,4,5,6,7,8,9,10]
[print(i*2) for i in l ]

l=[1,2,3,4,5,6,7,8,9,10]
[print(i-1) for i in l]

l=[1,2,3,4,5,6,7,8,9,10]
[print(i) for i in l if i%2==0]

l=[1,2,3,4,5,6,7,8,9,10]
[print(i) for i in l if i%2!=0]


x=["Hello", "Good", "Morning", "Nice", "to", "meet", "you"]
[print(i.upper()) for i in x]

names=["Nitin", "Sharan","Rahul"]
age=[27,28,29]
A=[(names,age) for names ,age in zip(names,age) ]
print(A)

names=["Nitin", "Sharan","Rahul"]
age=[27,28,29]
X=[(names,age) for names,age in zip(names,age)]
print(X)

names=["Nitin", "Sharan","Rahul"]
age=[27,28,29]
S=[(names,age) for names,age in zip(names,age)]
print(S)

names=["Nitin", "Sharan","Rahul"]
age=[27,28,29]
A=[(age,names) for age ,names in zip(age ,names)]
print(A)

names=["Nitin", "Sharan","Rahul"]
age=[27,28,29]
a=[(names,age) for names, age in zip(names,age)]
print(a)


x="Hello Good Morning, Nice to meet you "
a=x.split()
for i in a:
    s=i[::-1]
    print(s,end=" ")


x="Hello Good Morning, Nice to meet you "
a=x.split()
a=" ".join(reversed(a))
print(a)



##### LAMBDA FUNCTIONS
add=(lambda a,b:a+b)
print(add(20,30))

add=(lambda a,b:a*b)
print(add(2,4))

add=(lambda a:a*2)
print(add(100))

add=(lambda a,b,c:a+b+c)
print(add(20,20,30))


add=(lambda x,y:x/y)
print(add(3,80))

### MAP

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=list(map(lambda x:x+5,team))
print(add)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=list(map(lambda x: x-1,team))
print(add)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=list(map(lambda x: x, team[::2]))
print(add)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=list(map(lambda x: x, team[::-1]))
print(add)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=list(map(lambda x:x,team[::-1]))
print(add)


#### FILTER
team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
filt=list(filter(lambda x:x==6,team))
print(filt)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
filt=tuple(filter(lambda x: x%2==0, team))
print(filt)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
filt=list(filter(lambda x:x%2!=0, team))
print(filt)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
fllt=list(filter(lambda x:x>=9, team))
print(fllt)

team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
fllt=tuple(filter(lambda x: x<=5, team))
print(fllt)

#### REDUCE
team=[1,2,3,4,5,6,6,7,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
add=reduce(lambda x,y:x+y,team)
print(add)


#### FUNCTIONS

def my_fn():
    x=[1,2,3,4,5,6,1,2,3,4,5,67,7,8,43,3,227,8,9,0]
    l=[]
    for i in x:
        if i not in l:
            l.append(i)
    print(l)

my_fn()


def my_fn():
    l=[1,2,3,4,5,6]
    l2=[2,4,5,7,8,9]
    l3=[]
    for i in l:
        if i in l2:
            l3.append(i)
    print(l3)

my_fn()

#### POSITIONAL ARGUMENT
def my_fn(name,age,add):
    print(f" My name is {name}, I\'m {age} year old, My native place {add} ")

my_fn("Nitin", 26, "Bangalore")


#### KEYWORD ARGUMENT:
def my_fn(a,b,c):
    A=a+b+c
    print(A)

my_fn(b=50,c=30,a=80)


####DEFAULT ARGUMENT:
def my_fn(name="nitin",age=28,add="pune"):
    print(f"my name is {name}, im {age} year old, im from {add}")

my_fn()

def my_fn(fruits="apple",price=200,day="Monday",kg=1):
    print(f"in {day}, {fruits} price is {price} Rupes, per {kg}kg, is too high")

my_fn("Banana",200,"friday",2)

def my_fn(fruits="apple",price=200,day="Monday",kg=1):
    print(f"in {day}, {fruits} price is {price} Rupes, per {kg}kg, is too high")

my_fn()


#### Variable Length Argumnet:

def my_fn(a,*b):
    print(a)
    print(b)

my_fn(1,2,3,4,5,6,6)
my_fn(1,2)


