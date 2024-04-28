
EvenCheck = lambda no:(no%2==0)

Increase= lambda no:no+1

Add= lambda a,b: a+b

def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    return Result

def reduceX(Task,Elements):
    Result=0
    for no in Elements:
        Result=Task(Result,no)
    return Result

def main():

    Data =[11,14,20,23,18,16,15,20]    
    print("Data from input list", Data)

    FData=list(filterX(EvenCheck,Data))
    print("Filtered Data:",FData)

    MData=list(mapX(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduceX(Add,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()