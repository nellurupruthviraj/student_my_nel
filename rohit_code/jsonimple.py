import json
from rohit_code.workingjson import *
with open('student.json', 'r') as file:
    data = json.load(file)
print("what do you want")
b = input("enter 1 for how many males and females \n enter 2 to know avg maarks of subject \n enter 3 for student details")
c = 0
e = 0
if b=="2":
    c = input("which subject do you want")
if b == "3":
    e = input("enter the student name")
ad(b,data,c,e)

