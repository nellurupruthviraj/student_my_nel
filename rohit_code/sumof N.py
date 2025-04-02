a = int(input("enter a number"))
def sumofn():
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    print(f"sum of first n natural numbers {sum}")
sumofn()