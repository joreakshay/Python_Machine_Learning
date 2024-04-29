def CheckFrequency(Arr,Num):
    Freq=0
    for no in Arr:
        if(Num==no):
            Freq=Freq+1
    return Freq

def main():
    Arr=[]
    print("Number Of elements:")
    Cnt=int(input())
    print("Enter Numbers: ")
    for i in range(Cnt):
        Num=int(input())
        Arr.append(Num)
    print("Enter number to check frequency :")
    Num=int(input())
    Result=CheckFrequency(Arr,Num)
    print("Frequency is :",Result)
    
if __name__=="__main__":
    main()