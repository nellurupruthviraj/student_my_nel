
#### 1)find number even or odd
a=int(input("Enter a number: "))
if a%2==0:
    print("number is even")
else:
    print("number is odd")

a=int(input("enter a number: "))
if a%2==1:
    print("number is odd")
else:
    print("number is even")


#### 2) check if a number is palindrime or not
S = input("enter a number: ")
if S == S[::-1]:
    print("It is palindrome")
else :
    print("No Palindrome")


s=input("enter a number: ")
if s == s[::-1]:
    print("YES it is palindrome")
else :
    print("No palindrome")

#### 3) check a number is prime or not
def my_fun(s):
    if s<=1:
        print("return False")
    for i in range(2,s):
        if s % i ==0:
            print("return False")
    print("return True")
num = int(input("enter a number: "))
print(my_fun(num))


#### 4) check a given number positive or negative:
a=int(input("enter a number: "))
if a>0:
    print("Positive Number")
elif a<0:
    print("Negative Number")
else:
    print("Number is Zero")

a=int(input("Enter a number: "))
if a>0:
    print("Positive number")
elif a<0:
    print("Negative number")
else:
    print("Number is zero")



#### 5) sum of frist N Natural number

n= int(input("enter a number: "))
sum = n *(n+1)//2
print(sum)

a=int(input("enter a number: "))
s=a*(a+1)//2
print(s)


#### 6) find Sum Of AP series
def sum_off(a,b,c):
    print(c/2 *(2*a +(c-1)*b))
a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
c=int(input("enter a number3: "))

print(sum_off(a,b,c))


#### 7) gratest of two numbers

A=int(input("enter a numberA: "))
B=int(input("enter a numberB: "))

if A>B:
    print("A is Grater")
elif B>A:
    print("B is Grater")
else:
    print("Both are equal")


#### 8) Gratest of Three numbers

A=int(input("enter a numberA: "))
B=int(input("enter a numberB: "))
C=int(input("enter a numberC: "))

if A>B:
    print("A is Grater")
elif A>C:
    print("A is grater")
elif B>A:
    print("B is Grater")
elif B>C:
    print("B is Grater")
elif C>A:
    print("C is Grater")
elif C>B:
    print("C is Grater")
else:
    print("All are equal")


A=int(input("enter a numberA: "))
B=int(input("enter a numberB: "))
C=int(input("enter a numberC: "))

print(max(A,B,C))


#### 9) Leap year or not
year= int(input("Enter a year: "))

if year%4==0 and (year %100 !=0 or year % 400 == 0):
    print(year, "is leap year")
else:
    print(year, "is not a leap year")


#### 10) reverses digits of a number
num = int(input("Enter a number: "))

A=int(str(num)[::-1])
print(A)

l=(10,20,30,40,50,60,70,80)
a=l[::-1]
print(a)


#### 11) maximum and minimum digit in a number
A=int(input("enter a value: "))
digits = [int(d) for d in str (A)]
print("maximum digits: ", max(digits))
print("Minimum digits: ", min(digits))


#### 12) print Fibonacci upto Nth Term
n= int(input("enter the number of terms: "))
a,b = 0, 1
for i in range(n):
    print(a,end=" ")
    a, b=b, a+b


#### 13) Factorial of a number

num = int(input("enter a number: "))
factorial =1
for i in range(1, num + 1):
    factorial *=i
print(factorial)