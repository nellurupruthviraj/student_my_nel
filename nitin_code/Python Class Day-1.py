#### Python Class Day-1###

# Python files are ending with .py
print("Hello World!")

##python Types of errors:

###Syntax error:(it means we missed cotes or brackets or equal symbol or ect.)
'''
A=("Bangalore)
print(A)

print=("hello good evening)

print=("India"

print"Bangalore"  

### Name Error:( We given a different Variable name that is name Error )

L=("Bangalore, Karnataka")
print(s) 

Z=[1,2,3,4,5,6,7,8]
print(Z)

Z=[1,2,3,4,5,6,7,8]
print(z) 

### Type Error:(It Means we can't combine a different data types)

X=72636
Y="Hello"
print(X+Y)

C=("12345666")
D=[1,2,3,45,6,7,7]
print(C+D)  

### Value Error:(in this specify a different data type)

A=int("Hello")
print(A) 

### INdex Error:(It means providing a wrong index number)

A=[1,2,3,4,5,6]
print(A[4])

S=("Bangalore Karnataka")
print(S[8])

Index Error:
C=("Hello Good Morning")
print(C[18])

###Endex Error:
Z=[33,4,56,88,66,65,4,4,3,333]
print(Z[18])  


#### Key Error:(In Dict puting a key Value Different)

My_Dict={"Name": "Nitin", "Age":26,
         "Nam": "Sharan", "Ag":28,
         "Na": "Rahul", "A":29}

print(My_Dict)
print(My_Dict["Name"])
print(My_Dict["Nam"])
print(My_Dict["Na"])

### This the Key Error:
My_dict={"Name": "Nitin", "Age":26,
         "Nam": "Sharan", "Ag":28,
         "Na": "Rahul", "A":29}

print(My_dict)
print(My_dict["Namee"])
print(My_dict["Naam"])
print(My_dict["NNa"]) 


#### Import Error:( Importing the non-Existing moduls)

import "panda" as pd
import numpy as np



#### Runtime Error:( 


#### Python Single line comment(#),
#### Python Multi line Comment('''''')

#### Variable:(which is a variable identify the value)

X=555
x="Nitin"

print(X,x)

A=str(3)
print(A)

y=int(4)
print(y) 

#### type(it will the data type)
A=("Hello How is the day")
print(type(A))

B=[1,2,3,5,5,6,78,89]
print(type(B))

C={'Banana':222, "Apple":245,}
print(type(C))


### Variable Names:
### Camel Case:(my VariableName = "Nitin")
my_VarName="Nitin"
print(my_VarName)
### Pascal Case:(MYVariableName = "Nitin")
MyVarName="Bangalore"
print(MyVarName)
### Snake Case:(my_Variable_name = "Nitin")
my_var_name="Karnataka"
print(my_var_name)


### One Value multiple Values

X=Y=Z="Nitin","Hello","How"
print(Z)
print(Y)
print(Z)

x,y,z="Hello","Good","Morning"
print(x)
print(y)
print(z)


Name="Nitin"
age=26
is_student = False
weight=60.5

print(type(Name))
print(type(age))
print(type(weight))
print(type(is_student))

is_student="yes"
print(type(is_student))

age_float=float(age)
print(age_float)

s="1000"
print(type(s))

A=100.33
A_int=int(A)
print(A_int)

S=1234
a_float=float(S)
print(a_float)

W="1000"
E=848
print(int(W)+E)

x="Awesome"
print("Python is" " "+ x)

D="Hello Good evening"
L="How are you"
print(D +" " "Welcome to bangalore" " "+L)

#### Arithmatical operator:
n=10
m=3
print(n+m)  #output:13
print(n-m)  #output:7
print(n*m)  #output:30
print(n/m)  #output:3.333
print(n//m) #output:3 (Floor Division)
print(n%m)  #output:1 (Modules)
print(n**m) #output:1000 (Exponetiation)  


## Global Variable:

x="Awesome"
def myfunc():
    x="Fantastic"
    print("python is" + x)

myfunc()
print("python is" + x)

S = "Bangalore in karnataka"
def nitin():
    S="Karnataka in india"
    print("state" " "+ S)

nitin()
print(S)

z="Hello Good Morning Everyone"
def my_func():
    z="lets start the show"
    print("Hii" + z)

my_func()
print(z)

a="Bangalore is cool city"
def bang():
    a="Bangalore is traffic city "
    print("In Karnataka" " "+ a)

bang()
print(a)


a="Bangalore is cool city"
def bang():
    global a
    a="Bangalore is traffic city "
    print("In Karnataka" " "+ a)

bang()
print("In Karnataka" " "+a)


C="Nice to meet you"
def func():
    global C
    C="Have a nice day"
    print("Hii Good Morning" " "+C)

func()
print("Hii Good Morning" " "+ C)'''

