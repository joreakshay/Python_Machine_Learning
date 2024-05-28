import os
import sys

def main():
    FileName=input("Enter file Name : ")
    SubStr=input("Enter substring :")
    if os.path.exists(FileName):
        fobj = open(FileName, "r")
        Data = fobj.read() 
        fobj.close()
        cnt=Data.count(SubStr)
        print("Substring count is :",cnt)
    else:
        print("Unable to open file as file is not present in the current directory")


if __name__ == "__main__":
    main()
