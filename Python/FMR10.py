from MarvellousFMR import *
EvenCheck = lambda no:(no%2==0)

Increase= lambda no:no+1

Add= lambda a,b: a+b

def main():

    print("Enter number of element:")
    i=0
    Cnt=int(input())
    Data =[] 
    print("Enter numbers:")
    for i in range(Cnt):
        Data.append(int(input()))

    #Data =[11,14,20,23,18,16,15,20]    
    print("Data from input list", Data)

    FData=list(filterX(EvenCheck,Data))
    print("Filtered Data:",FData)

    MData=list(mapX(Increase,FData))
    print("Mapped Data:",MData)

    RData=reduceX(Add,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()