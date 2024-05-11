class Arithmetic:
    PI=3.14
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        print("Enter Value 1 :")
        self.Value1=int(input())
        print("Enter Value 2 :")
        self.Value2=int(input())

    def Addition(self):
        return self.Value1+self.Value2
    
    def Subtraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1*self.Value2

    def Division(self):
        return self.Value1/self.Value2

def main():
    Obj=Arithmetic()
    Obj.Accept()
    print("Addtion is :",Obj.Addition())
    print("Subtraction is :",Obj.Subtraction())
    print("Multiplication is :",Obj.Multiplication())
    print("Division is :",Obj.Division())
    
    

if __name__=="__main__":
    main()
