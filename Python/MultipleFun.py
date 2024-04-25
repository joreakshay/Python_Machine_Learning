def Calculation(No1,No2):
    Add=No1+No2
    Sub=No1-No2
    return Add,Sub

A=int(input("Enetr first no:"))
B=int(input("Enetr secont no:"))
Result1, Result2=Calculation(A,B)
print("Addition ",Result1)
print("Sub :",Result2)

