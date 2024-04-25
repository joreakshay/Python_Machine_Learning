def ChkNum(No):
    if(No%2==0):
        return True
    else:
        return False

def main():
    Num=0
    print("Enter Number : ")
    Num=int(input())
    Result = ChkNum(Num)
    if(Result==True):
        print("Even Number")
    else:
        print("Odd Number")

if(__name__=="__main__"):
    main()