a = list(map(int,input("enter with spaces list1").split()))
b = list(map(int,input("enter with spaces list2").split()))
c = list(map(int,input("enter with spaces list3").split()))
for i in b:
    if i in a and i in c:
        print(i)

