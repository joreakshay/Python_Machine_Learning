
class Demo:
    Data1=11    #class Varible
    Data2=21    #class Varible
    def __init__(self,A,B): #instance variable
        print("Inside constroctor")
        self.No1=A  #instance variable
        self.No2=B  #instance variable

    def Display(self):  #instance method
        print("Value of No1 from display :",self.No1)
        print("Value of No2 from display :",self.No2)
        print("Value of No1 from display :",Demo.Data1)
        print("Value of No2 from display :",Demo.Data2)


    def Display1():
        print("Value of No1 from display :",Demo.Data1)
        print("Value of No2 from display :",Demo.Data2)

    @classmethod #decorator
    def Fun(cls):   #Class method cls==Class
        print("Value of No1 from display :",cls.Data1)
        print("Value of No2 from display :",cls.Data2)
    
    @staticmethod
    def Gun():
        print("Inside static msthod")

Demo.Fun()
Demo.Gun()
obj1=Demo(5,10)
obj1.Display()
