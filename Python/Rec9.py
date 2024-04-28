Fact =1
def Factorial(No):
    global Fact
    if(No>=1):
        Fact=Fact*No
        No=No-1
        Factorial(No)
    return Fact

def main():
    print("Enter no:")
    Num=int(input())
    result = Factorial(Num)
    print("Fact=",result)

if(__name__=="__main__"):
    main()