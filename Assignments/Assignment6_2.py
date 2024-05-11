import threading

def DisplayEvenFactAdd(No):   
    Sum=0
    for i in range(1,No+1):
        if(No%i==0 and i%2==0):
            Sum=Sum+i
    print("Addition of even factor :",Sum)

def DisplayOddFactAdd(No):   
    Sum=0
    for i in range(1,No+1):
        if(No%i==0 and i%2!=0):
            Sum=Sum+i
    print("Addition of Odd factor :",Sum)

def main():
    print("Enter number :")
    Num=int(input())
    thread1=threading.Thread(target=DisplayEvenFactAdd, args=(Num,))
    thread2=threading.Thread(target=DisplayOddFactAdd, args=(Num,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Exit from main")
if __name__=="__main__":
    main()
