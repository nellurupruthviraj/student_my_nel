'''

x,y,z="Orange","Apple","Banana"
print(x)
print(y)
print(z)

x=y=z="Orange","Apple","Banana"
print(x)
print(y)
print(z)

x="Awesome"
print(f"python is {x}")


x="Cold"
def my_fn():
    x="Hot"
    print("Bangalore is", x)

my_fn()
print("Bangalore is", x)


x="Cold"
def my_fn():
    global x
    x="Hot"
    print("Bangalore is", x)

my_fn()
print("Bangalore is", x)


#### DATA TYPES

x="Hello"
print(type(x))

x=20
print(type(x))

x=20.7
print(type(x))

x=2+3j
print(type(x))

x=[1,2,3,4,5,"Hello","Hii",200]
print(type(x))

x=(1,2,3,4,5,"nitin","Hello","Hii")
print(type(x))

x={1,2,3,4,5,"apple","Banana","Orange"}
print(type(x))

x=range(1,1)
print(type(x))

x=frozenset((1,2,3,4,5,"apple","banana","Orange"))
print(type(x))

x={"Name":"nitin",
  "age":27,
   "gender": "Male"}

print(type(x))

#### Python Casting,

x=int(20)
print(x)
x=int(20.5)
print(x)
x=int("30")
print(x)


x=(float(20))
print(x)
x=(float(20.5))
print(x)
x=float("30")
print(x)

x=str(20)
print(x)
x=str(20.5)
print(x)
x=str("30")
print(x)

x="hello world"
print(x[8])

for i in "Banana":
     print(i)


x=("Hello good morning, have a nice day")
print(len(x))
print("Hello" in x)
print("good" not in x)

x=("Hello good morning, have a nice day")
print(x[7])
print(x[2:4])
print(x[::2])

x=("Hello good morning, have a nice day")
print(x[-9:-3])

x=("Hello good morning, have a nice day")
print(x.lower())

x=("Hello good morning, have a nice day")
print(x.upper())

x=("Hello good morning, have a nice day")
print(x.strip())

x=("Hello good morning, have a nice day")
print(x.lstrip())

x=("Hello good morning, have a nice day")
print(x.rstrip())

x=("Hello good morning, have a nice day")
print(x.replace("day","month"))

x=("Hello good morning, have a nice day")
a=x.split()
s=" ".join(reversed(a))
print(s)

x=("Hello good morning, have a nice day")
a=x.split()
for i in a:
    a=i[::-1]
    print(a,end=" ")  '''

A=")())(()())(([]{}"
b = {}
for i in A:
    b[i]=A.count(i)
print(b)
x = 0
C = 0
if x == C:
    print("Matching")
else:
    print("Not Matching")