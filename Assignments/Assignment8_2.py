class BankAccount:
    ROI=10.5
    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    def Display(self):
        print("Name :{0} Amount :{1}.".format(self.Name,self.Amount))

    def Deposit(self, Amt):
        self.Amount=self.Amount+Amt

    def Withdraw(self,Amt):
        self.Amount=self.Amount-Amt
    
    def CalculateIntrest(self):
        return(self.Amount*(BankAccount.ROI/100))


def main():
    Obj1=BankAccount("User1",10000)
    Obj1.Display()
    Obj1.Deposit(2000)
    Obj1.Display()
    Obj1.Withdraw(3000)
    Obj1.Display()
    print("Intrest :",Obj1.CalculateIntrest())

if __name__=="__main__":
    main()
