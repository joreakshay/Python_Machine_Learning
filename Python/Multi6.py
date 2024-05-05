import multiprocessing
import os
import threading

def PrintEven(num): 
    print("PID of even process:", os.getpid())
    print("Even Numbers:")
    X=2       
    for i in range(num):
        print(X)
        X=X+2

def PrintOdd(num):
    print("PID of odd process:", os.getpid())
    print("Odd Numbers:")
    X=1    
    for i in range(num):
        print(X)
        X=X+2


 
def main():
    print("PID of Main process:", os.getpid())
    Value=int(input("Enter number :"))
    p1=multiprocessing.Process(target=PrintEven, args=(Value,))
    p2=multiprocessing.Process(target=PrintOdd, args=(Value,))
   
    p1.start()    
    p1.join()

    p2.start()
    p2.join()
    print("End of main")
   
if __name__=="__main__":
    main()