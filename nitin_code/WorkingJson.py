

def my_fn(Data):
    TS=len(Data)
    TM=0
    TF=0

    for i in Data:
        A=Data[i]
        for s in A:
            if A[s]=="Male":
                TM=TM+1
            elif A[s]=="Female":
                 TF=TF+1

    print(f"Total student: {TS},\n Total male student: {TM},\n Total female student: {TF},")



def my_fn2(Data):
    for i in Data:
        A = Data[i]
        for s in A:
            if A[s]=="Suresh":
                print(A)


def my_fn3(Data):

    for i in Data:
        A=Data[i]
        C=A["test_marks"]
        D=C["Math"]
        Add=sum(D)
        Avg=Add/3
        print(Avg)











