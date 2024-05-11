import threading

def Display1():    
    for i in range(1,51):
        print(i)

def Display2():    
    for i in range(50,0,-1):
        print(i)


def main():
   
    thread1=threading.Thread(target=Display1, args=())
    thread2=threading.Thread(target=Display2, args=())
    
    thread1.start()
    thread1.join()

    thread2.start()   
    thread2.join()
    
    print("End of main")
if __name__=="__main__":
    main()
