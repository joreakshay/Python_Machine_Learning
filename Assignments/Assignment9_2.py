import os

def main():
    print("Enter the name of file : ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        Data = fobj.read()        
        print(Data)

        fobj.close()
    else:
        print("Unable to open file as file is not present in the current directory")


if __name__ == "__main__":
    main()
