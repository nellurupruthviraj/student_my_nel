from itertools import count

x="Nitin"
print(x)

x=5
print(x)

x,y,z="Nitin", "Kannur", "Gulbarga"
print(y)
print(x)
print(z)

x=y=z="Nitin", "Kannur", "Gulbarga"
print(z)
print(y)
print(x)

X="Hello"
print(X,"Good morning")
print("he said daily", X)


x="coming"
def my_fn():
    x="going city"
    if "city" in x:
        print("city is present")
    print("sandy is", x)

my_fn()
print("sandy is", x)


x="coming"
def my_fnn():
    global x
    x="going city"
    if "bang" not in x:
        print("bang is not present")
    print("sandy is", x)

my_fnn()
print("sandy is", x)

x=("nitin")
print(type(x))

x=509888
print(type(x))

x=635.46
print(type(x))

x=3+3j
print(type(x))

#### List
x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(type(x))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x.count(10))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(sum(x))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(max(x))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(min(x))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
a=x[2]=555
print(x)

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
x.insert(2,555)
print(x)

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
x.insert(8,5500)
print(x)

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
x.append(1110)
print(x)

x=[10,20,30,40,50]
x1=[20,30,40,50,60]
x.extend(x1)
print(x)

x=[10,20,30,40,60]
print(x.pop())
print(x.pop(0))

x=[10,20,30,40,50]
x.remove(50)
print(x)

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
a=x[5]
print(a)

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[-1])

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[::2])

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(len(x))

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[2:5])

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[::-1])

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[-8:-2])

x=[10,10,10,10,20,20,20,30,40,40,50,50,60,60,60]
print(x[-11:-8])

### tuple
x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(type(x))

x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(x[:])

x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(x[:5])

x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(x[::2])

x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(x[4])

x=(1,203,40,"Bangalore", "delhi", "pune", "goa")
print(x[-5:-2])

t=(20,30,"nn","ss")
t1=(40,"bb","cc",90)
s=t+t1
print(s)



#### SET
x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
print(type(x))

x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
print(len(x))

x={10,20,30,40,50}
print(sum(x))

x={10,20,30,40,50}
print(max(x))

x={10,20,30,40,50}
print(min(x))

x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
x.add("200")
print(x)

x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
x1={10,20,"nitin","kannur"}
x.update(x1)
print(x)

x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
print(x.pop())

x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
x.remove("goa")
print(x)
x={1,203,40,"Bangalore", "delhi", "pune", "goa"}
x.discard("g")
print(x)

x=[10,20,30,40,50,60,"apple","Banana","Mango"]
x.clear()
print(x)

X=[10,20,30,40,50,60,"apple","Banana","Mango"]
del x
print(X)
