a ="sssdddfff"
#from collections import Counter
c = {}
def cou(b,d):
    #c = dict(Counter(a))
    c = {i:a.count(i) for i in a}
    print(c)

    for s in c.values():
        if s % 2 != 0:
            d = d + 1
    if d < 2:
        print("yes")
    else:
        print("no")
cou(0,0)



