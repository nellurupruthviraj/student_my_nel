import json
from rohit_code.workingjson import *
with open('student.json', 'r') as file:
    data = json.load(file)
print("what do you want")
b = input("enter 1 for how many males and females \n enter 2 to know avg maarks of subject ")
c = 0
if b=="2":
    c = input("which subject do you want")
ad(b,data,c)