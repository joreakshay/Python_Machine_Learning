import sys

def main():
    print("Demonstration of command line arguments")
    print("Name of applictaion : ", sys.argv[0])
    print("data type of argv is :", type(sys.argv))
    print("Number of arguments are :", len(sys.argv))
if __name__=="__main__":
    main()