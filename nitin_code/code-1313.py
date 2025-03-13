'''
l=[1,2,4,5,6,7]

for s in l:
    print(s)

A=[10,20,30,40,50,60,70]

for i in A:
    print(i)


K =("Nitin RK")

for i in K:
    print(K)
    print(i)


Z=("Bangalore")

for i in Z:
    print(i[-1])

z=("Bangalore")

for i in z:
    if i=="o":
        pass
    print(i)

c=("Bangalore")

for i in c:
    if i == "g":
        break
    print(i)


b=("Bangalore")

for i in b:
    if i == "l":
        continue
    print(i)


# break statement
b=("Bangalore")

for i in b:
    if i == "n":
        break
    print(i)


#continue statement
b=("Bangalore")

for i in b:
    if i == "g":
        continue
    print(i)


# pass statement
b=("Bangalore")

for i in b:
    if i == "B":
        pass
    print(i) '''


G=("Bangalore City")

print(G[2:4])
print(G[:6])
print(G[-9])

G=("Bangalore City")

for i in G:
    if i == "C":
        print("C is present")


G=("Bangalore City")

for i in G:
    if i == "y":
        print(i)