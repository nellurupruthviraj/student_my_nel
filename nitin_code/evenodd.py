a=int(input("Enter a number: "))
if a%2==0:
    print("number is even")
else:
    print("number is odd")



'''l=[1,2,3,4,5,6,7,8,9,10]
[print(i,end=' ') for i in l if i>=5]

l=[1,2,3,4,5,6,7,8,9,10]
[print(i) for i in l if i==5]

l=[1,2,3,4,5,6,6,7,8,8,9,10,10]

l1=[]
for i in l:
    if i not in  l1:
        l1.append(i)
        print(l1)


s=lambda a,b: a if a>b else b
s(13,5)

l=["nitin","rahul","sharan","Naveen"]
S=list(filter(lambda i: i=="Naveen", l))
print(S)'''


f=open("abc.txt","w")
f.write("Nitin")
f.read()
f.close()