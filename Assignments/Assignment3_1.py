def ListAddion(Arr):
    Sum=0
    for no in Arr:
        Sum=Sum+no
    return Sum

def main():
    Arr=[]
    print("Number Of elements:")
    Cnt=int(input())
    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Arr.append(Num)
    Result=ListAddion(Arr)
    print("Addition of list is :",Result)
    
if __name__=="__main__":
    main()