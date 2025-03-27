a = (1,2,3,4,5,6,7,8,9)
ae = []
asd = []
ij = 0
def tupl(a,b,):
    print("(",end ="")
    ar = tuple((a,b))
    print (ar,end = "")
for i in a:
    n = 17
    if i < n/2:
        n = n-i
        if i != n:
            if n not in asd:
                if n in a:
                    aq = a.index(i)
                    aw = a.index(n)
                    tupl(aq,i)
                    tupl(aw,n)
                    print(") , ",end ="")
        asd.append(n)



