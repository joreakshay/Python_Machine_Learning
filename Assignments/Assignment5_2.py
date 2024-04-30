
def Pattern(No):
    if(No>=1):
        i=No       
        No=No-1
        Pattern(No)
        print(i, end=" ")
   

def main():
    print("Enter no:")
    Num=int(input())
    Pattern(Num)
    
if(__name__=="__main__"):
    main()