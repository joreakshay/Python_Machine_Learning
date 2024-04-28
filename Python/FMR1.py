from functools import reduce

def EvenCheck(no):
    return (no%2==0)

def Increase(no):
    return no+1

def Add(a,b):
    return a+b

def main():

    Data =[11,14,20,23,18,16,15,20]    
    print("Data from input list", Data)

    FData=list(filter(EvenCheck,Data))
    print("Filtered Data:",FData)

    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduce(Add,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()