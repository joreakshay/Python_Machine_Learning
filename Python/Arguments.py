# Types of argument
# 1 : Positional argument
# 2 : Keyword argument
# 3 : Default argument
# 4 : Variable number of argument

def Information(Name,Age,Salary):
    print("Name is :",Name)
    print("Age is :",Age)
    print("Salary is :",Salary)

Information("Amit", 32, 9000000)
Information("Pooja",29,70000)
Information(Age=29,Salary=78000,Name="Sagar")