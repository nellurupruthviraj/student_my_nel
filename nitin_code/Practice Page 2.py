

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
   print(letter*5,end=" ")

