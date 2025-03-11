a = list(map(str,input("").split()))
for i in a:
    s = a.count(i)
    print(f"{i} {s}", end =" ")