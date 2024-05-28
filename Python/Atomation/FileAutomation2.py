import sys

def Addition(A,B):
    return A+B

def main():
    print("-----------------------------------------------------")
    print("----------Automation to perform addition-------------")
    print("-----------------------------------------------------")
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H" ):
            print("This script is used to perform addition of 2 integral values")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use of script :")
            print("Name_of_file first_Argument Second_Argument")
            print("Note :  Both the argument should be in the integral format")
            exit()
        else:
            print("Invalid option")
            print("Use --h option to get the help  and --u option to get the usage of application")

    if(len(sys.argv)==3):
        try:
            ret= Addition(int(sys.argv[1]),int(sys.argv[2]))
            print("Addition is :", ret)

        except ValueError as obj1:
            print("Invalid type of arguments")
        
        except Exception as obj2:
            print("Unable to perform opration due to ", obj2)

    else:
        print("Invalid option")
        print("Use --h option to get the help  and --u option to get the usage of application")

    print("-----------------------------------------------------")
    print("----------Thank you for using our script-------------")
    print("------------------Akshay Jore------------------------")
    print("-----------------------------------------------------")
    
if __name__ =="__main__":
    main()