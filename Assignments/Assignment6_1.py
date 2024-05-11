import threading

def DisplayEven(No):
    print("Even numbers are :")
    for i in range(2,No+1,2):
        print(i)

def DisplayOdd(No):
    print("Even odd are :")
    for i in range(1,No,2):
        print(i)

def main():
    print("Enter number :")
    Num=int(input())
    thread1=threading.Thread(target=DisplayEven, args=(Num,))
    thread2=threading.Thread(target=DisplayOdd, args=(Num,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__=="__main__":
    main()
