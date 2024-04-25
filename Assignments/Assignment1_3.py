def Add(No1,No2):
    Ans=No1+No2
    return Ans

def main():
    Num1=0
    Num2=0
    print("Enter First Number : ")
    Num1=int(input())
    print("Enter Second Number : ")
    Num2=int(input())
    Result = Add(Num1,Num2)
    print("Addition is :",Result)

if(__name__=="__main__"):
    main()