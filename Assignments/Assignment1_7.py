def IsDivisibleByFive(No):
    if(No%5==0):
        return True
    else:
        return False

def main():
    Num=0
    print("Enter Number : ")
    Num=int(input())
    Result = IsDivisibleByFive(Num)
    print(Result)

if(__name__=="__main__"):
    main()