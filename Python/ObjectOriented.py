print("Demonstration of Object orientetion")

class Arithematic:
    def __init__(self,Value1,Value2):
        self.No1=Value1
        self.No2=Value2

    def Addition(self):
        return self.No1+self.No2

    def Substraction(self):
        return self.No1-self.No2


print("Enter first number")
No1=int(input())

print("Enter Second number")
No2=int(input())

obj=Arithematic(No1,No2)
Ans= obj.Addition()

print("Addition is :", Ans)

Ans= obj.Substraction()

print("Substraction is :", Ans)