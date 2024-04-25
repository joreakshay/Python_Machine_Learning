def Display(Arr):
    print("Numners :")
    for i in range(len(Arr)):
        print(Arr[i])

def main():
    print("How many numbers you want enter ")
    Cnt=int(input())
    #Arr=[]
    Arr=list()
    print("Enter numbers :")
    for i in range(Cnt):
        Arr.append(int(input()))
    #Display(Arr)
    print("Entered element",Arr)

if(__name__=="__main__"):
    main()