def divFive(val):
    if val %5==0:
        return True
    else:
        return False
    
    
    
def main():
    num=int(input("Enter number :"))
    ret=divFive(num)
    
    if ret==True:
        print(True)
    else:
        print(False)
    
    

    
if __name__=="__main__":
    main()