import schedule
import time
import sys
import os

def bakupCopy(DirectoryName):
    file="MyFile.txt"
    fobj=open(file,"w")
    
    data=fobj.read()
    fobj.close()
    
    newfile=open("Test1","w")
    newfile.write(data)
    newfile.close()
    
    
    


def main():
    
    
    res1=os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])
    res2=os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])
 
    if len(sys.argv)==3:
        
        
        if res1==True:
            # bakupCopy(sys.argv[1])
            print("all conditions pass")
            
            
        
        elif res2==True:
            print("This is not type of directory")
            
        else:
           print("No such directory found")
    
    else:
        print("Invalid number of argument")
    
    
    
    
if __name__=="__main__":
    main()   