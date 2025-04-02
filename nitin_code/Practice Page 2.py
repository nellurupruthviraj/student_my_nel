
'''
A= "hello good morning how is the day, welcme a bangalore"
a=len(A)//2
print(A[a:])

x=1
if x==10:
    print("yes X is 10")
else:
   print("x is diffent")


X=24
if X%2==0:
   print("X is even")
else:
   print("X is odd ")


Signal="red"

if Signal=="red":
   print("Stop")
else:
   print("Go")

Signal = "green"

if Signal=="red":
   print("Stop")
elif Signal=="yellow":
   print("Ready")
else:
   print("Go")

Signal = input("What is the colour of singnal: ")

if Signal=="Red":
   print("Stop")
elif Signal=="Yellow":
   print("Ready")
elif Signal=="Green":
   print("GO")
else:
   print("User added Different colour")

def my_fun():
   Time=20

   if Time==8:
      print("Its Breakfast time")
   elif Time==13:
      print("Its lunch time")
   elif Time==20:
      print("Its a Dinner Time")
   else:
      print("Its not meal time")

my_fun()


A=(int(input("Enter Att: ")))

if A>=75:
   print("EXAM")
elif A>45:
   print("EXAM")
elif A<45:
   print("To see")
else:
   print("NO Exam")


gender = input("Enter gender: ")
age = int(input("Age: "))
if gender=="female":
   print("FREE")
else:
   if age <= 5:
      print("Free Child")
   elif age<=12:
      print("Half Ticket")
   elif age>=60:
      print("senior citizen discount")
   else:
      print("Pay full amount")



#### LOOPS

condition =True

while condition:
   print("condition is True")


is_failed =True
i=1

while is_failed and i<=100:
   print(f"Try {i}")
   i+=1
   if i>100:
      break

print("I gave up!")

i=0
while i<=10:
   print("Nitin"*i)
   i+=1

pin ="1234"
trails=0

while trails<3:
   input_pin=input(f"Trail-{trails} | pin: ")
   trails +=1
   if input_pin== pin:
      print("CORRECT")
      break
   else:
      print("INCORRECT")



####FORLOOP

for i in range(1,20):
   print(i,end=" ")

for i in range(1,5):
   print(i,end=" ")

for i in range(10,50):
   if i%2==0:
      print(i,end=" ")

for i in range(10,20):
   print(i)

for i in range(10,21):
   print(i, end=" ")

for i in range(10,21):
   if i%2==0:
      print(i, end=" ")


for i in range(10,25):
   if i%2==1:
      print(i,end=" ")


for i in range(10,21):
   print(i)

for i in range(10,21):
   print(i,end=" ")

for i in range(10,21):
   if i%2==0:
      print(i)

for i in range(10,21):
   if i%2==0:
      print(i,end=" ")

for i in range(10,21):
   if i%2==1:
      print(i)

for i in range(10,21):
   if i%2==1:
      print(i,end=" ")


A="Hello Good Morning, how are you, when you came , nice to meet you"
a=len(A)//2
print(A[:a])

A="Hello Good Morning, how are you, when you came , nice to meet you"
s=len(A)//2
print(A[s:])

bag=["red","green","yellow"]
for ball in bag:
   print(ball)

bag=["red","green","yellow"]
for ball in bag:
   print(ball, end=" ")

name="Nitin"
for letter in  name:
   print(letter*2)

name="Nitin"
for letter in name:
   print(letter*5,end=" ") '''

n=1
while n<=3:
   print(n)
   n+=1

X=str(3)
print(X)

x=5
y="Jhon"
print(type(x))
print(type(y))


x,y,z="orange","banana","cherry"
print(x)

x=y=z="orange","banana","cherry"
print(x)

x="awesome"
print("python is" ,x)


X="super"

def my_fn():
   X="Nice"
   print("India is", X)

my_fn()
print("America is", X)

X="super"

def my_fnc():
   global X
   X="Nice"
   print("India is", X)

my_fnc()
print("America is" , X)

x="Hello World"
print(type(x))

x=20
print(type(x))

x=20.5
print(type(x))

x=2+10j
print(type(x))

x=["Apple","Banana"]
print(type(x))

x=("Apple","Banana","mango")
print(type(x))

x=range(1,10)
print(type(x))

x={"name":"Nitin","age":26,"address":"Bangalore"}
print(type(x))

x={"Apple","Banana"}
print(type(x))

x=frozenset(("apple","Banana", "Mango"))
print(type(x))

x=True
print(type(x))

import random
print(random.randrange(1,10))

a="hello world"
print(a[1])
print(a[6])

x="banana"
for i in x:
   print(i)

a="hello wolrd"
print(len(a))

x="the best things in life are free!"
print("free" in x)
print("are" not in x)

A="Hello, World!"
print(A[2:5])

A="Hello, World!"
print(A[:])

A="Hello, World!"
print(A.upper())

A="Hello, World!"
print(A.lower())

A=" Hello, World! "
print(A.strip())

A="Hello, World!"
print(A.lstrip())

A="Hello, World!"
print(A.rstrip())

A="Hello, World!"
print(len(A))

A=[11,1,12,3,4,5,6,4,4,3,3,44,5]
print(A.count(3))
print(A.count(4))
print(sum(A))

A="Hello, World!"
print(A.replace("World","India"))
print(A.replace("World","Karnataka"))

A="Hello, World!"
print(A.split())

A="Hello, World!"
A="Hello, World!"

print(A+" "+ A)

A="Nitin"
B="Bangalore"
C= "Day"
S="Hello {}, You are from {}, Have a good {}"
print(S.format(A,B,C))

A="Hello, Wor\'ld!"
print(A)

A="It\'s Very good"
print(A)

A="Hello, \\World!"
print(A)

A="Hello,\n World!"
print(A)

A="Hello, \r World!"
print(A)

A="Hello, \tWorld!"
print(A)

A="Hello, \bWorld!"
print(A)

A= "hello good morning how is the day, welcome a bangalore"
print(A.capitalize())

A= "hello good morning how is the day, welcome a bangalore"
print(A.casefold())

A= "hello good morning how is the day, welcome a bangalore"
print(A.encode())

A= "hello good morning how is the day, welcome a bangalore"
print(A.endswith("bangalore" ))

A= "hello good morning how is the day, welcome a bangalore"
print(A.expandtabs())

A= "hello good morning how is the day, welcome a bangalore"
print(A.find("a"))
a=len(A)// 2
print(A[:a])
print(A[a:])

A= "hello good morning how is the day, welcome a bangalore"
print(A.find("g"))

z="Nice meet you"
A= "hello good morning how is the day, welcome a bangalore, {}"
print(A.format(z))

A= "hello good morning how is the day, welcome a bangalore"
print(A.format_map("is"))

A= "hello good morning how is the day, welcome a bangalore"
print(A.index("m"))

A= "hello good morning how is the day, welcome a bangalore"
print(A.isalnum())

A= "hello good morning how is the day, welcome a bangalore"
print(A.isdecimal())

################## BOOOLEAN:

print(10>9)
print(10==9)
print(10<9)


a=200
b=33

if b>a:
   print("b is grater then a")
else:
   print("b is not grater then a")








'''A="Nitin"
for i in A:
   print(i,end=" ")


A='Nitin Kannur'
for i in A:
      print(i*2,end=" ")



####for i in range(1,11):
  ### print(f"2X{i}={2*i}")'''
