import os

def main():
    FileName1=input("Enter first file name:")
    FileName2=input("Enter second file name:")
    Data1=""
    Data2=""
    if os.path.exists(FileName1):
        fobj = open(FileName1, "r")
        Data1 = fobj.read() 
        fobj.close()        
    else:
        print("Unable to open file as file is not present in the current directory")


    if os.path.exists(FileName2):
        fobj = open(FileName2, "r")
        Data2 = fobj.read() 
        fobj.close()        
    else:
        print("Unable to open file as file is not present in the current directory")

    if(Data1==Data2):
        print("File contains are same")
    else:
        print("File contains are not same")


if __name__ == "__main__":
    main()
