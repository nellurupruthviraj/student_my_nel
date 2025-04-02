a = ["ram","pat","abhi","head","sant"]
b = [1,5,3,8,9]
c = 0
d = {}
for i in a:
    d[i] = b[c]
    c = c+1
print(d)
for i in d:
    print(f"{i} {d[i]}")
for i in range(len(a)):
    print(f"{a[i]}  {b[i]}")