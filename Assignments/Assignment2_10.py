def AddDigits(Num):
    Sum=0
    while(Num>10):
        Mod=Num%10
        Sum=+Sum+Mod
        Num=int(Num/10)
    Sum=Sum+Num
    return Sum

def main():
    print("Enter No:")
    No=int(input())
    Result=AddDigits(No)
    print("Addition of digits", Result)

if(__name__=="__main__"):
    main()