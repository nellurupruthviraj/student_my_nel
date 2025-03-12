#a = list(map(str,input("").split()))
a = str(input("enter"))
b = []
dd = 0
for i in a:
    if i not in b:
        b.append(i)
for j in b:
    for k in a:
        if j == k :
            dd = dd + 1
    print(f"{j} {dd}", end =" ")
    dd = 0