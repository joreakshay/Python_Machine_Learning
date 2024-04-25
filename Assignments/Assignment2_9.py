def NumbersInDigit(Num):
    Cnt=1
    while(Num>10):
        Cnt=Cnt+1
        Num=int(Num/10)
    return Cnt

def main():
    print("Enter No:")
    No=int(input())
    Result=NumbersInDigit(No)
    print("Number of digits", Result)

if(__name__=="__main__"):
    main()