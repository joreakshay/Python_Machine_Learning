def Max(Arr):
    Max=Arr[0]
    for no in Arr:
        if(Max<no):
            Max=no
    return Max

def main():
    Arr=[]
    print("Number Of elements:")
    Cnt=int(input())
    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Arr.append(Num)
    Result=Max(Arr)
    print("Maximum is :",Result)
    
if __name__=="__main__":
    main()