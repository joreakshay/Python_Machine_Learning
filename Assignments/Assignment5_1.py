
def Pattern(No):
    if(No>=1):
        print("*", end=" ")
        No=No-1
        Pattern(No)
   

def main():
    print("Enter no:")
    Num=int(input())
    Pattern(Num)

if(__name__=="__main__"):
    main()