i=1
def fun(Cnt):
    global i
    print(i)
    if(i<Cnt):
        i=i+1
        fun(Cnt)

def main():
    print("Enter no:")
    Num=int(input())
    fun(Num)

if(__name__=="__main__"):
    main()