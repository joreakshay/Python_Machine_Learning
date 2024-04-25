
def Factorial(Num):
    fact=1
    for i in range(1,Num+1):
        fact=fact*i
    return fact

def main():
    print("Enter No:")
    No=int(input())
    Result=Factorial(No)
    print("Factorial is:", Result)
    

if(__name__=="__main__"):
    main()