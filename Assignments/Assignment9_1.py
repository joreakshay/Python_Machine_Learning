import os

def main():
    print("Enter the name of file : ")
    Fname = input()

    if os.path.exists(Fname):
        print("File is exist")

    else:
        print("File is not exist")

if __name__ == "__main__":
    main()
