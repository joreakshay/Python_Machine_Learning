from functools import reduce

def main():

    Data =[11,14,20,23,18,16,15,20]    
    print("Data from input list", Data)

    FData=list(filter(lambda no:(no%2==0),Data))
    print("Filtered Data:",FData)

    MData=list(map(lambda no:no+1,FData))
    print("Mapped Data:",MData)

    RData=reduce(lambda a,b: a+b,MData)
    print("Data after reduce actibity is :",RData)
    


if __name__=="__main__":
    main()