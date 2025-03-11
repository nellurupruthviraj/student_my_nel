# to find same no of open and close brackets or not
a = input(" enter curly brackets")
print(a)
c= 0
d= 0
for i in a:
    if i == "(":
        c = c+1
    else:
        d = d+1
if c==d:
    print(matching)
else:
    print("not matching")
