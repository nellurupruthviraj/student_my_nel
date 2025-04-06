
myVariableName="Nitin" ###  Camelcase

MyVariableName="Nitin"  ### PascalCase

my_variable_name="nitin" #### snake case


######

x,y,z="apple","orange","banana"
print(y)
print(z)
print(x)

x=y=z="apple","orange","banana"
print(y)
print(z)
print(x)


##### GLOBAL VARIABLE
x="city"
def my_fn():
    x="big city"
    print("bangalore ", x)

my_fn()
print("bangalore ", x)

x="city"
def my_fn():
    global x
    x="big city"
    print("bangalore",x)

my_fn()
print("bangalore ", x)

x="nitin"
print(type(x))

x=20
print(type(x))

x=20.7
print(type(x))

x=3+2j
print(type(x))

x=[1,2,3,4,5,"nitin","sharan","naveen"]
print(type(x))

x=(1,2,3,"nitin","rahul","sharan")
print(type(x))

x=range(2,10)
print(type(x))

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
print(type(x))
del x["C"]
print(x)

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
x.pop("B")
print(x)

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
x.popitem()
print(x)


x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
a=x.keys()
print(a)

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
a=x.clear()
print(a)

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
a=x.values()
print(a)

x={"name": "nitin", "age":26,"address":"Bangalore","A":100,"B":200,"C":300}
a=x.items()
print(a)

x={10,203,10,40,50,"nitin","rahul","sharan"}
print(type(x))
print(x)

x=frozenset(("nitin","sharan",201,203,404,40))
print(type(x))

x=10
c=10
print(x is not c)

import random
print(random.randrange(10))

x=3.5
print(int(x))
print(float(x))
print(str(x))


x=30
print(int(x))
print(float(x))
print(str(x))

x="30"
print(int(x))
print(float(x))
print(str(x))

x="hello good morning"
print(x[2])

x="hello good morning"
print(x[2:])

x="hello good morning"
print(x[2:6])

x="hello good morning"
print(x[:])

x="hello good morning"
s=x.split()
for i in s:
    print(i[::-1],end=" ")

x = "hello good morning"
print(x[-15:])

txt="Happy diwali to all"
if "all" in txt:
    print("all is present")

txt = "Happy diwali to all"
if "hello" not in txt:
    print("hello is not present")


txt = "Happy diwali to all,weLcome to my Home"
print(txt.upper())

txt = ("    Happy diwali to all,weLcome to my Home   ")
print(txt.lower())

txt = ("    Happy diwali to all,weLcome to my Home   ")
print(txt.strip())

txt = ("    Happy diwali to all,weLcome to my Home   ")
print(txt.lstrip())

txt = ("    Happy diwali to all,weLcome to my Home   ")
print(txt.rstrip())

x=[1,1,22,22,22,3,3,3,3,3,33,3,3,5,6,6,7,8,6,5,6,7,8,9,]
print(x.count(22))
print(x.count(6))
print(x.count(3))
print(sum(x))
print(max(x))
print(min(x))


x = ("Happy diwali to all,weLcome to my Home")
print(x.index("H"))
print(x.index("t"))
print(x.index("e"))
print(x.index("m"))

x=500
v=800
s=x-v
print(s)
print(abs(s))

x = ("Happy diwali to all,weLcome to my Home")
print(x.replace("diwali","Holly"))
print((x.replace("Home","Hotel")))

x = ("Happy diwali to all, weLcome to my Home")
s=x.split()
print(s)

for i in s:
    s=i[::-1]
    print(s,end=" ")

x = ("Happy diwali to all, weLcome to my Home")
s=x.split()

a=" ".join(reversed(s))
print(a)

x = ("Happy diwali to all, weLcome to my Home")
print(len(x))

x=[1,1,22,22,22,3,3,3,3,3,33,3,3,5,6,6,7,8,6,5,6,7,8,9,]
print(sorted(x))

x = ("Happy diwali to all, weLcome to my Home, it\'s a happy moment")
print(x)

x = ("Happy diwali to \\ all,weLcome to my Home,\\ it\'s a happy moment")
print(x)

