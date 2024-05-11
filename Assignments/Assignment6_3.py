import threading

def DisplayEvenAdd(Numbers):   
    Sum=0
    for i in Numbers:
        if(i%2==0):
            Sum=Sum+i
    print("Addition of even :",Sum)

def DisplayOddAdd(Numbers):   
    Sum=0
    for i in Numbers:
        if(i%2!=0):
            Sum=Sum+i
    print("Addition of Odd :",Sum)

def main():
    print("Enter number count:")
    Cnt=int(input())
    NumList=[]
    print("Enter numbers:")
    for i in range(Cnt):
        NumList.append(int(input()))
    thread1=threading.Thread(target=DisplayEvenAdd, args=(NumList,))
    thread2=threading.Thread(target=DisplayOddAdd, args=(NumList,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("End of main")
if __name__=="__main__":
    main()
