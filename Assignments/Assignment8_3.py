class Numbers:    
    def __init__(self,value):
        self.Value=value

    def ChkPrime(self):
        if(self.Value==0 or self.Value==1):
            return True
        for i in range(2,int(self.Value/2)+1):
            if(self.Value%i==0):
                return False
        return True

    def ChkPerfect(self):
        Sum=self.SumFactor()
        if(Sum==self.Value):
            return True
        else:
            return False

    def SumFactor(self):
        Sum=0
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i==0):
                Sum=Sum+i
        return Sum

    def Factor(self):
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i==0):
                print(i)

def main():

    Num=int(input("Enter number :"))
    Obj1=Numbers(Num)
    if(Obj1.ChkPrime()):
        print("Number is prime")
    else:
        print("Number is not prime")

    if(Obj1.ChkPerfect()):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    print("Sum of Factors :",Obj1.SumFactor())
    Obj1.Factor()

if __name__=="__main__":
    main()
