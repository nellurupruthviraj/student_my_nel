import json
from nitin_code.WorkingJson import *
with open('stud_Details.json',"r") as file:
    STUD=json.load(file)
#print(STUD)
my_fn(STUD)

my_fn2(STUD)

my_fn3(STUD)
