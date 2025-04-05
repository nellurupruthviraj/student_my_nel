##### FUNCTIONS

a="hello"

def my_fn():
    a="Hii"
    print("Nitin: ",a)

my_fn()
print("Nitin:",a)

a="Hello"

def my_f():
    global a
    a="Hii"
    print("NITIN", a)

my_f()
print("NITIN", a)


##### positional Arguments
def my_fnc(a,b):
    c=a+b
    print(c)

my_fnc(10,20)


def my_fnn(a,b,c):
    if a>b and a>c:
        print("a is grater")
    elif b>a and b>c:
        print("b is grater")
    else:
        print("c is grater")

my_fnn(200,100,50)


def my_fcn(name,age,address):
    print(f"Hello, My name is {name}, and Im {age} year old, and im from {address}")

my_fcn("Sharan",22,"Bangalore")


def my_fnc(fruitname,price,kg):
    print(f"monday {fruitname}, price is {price} rupers for a {kg} kg")

my_fnc("Apple", "150/-",2)
my_fnc("Banana", "100/-", 5)



##### KEYWORD ARGUMENT

def my_fn(a,b,c):
    x=a+b*c
    print(x)

my_fn(c=10,a=12,b=9)

####Program-2

def my_fn(a,b,c):
    if a>b and a>c:
        print("a is grater")
    elif b>a and b>c:
        print("b is grater")
    else:
        print("c is grater")

my_fn(a=15,c=10,b=24)


def my_fn(name, age, address):
    print(f"My name is {name}, and i am {age} years old, and i\'m from {address}")

my_fn(age=31,address="Pune",name="Rolex")


def my_fn(fruit,price,kg):
    print(f"yesterday {fruit} price is {price} rupes, per {kg} kg")

my_fn(kg=2,price="120.00 /-",fruit="Mango")
my_fn(price="150.00 /-",kg=5,fruit="Orange")


def my_fn(length, width):
    c=length*width
    print(c)

my_fn(width=40,length=20)



#### DEFAULT ARGUMENT:

def my_fn(a=20,b=10):
    c=a+b
    print(c)

my_fn()


def my_fn(a=20,b=10):
    c=a+b
    print(c)
my_fn()
my_fn(5,8)


def my_fn(name="Nitin",age=27,address="Bangalore"):
    print(f"My name is {name}, i\'m {age} year old, i\'m from {address}")

my_fn()
my_fn("sharan",30,"pune")



##### VARIABLE LENGTH ARGUMENT

def my_fn(a,*b):
    print(a)
    print(b)

my_fn(1,2,3,5,6)

def my_fn(*a):
    c=a
    print(c)

my_fn(1,2,3,4,5,6,7,8,9)



def my_fn(a,*b):
    print(a)
    for i in b:
        if i%2==0:
            print(i,end=' ')

my_fn(1,2)
my_fn(1,2,3,4,5,6,7,8,9,10)


#### COMBINATION OF ARGUMENTS:

def my_fn(a,b):
    s=a+b
    print(s)

my_fn(50,b=20) ### This type is work


def my_fn(a,b):
    s=a+b
    print(s)

#my_fn(a=50,20)  ### This type is not work

