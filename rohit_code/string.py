stri="Hello name is rohit"
ap = list(map(str,stri.split(" ")))
def ste(a):
    for i in a:
        b = i[::-1]
        print(b ,end = " ")
ste(ap)
