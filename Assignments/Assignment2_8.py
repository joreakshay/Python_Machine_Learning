def main():
    print("Enter No:")
    No=int(input())
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("")

if(__name__=="__main__"):
    main()