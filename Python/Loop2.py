def Display(Cnt):
    i=0
    if(Cnt <=0):
        print("Invalid input")
        return

    for no in range(Cnt):
        print("Jay ganesh...",end = " ")

def Main():
    Cnt= int(input("Please enter Frequency :"))
    Display(Cnt)

if __name__=="__main__":
    Main()
