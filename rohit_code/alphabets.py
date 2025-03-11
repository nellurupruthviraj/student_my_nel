a = list(map(str,input("").split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
for j in b:
    s = a.count(j)
    print(f"{j} {s}", end =" ")