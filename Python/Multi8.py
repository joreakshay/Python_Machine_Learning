import threading

def PrintEven(num): 
    print("Even Numbers:")
    X=2       
    for i in range(num):
        print("Even :",X)
        X=X+2

def PrintOdd(num):
    print("Odd Numbers:")
    X=1    
    for i in range(num):
        print("Odd :",X)
        X=X+2
 
def main():
    Value=int(input("Enter number :"))
    p1=threading.Thread(target=PrintEven, args=(Value,))
    p2=threading.Thread(target=PrintOdd, args=(Value,))
   
    p1.start()
    p2.start()
        
    p1.join()
    p2.join()
    print("End of main")
   
if __name__=="__main__":
    main()