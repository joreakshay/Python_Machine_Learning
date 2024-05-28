import os
import sys

def main():
    if os.path.exists(sys.argv[1]):
        fobj = open(sys.argv[1], "r")
        Data = fobj.read() 
        fobj.close()

        fobj=open("Demo.txt","w")
        fobj.write(Data)
        fobj.close()
        print("File copied..")
    else:
        print("Unable to open file as file is not present in the current directory")


if __name__ == "__main__":
    main()
