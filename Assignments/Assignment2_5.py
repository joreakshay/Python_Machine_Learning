
def IsPrime(Num):
    for i in range(2,int(Num/2)+1):
        if(Num%i==0):
            return False
    return True

def main():
    print("Enter No:")
    No=int(input())
    Result=IsPrime(No)
    if(Result==True):
        print("Number is prime")
    else:
        print("Number is not prime")
    

if(__name__=="__main__"):
    main()