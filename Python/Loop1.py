def Display(Cnt):
    i=0
    if(Cnt <=0):
        print("Invalid input")
        return

    while(i< Cnt):
        print("Jay ganesh...",end = " ")
        i=i+1

def Main():
    Cnt= int(input("Please enter Frequency :"))
    Display(Cnt)

if __name__=="__main__":
    Main()