### Data types:
'''a="Hello world"
print(type(a))

b=20
print(type(b))

c=20.5
print(type(c))

d=1j
print(type(d))

e=["Apple","Banana"]
print(type(e))

f=("Apple","Banana")
print(type(f))

g=range(6)
print(type(g))

h={"Name": "Nitin", "Age":26}
print(type(h))

i={"apple", "Banana"}
print(type(i))

j=frozenset[{"Apple","Banana"}]
print(type(j))

k=True
print(type(k))

l=b"Hello"
print(type(l))

m=bytearray(5)
print(type(m))

n=memoryview(bytes(5))
print(type(n))  '''


#### specify the data type:
a=str("Hello World")
print(a)

b=int(20)
print(b)

c=float(20.5)
print(c)

d=complex(1j)
print(d)

e=list(("Apple","Banana"))
print(e)

f=tuple(("apple","banana"))
print(f)

g=range(6)
print(g)

h=dict["Name":"Jhon","age":45]
print(h)

'''
i=set("Apple","banana")
print(i) '''

j=frozenset(("Apple","Banana"))
print(j)

k=bool(5)
print(k)

x,y,z="orange","banana","Cherry"
print(x)

x=y=z ="orang","banan","Cherr"
print(x)

#### Ascending order
G=[1,2,4,2,1,2,3,4,4,5,6,9,54]
G.sort()
print(G)

x=["Apple","Banana"]
print(type(x))

### INT
x=int(1)
print(x)

x=int(2.8)
print(x)

x=int("3")
print(x)

### FLOAT
x=float(1)
print(x)

x=float(2.8)
print(x)

x=float("3")
print(x)

x=float("4.2")
print(x)

### STR
x=str("s1")
print(x)

x=str(2)
print(x)

x=str(3.0)
print(x)


### Index Number
a="Hello World"
print(a[1])

### Looping Through a String
for x in "Banana":
    print(x)

for x in "Bangalore city":
    print(x)

### String Length
a="Hello good morning"
print(len(a))

x="Hello Bangalore , how is the day"
print(len(x))

#### Check string
txt= "The best things in life are free"
print("free" in txt)

t="Hii goog morning welcome to delhi"
print("to" in t)

t="Hii goog morning welcome to delhi"
print("delhi" in t)

txt= "The best things in life are free"
if "free" in txt:
    print ("free , 'free' is present")

N="HI MY name is Nitin"
if "name" in N:
    print("yes, 'name' is present")


txt="Bangalore city in karnataka"
if "india" not in txt:
    print("yes,'india' not in txt")

t="Hii goog morning welcome to delhi"
print("delhi" not in t)

r="I am in Bangalore"
print("in" in r)

l=[1,2,3,3,4,5,6,67,78]
for x in l:
    print(x)


### we can write a multiple lines in thribale cot

a=('''india is my country have greate of msjusgjdghgfddfhjfjhdfwefdufwfwe''')
print(a)