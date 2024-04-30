
def Factorial(No):
    if(No<1):        
        return 1    
    return (No*Factorial(No-1))   
   

def main():
    print("Enter no:")
    Num=int(input())
    Result=Factorial(Num)    
    print("Factorial of number:",Result)
    
if(__name__=="__main__"):
    main()