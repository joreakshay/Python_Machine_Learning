import os

def main():
    print("PID of running process :",os.getpid())
    print("PID of running process :",os.getppid()) 
if __name__=="__main__":
    main()