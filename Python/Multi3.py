
def PrintEven(num): 
    print("Even Numbers:")
    X=2       
    for i in range(num):
        print(X,end=" ")
        X=X+2

def PrintOdd(num):
    print("Odd Numbers:")
    X=1    
    for i in range(num):
        print(X,end=" ")
        X=X+2


 
def main():
    Num=int(input("Enter number"))
    PrintEven(Num)
    print("")
    PrintOdd(Num)


if __name__=="__main__":
    main()