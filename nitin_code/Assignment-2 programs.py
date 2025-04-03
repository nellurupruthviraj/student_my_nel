S="Hello world welcome my name is Nitin"
a=S.split(" ")
for i in a:
    b=i[::-1]
    print(b, end=" ")

#### Second Question

S = "Hello world welcome my name is Nitin"
a=S.split(" ")
b=" ".join(reversed(a))
print(b)