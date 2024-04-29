import MarvellousNum

def ListPrime(Arr):
    PrimeArr=[]
    for no in Arr:
        if(MarvellousNum.CheckPrime(no)):
            PrimeArr.append(no)
    return PrimeArr

def main():
    Arr=[]
    print("Number Of elements:")
    Cnt=int(input())
    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Arr.append(Num)
    PrimeArr=ListPrime(Arr)
    print(PrimeArr)
    Result=MarvellousNum.ListAddion(PrimeArr)
    print("Addion of prime is :",Result)
    
if __name__=="__main__":
    main()