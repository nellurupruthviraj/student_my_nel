stud=["Nitin","Sharan","Rahul","Suresh"]
[print(i) for i in stud if i=="Rahul"]


stud=["Nitin","Sharan","Rahul","Suresh"]
[print(i) for i in stud  if i!="Sharan"]

stud=["Nitin","Sharan","Rahul","Suresh"]
[print(i) for i in stud if i == "Nitin"]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
[print(i) for i in A if i!=50]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
[print(i) for i in A if i>=50]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
[print(i) for i in A if i<=50 ]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
[print("Grater",i,end=" ") for i in A if i>=60]

A=[10,20,30,40,50,50,60,60,70,80,90,100]
[i**2 for i in A]

A=[1,2,3,4,5,6,6,7,7,8,9,10]
[print(x*2,end=" ") for x in A if x%2==0]

A=[1,2,3,4,5,6,6,7,7,8,9,10]
[print(x-5,end=' ') for x in A ]

A=[1,2,3,4,5,6,6,7,7,8,9,10]
[print(x-2,end=' ') for x in A if x%2==0]




