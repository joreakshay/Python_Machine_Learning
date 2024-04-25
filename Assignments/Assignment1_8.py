def PrintStar(Num):
    for i in range(Num):
        print("*",end = " ")

def main():
    Num=0
    print("Enter Number : ")
    Num=int(input())
    PrintStar(Num)

if(__name__=="__main__"):
    main()