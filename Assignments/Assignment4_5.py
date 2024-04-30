from functools import reduce

def CheckPrime(Num):
    for i in range(2,int(Num/2)+1):
        if(Num%i==0):
            return False
    return True

Increase= lambda no:no*2

def Max(a,b):
    if(type(a)== "NoneType" ):
        return b
    if(a<b):
        return b
    else:
        return a

def main():
    Data=[]
    print("Number Of elements:")
    Cnt=int(input())

    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Data.append(Num)

    
    print("Data from input list", Data)

    FData=list(filter(CheckPrime,Data))
    print("Filtered Data:",FData)

    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduce(Max,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()