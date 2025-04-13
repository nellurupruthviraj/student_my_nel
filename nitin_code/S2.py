
def my_fn1(A):
    TS=len(A)
    TM=0
    TF=0

    for i in A:
        s=A[i]
        for i in s:
            if s[i]=="Male":
                TM=TM+1
            elif s[i]=="Female":
                TF=TF+1
    print(f"Total student {TS},\n Total male student {TM},\n Total female student {TF}")


def my_fn2(B):
    for i in B:
        a=B[i]
        for i in a:
            if a[i]=="Rahul":
                print(a)

def my_fn3(C):
    for i in C:
        a=C[i]
        b=a["test_marks"]
        c=b["Math"]
        d=sum(c)
        avg=d/3
        print(f"ALl students Math Average {avg}")

def my_fn4(D):
    for i in D:
        a=D[i]
        b=a["test_marks"]
        c=b["Science"]
        d=sum(c)
        avg=d/3
        print(f"ALl students Science Average {avg}")


def my_fn5(E):
    for i in E:
        a=E[i]
        b=a["test_marks"]
        c=b["English"]
        d=sum(c)
        avg=d/3
        print(f"ALl students English Average {avg}")
