
def main():
    Num=0
    print("Enter Number : ")
    Num=int(input())
    if(Num==0):
        print("Zero")
    elif(Num<0):
        print("Negative Number")
    else:
        print("Positive Number")

if(__name__=="__main__"):
    main()