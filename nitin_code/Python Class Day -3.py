x=5
x="nitin"
print(type(x))

something="orange","banana","cherry"
x,y,z=something
print(x)
print(y)
print(z)


x=y=z ="orange","banana","cherry"
print(z)
print(y)
print(x)

x="Good"
print("Bangakore climet is", x)

x="super"
def myfunc():
    x="good"
    print("python is", x)

myfunc()
print("python is",x)

x="super"
def myfnc():
    global x
    x="good"
    print("pyhton is", x)

myfnc()
print("python is", x )


### Data types

x="Bangalore"
print(type(x))

x=392
print(type(x))

x=540.55
print(type(x))

x=10+3j
print(type(x))

x=["nitin",20,"Bangalore",12.1]
print(type(x))

x=("nitin",20,"Bangalore",12.1)
print(type(x))

x=range(10)
print(type(x))

import random

print(random.randrange(100,200))

x={"Name":"Rahul", "Age":30,"class":"puc","address":"Bangalore"}
print(type(x))

x={"Nitin",26,"bangalore",9900220022}
print(type(x))

x=frozenset(("Nitin",26,"bangalore",9900992200))
print(type(x))

x=int(1)
print(x)
x=int(2.8)
print(x)
x=int("3")
print(x)

x=float(1)
print(x)
x=float(2.8)
print(x)
x=float("3")
print(x)
x=float("4.2")
print(x)

x=str("s1")
print(x)
x=str(2)
print(x)
x=str(3.4)
print(x)

### indexing

x="Hello Bangalore, good morning"
print(x[20])

x="Hello Bangalore, good morning"
a=len(x)//2
print(x[a:])
print(x[:a])
print(x[2:20])
print(x[-10:-2])

## Break, Continue and Pass Statements

x="Banana"
for s in x:
    if s=="n":
        break
    print(x)

x="Hello Bangalore, good morning"
for i in x:
    if i=="g":
        continue
    print(i,end=" ")

x="Hello Bangalore, good morning"
for i in x:
    if i=="e":
        pass
    print(i,end=" ")


## functions

x="Hello bangalore, good morning"
print(x.title())

x="Hello Bangalore, good morning"
print(x.upper())

x="Hello Bangalore, good morning"
print(x.lower())

x=" Hello Bangalore, good morning  "
print(x.strip())

x="   Hello Bangalore, good morning  "
print(x.rstrip())

x="   Hello Bangalore, good morning  "
print(x.lstrip())

x="Hello Bangalore, good morning"
print(x.replace("Hello","Hii"))

x="Hello Bangalore, good morning"
print(x.split())

x="Hello Bangalore, good morning"
print(len(x))
print(len(x.replace(" ","")))


## format strings

a="Bangalore\\hyderabad"
b="pune\\goa"
c="delhi"
x="I know {} {} These citys and one more city i know {}"

print(x.format(b,a,c))


a="Bangalore\\hyderabad"
b="pune\\goa"
c="delhi"
x="I know {1} {0} These citys and one more city i know {2}"

print(x.format(a,b,c))




x="Hello Bangalore, good morning, it\'s good moment"
print(x)

x="Hello Bangalore,\n good morning, it\'s good moment"
print(x)

x="Hello Bangalore,\n \\good morning,\\ it\'s good moment"
print(x)

x="Hello Bangalore,\ngood morning, \rits good moment"
print(x)

x="Hello Bangalore, good \r morning"
print(x)

x="Hello\t Bangalore,\t good \tmorning"
print(x)

x="Hello \bBangalore, good \bmorning"
print(x)

x="Hello Bangalore,\f good \fmorning"
print(x)

x="Hello Bangalore, good\000 morning"
print(x)

x="Hello Bangalore, good morning"
print(x)


### list

x=["nitin",132,2552.2,"bangalore"]
print(x)
print(x[0])
print(x[0:2])
print(x[:])
print(x[::2])
print(x[-1])
print(x[-4:-2])

## APPEND
x=["nitin",132,2552.2,"bangalore"]
x.append("hyd")
print(x)

x=["nitin",132,2552.2,"bangalore"]
x.append("pune")
print(x)

## INSERT
x=["nitin",132,2552.2,"bangalore"]
x.insert(1,"Sharan")
print(x)

### EXTEND
x=["nitin",132,2552.2,"bangalore"]
a=["Rahul",121,64.2,"delhi"]
x.extend(a)
print(x)


### POP
x=["nitin",132,2552.2,"bangalore","delhi","Goa"]
print(x)
x.pop()
print(x)

x=["nitin",132,2552.2,"bangalore","delhi","Goa"]
print(x)
x.pop(0)
print(x)


### remove
x=["nitin",132,2552.2,"bangalore","delhi","Goa"]
x.remove(2552.2)
x.remove("delhi")
print(x)


#### TUPLE
### INDEXING AND SLICING
x=("Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad")
print(x[3])
print(x[1])
print(x[-1])

print(x[1:])
print(x[1::2])
print(x[:])
print(x[::2])
print(x[-4:])


#### SET

x={"Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad"}
x.add("pune")
x.add("kerala")
print((x))

x={"Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad"}
x1={"Nitin","Kannur","Mumbai","Kochi",30,29,39,2020}
x.update(x1)
print(x)


x={"Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad"}
x.pop()
print(x)

x={"Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad"}
x.remove("Goa")
print(x)

x={"Nitin","Bangalore",2020,20.20,"delhi","Goa","Hydrabad"}
x.discard("Go")
print(x)


### Dictionary

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x)
x["ID Card"]="YES"
x["Result"]="PASS"
print(x)

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x)
x.pop('age')
print(x)
x["age"]=22
print(x)

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
x.popitem()
print(x)


x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x.keys())

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x.values())

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x.keys())

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x.values())

x={"Name":"Rahul","age":30,"address":"Bangalore","MNo":9900998800}
print(x.items())


X="3[a2[d]]"
z=[]
A=str(X)
for i in A:
    if i=="a":
        a=(i*3)
        z.append(a)
    if i=="b":
        a=(i)
    if i=="c":
        c=(i)
        M=a+c
        z.append(M)
        n=a+c
        z.append(n)
        print(z)

S="3[a2[c]]"
def decode_string(S):
    num1=int(s[0])
    num2=int(s[3])
    return 'acc'


