import multiprocessing
 
def main():
    print("CPU count:", multiprocessing.cpu_count())
   
if __name__=="__main__":
    main()