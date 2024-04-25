def Calculation(No1,No2):
    def Addition(X,Y):
        return X+Y
    def Substraction(X,Y):
        return X-Y
    ans1=Addition(No1,No2)
    ans2=Substraction(No1,No2)
    return ans1,ans2

A=int(input("Enetr first no:"))
B=int(input("Enetr secont no:"))
Result1, Result2=Calculation(A,B)
print("Addition ",Result1)
print("Sub :",Result2)

