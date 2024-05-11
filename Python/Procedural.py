print("Demonstration of Procedural")

def Addition(No1,No2):
    return No1+No2

def Substraction(No1,No2):
    return No1-No2

def main():
    print("Enter first number")
    No1=int(input())

    print("Enter Second number")
    No2=int(input())

    Ans= Addition(No1,No2)

    print("Addition is :", Ans)

    Ans= Substraction(No1,No2)

    print("Substraction is :", Ans)

if __name__=="__main__":
    main()