x = ("Happy diwali to all,\n weLcome to my Home,\n it\'s a happy moment")
print(x)

x = ("Happy diwali to all, weLcome\r  to my Home, it\'s a happy moment")
print(x)

x = ("Happy \tdiwali to all, \tweLcome to my Home, it\'s a happy moment")
print(x)

x = ("Happy\b diwali to \ball, weLcome to my Home, it\'s a happy moment")
print(x)



###### CONDITIONAL STATEMENT
num1=eval(input("Enter a number1: "))
num2=eval(input("Enter a number2: "))
num3=eval(input("Enter a number3: "))

if num1>num2 and num1>num3:
    print(f"NUM1: {num1} is grater")
elif num2>num1 and num2>num3:
    print(f"NUM2: {num2} is grater")
else:
    print(f"NUM3: {num3} is grater")



####  TRANSFER STATEMENT
x="Nitin Kannur welcome to bangalore"
for i in x:
    if i == "l":
        break
    print(i)

x="Nitin Kannur welcome to bangalore"
for i in x:
    if i=="K":
        continue
    print(i, end=' ')


x="Nitin Kannur welcome to bangalore"
for i in x:
    if i=="K":
        pass
    print(i,end=" ")

x="Nitin Kannur welcome to bangalore"
i=0
while i<=len(x):
    if i=="w":
        break
    print(i,end=' ')
    i+=1


i=0
while i<=10:
    if i==5:
        break
    print(i)
    i+=1

i=0
while i<=10:
    if i==6:
        continue
    print(i,end=' ')
    i+=1

i=0
while i<=10:
        print(i)
        i+=1


x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
for i in x:
    if i==43:
        print(i)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x.append(50)
print(x)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x.insert(2,111)
print(x)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x1=[10,20,30,40,50]
x.extend(x1)
print(x)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x.pop()
print(x)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x.pop(4)
print(x)

x1=[10,20,30,40,50]
x1.pop(3)
print(x1)

x=[1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7]
x.remove(43)
print(x)


#### tuple
x=(1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7)
a=x[2:6]
print(a)

x=(1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7)
a=x[5]
print(a)

x=(1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7)
a=x[-10:-4]

print(list(a))

x={1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88}
x.add(600)
print(x)

x={1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7}
x.add(1122)
print(x)

x={1,2,3,4,3,2,1,2,3,43,2,1,2,35,6,7}
x1=(10,20,30,40,60,60,70)
x.update(x1)
print(x)


x={10,203,30,40,2,3,403,203,4022}
x.pop()
print(x)

x={10,203,30,40,2,3,403,203,4022}
x.remove(403)
print(x)

x={10,203,30,40,2,3,403,203,4022}
x.discard(4031)
print(x)


x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
print(x)

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
print(x.keys())

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
print(x.values())

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
print(x.items())

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
del x['Add']
print(x)

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
x.pop('age')
print(x)

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
x.popitem()
print(x)

x={"name":'Nitin',"work":"engineer","age":26,"Add":"Bangalore"}
x.clear()
print(x)


#### LIST COMPREHENSION
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(i) for i in x if i==15]

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(i,end=' ') for i in x if i>=10]

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(i,end=' ') for i in x if i<=10]

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(i,end=' ') for i in x if i%2==0]

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(i,end=' ') for i in x if i%2!=0]


x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[print(x[::2])]


##### lAMBDA FUNCTIONS

X=(lambda x,y:x+y)
print(X(10,20))

x=(lambda a: a*2)
print(x(5))

###  MAP
data=[10,203,40,20,201,1,5,10,15,25]
add=list(map(lambda x: x+20,data))
print(add)

data=[10,203,40,20,201,1,5,10,15,25]
re=tuple(map(lambda x: x*2,data))
print(re)

data=[10,203,40,20,201,1,5,10,15,25]
rem=list(map(lambda x:x-10, data))
print(rem)

data=[10,203,40,20,201,1,5,10,15,25]
a=list(map(lambda x:x/2,data))
print(a)


### FILTER
data=[10,203,40,20,201,1,5,10,15,25]
A=list(filter(lambda x: x>=40, data))
print(sorted(A))

