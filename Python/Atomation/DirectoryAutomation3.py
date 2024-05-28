import sys
import os
import time
def DirectoryWatcher(DirName):

    flag=os.path.isabs(DirName)
    if(flag==False):
        DirName=os.path.abspath(DirName)
    exist = os.path.isdir(DirName)
    if(exist==True):
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current folder is", foldername)

            for subname in subfoldername:
                print("Sub folder name :",subname)

            for name in filename:
                print(name)
    else:
        print("Directory not exist")

def main():
    print("-----------------------------------------------------")
    print("--------------------Directory Watcher----------------")
    print("-----------------------------------------------------")
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H" ):
            print("This script is used to perform Directory travarsal")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use of script :")
            print("Name_of_file Name_of_Directory")
            exit()
       
        try:
            starttime=time.time()
            DirectoryWatcher(sys.argv[1])
            endtime=time.time()

            print("Time required to exicute :", endtime-starttime)
            
        except Exception as obj2:
            print("Unable to perform opration due to ", obj2)

    else:
        print("Invalid option")
        print("Use --h option to get the help  and --u option to get the usage of application")

    print("-----------------------------------------------------")
    print("----------Thank you for using our script-------------")
    print("------------------Akshay Jore------------------------")
    print("-----------------------------------------------------")
    
if __name__ =="__main__":
    main()