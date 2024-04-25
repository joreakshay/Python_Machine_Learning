import Arithmatic

def main():
    Num1=0
    Num2=0
    Result = 0
    print("Enter First Number : ")
    Num1=int(input())
    print("Enter Second Number : ")
    Num2=int(input())
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Mutiplication ")
    print("4. Division ")
    Ch=int(input("Select option"))
    if(Ch==1):
        Result = Arithmatic.Add(Num1,Num2)
    elif(Ch==2):
        Result = Arithmatic.Sub(Num1,Num2)
    elif(Ch==3):
        Result = Arithmatic.Mult(Num1,Num2)
    elif(Ch==4):
        Result = Arithmatic.Div(Num1,Num2)
    
    print("Result is :",Result)

if(__name__=="__main__"):
    main()