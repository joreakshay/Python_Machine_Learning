import sys
import os
import time
import DirectoryAutomation

def main():
    fobj=open("Output.txt","w")
        
    fobj.write("-----------------------------------------------------\n")
    fobj.write("--------------------Directory Watcher----------------\n")
    fobj.write("-----------------------------------------------------\n")
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H" ):
            print("This script is used to perform to show file of given extention")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use of script :")
            print("Name_of_file Name_of_Directory File_Extention")
            exit()
    if(len(sys.argv)==3):
        try:
            starttime=time.time()
            DirectoryAutomation.ShowFileNameFileExtention(fobj,sys.argv[1],sys.argv[2])
            endtime=time.time()

            fobj.write("Time required to exicute :"+str(endtime-starttime)+"\n")
            
        except Exception as obj2:
            fobj.write("Unable to perform opration due to "+str(obj2)+"\n")

    else:
        print("Invalid option")
        print("Use --h option to get the help  and --u option to get the usage of application")

    fobj.write("-----------------------------------------------------\n")
    fobj.write("----------Thank you for using our script-------------\n")
    fobj.write("------------------Akshay Jore------------------------\n")
    fobj.write("-----------------------------------------------------\n")
    fobj.close()
    
if __name__ =="__main__":
    main()