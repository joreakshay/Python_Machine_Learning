def CheckEven(No):
    if(No%2==0):
        print("Even")
    else:
        print("Odd")

def main():
    print("Enter no: ")
    A=int(input())
    CheckEven(A)

main()