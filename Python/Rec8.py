
def fun(Cnt):
    if(Cnt>0):
        print(Cnt)
        Cnt=Cnt-1
        fun(Cnt)

def main():
    print("Enter no:")
    Num=int(input())
    fun(Num)

if(__name__=="__main__"):
    main()