####
a=int(input("enter a number: "))
if a% 2 == 0:
    print("num is  even")
else:
    print("odd")


####
s = input("enter a number: ")
if s == s[::-1]:
    print("it is a palindrome")
else:
    print("its not a palindrome")


####
start=int(input("enter start of range: "))

end = int(input("enter end of range: "))

P=[i for i in range(start,end+1) if str(i)==str(i)[::-1]]
print(P)



####
def is_prime(n):
    if n<=1:
        return false
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

num=int(input("inter a number: "))
print(is_prime(num))

