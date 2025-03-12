a = input("")
b = []
for i in a:
    if i not in b:
        b.append(i)
if len(a) == len(b):
    print(" no repeating string false")
else:
    print(" Repeating string true")

