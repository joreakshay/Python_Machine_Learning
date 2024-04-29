def CheckPrime(Num):
    for i in range(2,int(Num/2)+1):
        if(Num%i==0):
            return False
    return True

def ListAddion(Arr):
    Sum=0
    for no in Arr:
        Sum=Sum+no
    return Sum
