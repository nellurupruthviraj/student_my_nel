
a = str(input("enter"))
b = []
dd = 0
for i in a:
    for j in a:
        if i == j:
            dd = dd + 1
    if i not in b:
        b.append(i)

    dd = 0