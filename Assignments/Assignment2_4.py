
def AddOfFact(Num):
    fact=0
    for i in range(1,int(Num/2)+1):
        if(Num%i==0):
            fact=fact+i
    return fact

def main():
    print("Enter No:")
    No=int(input())
    Result=AddOfFact(No)
    print("Addition of factors is:", Result)
    

if(__name__=="__main__"):
    main()