data=[10,203,40,20,201,1,5,10,15,25]
a=list(filter(lambda x:x<=50,data))
print(sorted(a))

data=[10,203,40,20,201,1,5,10,15,25]
a=list(filter(lambda x: x, data[::2]))
print(a)

data=[10,203,40,20,201,1,5,10,15,25]
a=list(filter(lambda x:x%2==0, data))
print(a)

data=[10,203,40,20,201,1,5,10,15,25]
a=list(filter(lambda x: x%2!=0, data))
print(a)


#### REDUCE
data=[10,203,40,20,201,1,5,10,15,25]
a=reduce(lambda x, y: x+y,data)
print(a)

data=[10,203,40,20,201,1,5,10,15,25]
a=reduce(lambda x,y:x-y,data)
print(a)


#### DEF FUNCTIONS

def my_fn():
    x=[1,2,3,4,5,5,6,6,7,7,8,8,9,10,11,12,13,14,15,16,17,18,19,20]
    l=[]
    for i in x:
        if i not in l:
            l.append(i)
    print(l)

my_fn()


a=[1,1,1,2,2,3,3,4,4,5,5,6,6,7,8,]
l=[]
for i in a:
    if i not in l:
        l.append((i))
print(l)


#### POSITIONAL ARGUMENT
def my_fn(num1, num2, num3):
    if num1>num2 and num1>num3:
        print("NUM1:", num1,"is grater")

    elif num2>num1 and num2>num3:
        print("NUM2: ",num2, "is grater")

    else:
        print("NUM3:",num3, "is greater")

my_fn(599,499,399)
my_fn(20,40,30)


def my_fn(date,day,shares,price):
    print(f"{date}, {day}, {shares} shares price is. {price} Rupes,")

my_fn("07/04/2025", "Monday","TATA","2400 /-")


my_fn("09/04/2025", "sunday","JIO","5000 /-")



#### KEYWORD ARGUMENT
def my_fn(a,b):
    c=a+b
    print(c)

my_fn(b=10,a=6)

def my_fn(a,b):
    a.extend(b)
    print(a)

my_fn(a=[1,2,3,4,5,],b=[6,5,7,8,9,3])

def my_fn():
    a="hello good morning"
    s=a.split()
    for i in s:
        a=i[::-1]
        print(a,end=' ')
my_fn()


def my_fn(a):
    for i in a:
        if i%2==0:
            print(i,end=' ')

my_fn(a=[1,2,3,4,5,6,7,8,9,10])


def my_fn(a):
    for i in a:
        if i%2!=0:
            print(i,end=' ')

my_fn(a=[1,2,3,4,5,6,7,8,9,10])


#### KEY WORD ARGUMENT

def my_fn(day,name,price,kg):
    print(f"{day} in a market {name} price is {price} Rupres, of a {kg}kg.")

my_fn(name="Apple",price="200 /-",day="Sunday",kg=2)
my_fn(name="Banana",price="800 /-",day="monday",kg=10)
my_fn(name="Orange",price="1000 /-",day="saturday",kg=10)

def my_fn(a,b,c):
    c=a+b+c
    print(c)

my_fn(b=20,c=10,a=30)


#### DEFAULT ARGUMENT

def my_fn(name="Nitin",age=27,address="bangalore"):
    print(f"My name is {name}, I am {age} year old, and I am from {address}")

my_fn()

def my_fn(name="jhon",age=30,address="delhi"):
    print(f"My name is {name}, I am {age} year old, and I am from {address}")

my_fn()

def my_fn(name="jhon",age=30,address="delhi"):
    print(f"My name is {name}, I am {age} year old, and I am from {address}")

my_fn("Ironman",100)

def my_fn(name="jhon",age=30,address="delhi"):
    print(f"My name is {name}, I am {age} year old, and I am from {address}")

my_fn("superman",100, "america")



def my_fn(*a,):
    print(a)

my_fn(1,2,3,5,6,7)
my_fn(10)

'''def my_fn(*a,b):
    print(a)
    print(b)     ### Its not work

my_fn(10,20,304,40)'''


def my_fn(a,*b):
    print(a)
    print(b)

my_fn(10,20,304,40)
my_fn(1,2)


