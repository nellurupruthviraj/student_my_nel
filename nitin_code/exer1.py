'''A="HELLWORLD 123HELLOWORLD"
s=A[2:-1]
print(s)

S=A[5:-3]
print(S)

S=A[10:13]
print(S)

S=A[10:]
print(S)

S=A[-22:-10]
print(S)

S=A[:-10]
print(S)


S=A[11]
print(int(S))

S=A[1]
print(S)

S=A[10]
print(float(S))

S="Hello Good Morning"
a=S[1:-1]
print(a)

A=("If you get up in the morning and "
   "think the future is going to be better,"
   " it is a bright day. "
   "Otherwise, it's not.")

V=len(A)
print(V) '''

x,y,z ="Bangalore city", "Bangalore", "Karnataka"
print(z)

x=y=z ="Bangalore city", "Bangalore", "Karnataka"
print(z)

x="Bangalore"
def my_fn():
   x="Karnataka"
   print("good city",x)

my_fn()
print("good city", x)

x="Bangalore"
def my_fnc():
   global x
   x="Karnataka"
   print("good city",x)

my_fnc()
print("good city", x),

def my_fnn():
   X="Hello World!"
   print(type(X))

   X=20
   print(type(X))

   X=20.5
   print(type(X))

   X=1J
   print(type(X))

   X=["Apple","Banana"]
   print(type(X))

   X=("Apple","Banana")
   print(type(X))

   X=range(10,20)
   print(type(X))

   X={"Name": "Nitin","Age":26, "address":"Bangalore"}
   print(type(X))

   X={"Apple","Banana"}
   print(type(X))

   X=frozenset(("Apple","Banana"))
   print(type(X))

my_fnn()

