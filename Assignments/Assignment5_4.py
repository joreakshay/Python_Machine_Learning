
def SumOfDigits(No):
    Mod=No%10
    No=int(No/10)
    if(No==0):        
        return Mod
    return (Mod+SumOfDigits(No))   
   

def main():
    print("Enter no:")
    Num=int(input())
    Result=SumOfDigits(Num)    
    print("Sum of digits :",Result)
    
if(__name__=="__main__"):
    main()