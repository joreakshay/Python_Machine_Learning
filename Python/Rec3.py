
def fun():
    print("inside fun")
    fun()

def main():
    fun()

if(__name__=="__main__"):
    main()