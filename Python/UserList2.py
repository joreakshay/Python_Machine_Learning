def Addition(Data):
    Sum=0
    for no in Data:
        Sum=Sum+no

    return Sum

def main():
    print("How many numbers you want enter ")
    Cnt=int(input())
    #Arr=[]
    Arr=list()
    print("Enter numbers :")
    for i in range(Cnt):
        Arr.append(int(input()))
    #Display(Arr)
    print("Addition is :",Addition(Arr))

if(__name__=="__main__"):
    main()