from selenium import webdriver

def asd(a):
    #print(a)
    c = 0
    d =0
    for i in a:
        b = a[i]
        #print(b)
        for j in b:
            #print(j)
            if b[j] == "Suresh":
                print(b)
            elif b[j] =="Male":
                c = c+1
            elif b[j] == "Female":
                d =d +1
    print(c,d)
def asf(a):
    #print(a)
    c = 0
    d =0
    e = 0
    f = 0
    for i in a:
        b = a[i]
        c = b['test_marks']
        d = c['Math']
        e = sum(d)
        f = 0
        f = e/3
        #return f


class StudentData:
    def __init__(self, data):
        self.data = data

class StudentStatistics(StudentData):
    def my_fn1(self):
        TS = len(self.data)
        TM = 0
        TF = 0

        for i in self.data:
            s = self.data[i]
            for i in s:
                if s[i] == "Male":
                    TM = TM + 1
                elif s[i] == "Female":
                    TF = TF + 1
        print(f"Total student {TS},\n Total male student {TM},\n Total female student {TF}")

class StudentSearch(StudentData):
    def my_fn2(self):
        for i in self.data:
            a = self.data[i]
            for i in a:
                if a[i] == "Rahul":
                    print(a)

class StudentMathMarks(StudentData):
    def my_fn3(self):
        for i in self.data:
            a = self.data[i]
            b = a["test_marks"]
            c = b["Math"]
            d = sum(c)
            avg = d / 3
            print(f"ALl students Math Average {avg}")

class StudentScienceMarks(StudentData):
    def my_fn4(self):
        for i in self.data:
            a = self.data[i]
            b = a["test_marks"]
            c = b["Science"]
            d = sum(c)
            avg = d / 3
            print(f"ALl students Science Average {avg}")

class StudentEnglishMarks(StudentData):
    def my_fn5(self):
        for i in self.data:
            a = self.data[i]
            b = a["test_marks"]
            c = b["English"]
            d = sum(c)
            avg = d / 3
            print(f"ALl students English Average {avg}")

