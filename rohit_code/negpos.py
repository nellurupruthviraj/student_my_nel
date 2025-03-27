a = [-1,1,2,-3,5]
pos = []
neg = []
for i in a:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
e = []
p = 0
n = 0
while p<len(pos) or n <len(neg):
    if p <len(pos):
        e.append(pos[p])
        p+=1
    if n <len(neg):
        e.append(neg[n])
        n+=1
print(e)
"""
for i in range(g):
    e.append(b[i])
    while len(c)>0:
        e.append(c[i])
        c.remove(c[i])
print(e)
"""





