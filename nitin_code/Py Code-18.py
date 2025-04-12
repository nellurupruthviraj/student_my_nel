a=10
b=10
c=20

if a is c:
    print("a is c True")
elif a is b:
    print("A  is b True")
else:
    print("c is a True")


## for loop program

S= "Bangalore"
print(type(S))

A= [1,2,3,4,5,6,6]
print(type(A))

B=int(1)
print(type(B))

C=(1,2,3,4,5,6,667)
print(type(C))

Z=("Bangalore")
print(len(Z))

N="Hello World"
print(N.upper())

M= "Hello World \n good Morning \n have a nice day"
print(len(M))
print(type(M))
print(M.upper())
print(M.lower())

Q=["Aplle", "Banana", "Grapes", "Mango"]
W=("Orange", "papay")
Q.append(W)
print(Q)

i=["Apple", "Banana", "Grapes", "Mango"]

if "Apple" in i:
    print("Yes, Apple is present")

i = ["Apple", "Banana", "Grapes"]
if "Mango" not in i:
    print("yes, Mango is not present")
if "Mango" in i:
    print("Yes mango is present")