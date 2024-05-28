

def sub(A,B):
    print(A-B)

def SmartSub(fptr):
    def Inner(A,B):
        if A<B:
            A,B=B,A
        return fptr(A,B)
    return Inner
sub=SmartSub(sub)

#simple code to undertand.
def sub1(A,B):
    print(A-B)
    
subptr=sub1

def InnerSub(A,B):
    if A<B:
        A,B=B,A
    return subptr(A,B)
    
sub1=InnerSub


def main():
    No1=int(input("Enter first number :"))
    No2=int(input("Enter second number :"))

    sub1(No1,No2)

if __name__=="__main__":
    main()