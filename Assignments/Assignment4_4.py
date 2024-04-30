from functools import reduce

EvenCheck = lambda no:(no%2==0)

Increase= lambda no:no*no

Add= lambda a,b: a+b

def main():
    Data=[]
    print("Number Of elements:")
    Cnt=int(input())

    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Data.append(Num)

    
    print("Data from input list", Data)

    FData=list(filter(EvenCheck,Data))
    print("Filtered Data:",FData)

    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduce(Add,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()