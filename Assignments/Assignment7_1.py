class Demo:
    Value=10
    def __init__(self,num1,num2):
        self.no1=num1
        self.no2=num2

    def Fun(self):
        print("First number is :",self.no1)
        print("Second number is :",self.no2)

    def Gun(self):
        print("First number is :",self.no1)
        print("Second number is :",self.no2)


def main():
    Obj1=Demo(11,21)
    Obj2=Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()
    

if __name__=="__main__":
    main()
