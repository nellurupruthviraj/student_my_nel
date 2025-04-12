def ad(a,data,b =0):
    if a == "1":
        o = ge()
        o.gen(data)
    elif a == "2":
        o= subject()
        o.maths(data,b)
    elif a =="4":
        pass
    else:
        return "enter the correct number"

class cell:
    def fin(self,data):
        dat = dict(data)
        for i,j in dat.items():
            h = list(j)
            return h
class ge(cell):
    #gen(h)
    def gen(self,o):
        c= super().fin(o)
        a = 0
        b = 0
        for i in c:
            if  i["gender"] == "female":
                a = a+1
            elif i["gender"] == "male":
                b = b+1
            else:
                pass
        print(f"count of male {b},count of female {a}")
class age(cell):
    #age(h)
    def age(self,o):
        c= super().fin(o)
        a  = 0
        b = 0
        for i in c:
            if i["age"] < 23:
                a = a+1
            elif i["age"] < 30:
                b = b+1
        print(f"age less than 23 {a} age greater than 23 {b} ")
class subject(cell):
    def maths(self,o,aa):
        c = super().fin(o)
        #print(c)
        for i in c:
            bb = i["name"]

            a = i[aa]
            #print(a)
            ab = a["name"]
            b = a["marks"]
            sum = 0
            kk = 0
            for i in b:
                sum = sum + i
            kk = sum // 3
            print(f"{bb}'s avg marks in {ab} is {kk} ")

