#a = int(input(""))
def arm():
    a = int(input(""))
    ac = a
    c = len(str(a))
    b = 0
    d = 0
    while a>0:
        b = a%10
        d = b**c + d
        a = a//10
    if d == ac:
        print("armstrong number")
    else:
        print("not an armsttrong number")
arm()
