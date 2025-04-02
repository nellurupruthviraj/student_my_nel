def my_fun(s):
    if s<=1:
        return "False"
    for i in range(2,s):
        if s % i ==0:
            return "false"
    return "true"
num = int(input("enter a number: "))
print(my_fun(num))


