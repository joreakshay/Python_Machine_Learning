import threading

def DisplayCountOfSmall(InputString): 
    T=threading.current_thread()
    print("Name Of thread :",T.name)

    print("ID of thread :",threading.get_ident())   
    Cnt=0
    for ch in InputString:
        if(ord(ch)>=97 and ord(ch)<=122):
            Cnt=Cnt+1
    print("Count of Small :",Cnt)

def DisplayCountOfCapital(InputString): 
    T=threading.current_thread()
    print("Name Of thread :",T.name)

    print("ID of thread :",threading.get_ident())   
    Cnt=0
    for ch in InputString:
        if(ord(ch)>=65 and ord(ch)<=90):
            Cnt=Cnt+1
    print("Count of Capital :",Cnt)

def DisplayCountOfDigit(InputString): 
    T=threading.current_thread()
    print("Name Of thread :",T.name)
    print("ID of thread :",threading.get_ident())  
    Cnt=0
    for ch in InputString:
        if(ord(ch)>=48 and ord(ch)<=57):
            Cnt=Cnt+1
    print("Count of Digit :",Cnt)

def main():
    print("Enter String:")
    InputString=input()

    thread1=threading.Thread(target=DisplayCountOfSmall, args=(InputString,))
    thread1.name="Samll"
    thread2=threading.Thread(target=DisplayCountOfCapital, args=(InputString,))
    thread2.name="Capital"
    thread3=threading.Thread(target=DisplayCountOfDigit, args=(InputString,))
    thread3.name="Digits"

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print("End of main")
if __name__=="__main__":
    main()
