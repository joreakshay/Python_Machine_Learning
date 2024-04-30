from functools import reduce

CheckRange = lambda no:(no>=70 and no<=90)

Increase= lambda no:no+10

Mult= lambda a,b: a*b

def main():
    Data=[]
    print("Number Of elements:")
    Cnt=int(input())

    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Data.append(Num)

    
    print("Data from input list", Data)

    FData=list(filter(CheckRange,Data))
    print("Filtered Data:",FData)

    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduce(Mult,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()