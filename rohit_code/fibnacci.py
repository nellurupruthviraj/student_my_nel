a = int (input("where to end the series"))
def fib():
    z = 0
    c = 1
    print(z,end = " ")
    b =1
    while b < a:
        bb = b
        print(b,end = " ")
        b = b + c
        c = bb


fib()
