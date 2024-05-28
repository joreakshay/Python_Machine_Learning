import os
import shutil

def ShowFileNameFileExtention(fobj, DirName, FileExtention):
    flag=os.path.isabs(DirName)
    if(flag==False):
        DirName=os.path.abspath(DirName)
    exist = os.path.isdir(DirName)
    if(exist==True):
        for foldername, subfoldername, filename in os.walk(DirName):
           
            for name in filename:
                if(name.lower().endswith(FileExtention)):
                     fobj.write(name+"\n")
    else:
         fobj.write("Directory not exist\n")



def ChangeFileExtention(fobj, DirName, SrcFileExtention,DesFileExtention):
    flag=os.path.isabs(DirName)
    if(flag==False):
        DirName=os.path.abspath(DirName)
    exist = os.path.isdir(DirName)
    if(exist==True):
        for foldername, subfoldername, filename in os.walk(DirName):           
            for name in filename:
                if(name.lower().endswith(SrcFileExtention)):
                    os.rename(os.path.join(foldername,name), os.path.splitext(os.path.join(foldername,name))[0]+DesFileExtention)
                     
    else:
         fobj.write("Directory not exist\n")

def CopyFilesToDir(fobj, srcDirName,desDirName):
    flag=os.path.isabs(srcDirName)
    if(flag==False):
        srcDirName=os.path.abspath(srcDirName)
    exist = os.path.isdir(srcDirName)
    if(exist==True):
        if(os.path.isdir(desDirName)==False):
            os.makedirs(desDirName)
        flag=os.path.isabs(desDirName)
        if(flag==False):
            desDirName=os.path.abspath(desDirName)

        for foldername, subfoldername, filename in os.walk(srcDirName):
            for name in filename:
                shutil.copyfile(os.path.join(srcDirName,name),os.path.join(desDirName,name))
                     
    else:
         fobj.write("Directory not exist\n")

def CopyFilesToDirByExtention(fobj, srcDirName, desDirName, fileExtention):
    flag=os.path.isabs(srcDirName)
    if(flag==False):
        srcDirName=os.path.abspath(srcDirName)
    exist = os.path.isdir(srcDirName)
    if(exist==True):
        if(os.path.isdir(desDirName)==False):
            os.makedirs(desDirName)
        flag=os.path.isabs(desDirName)
        if(flag==False):
            desDirName=os.path.abspath(desDirName)

        for foldername, subfoldername, filename in os.walk(srcDirName):
            for name in filename:
                if(name.lower().endswith(fileExtention)):
                    shutil.copyfile(os.path.join(srcDirName,name),os.path.join(desDirName,name))
                     
    else:
         fobj.write("Directory not exist\n")
