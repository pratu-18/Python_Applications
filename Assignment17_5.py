def prime(no):
    fixed=no
    for i in range(2,no):
        if fixed%i==0:
            return False
    else:
        return True
    
    
def main():
    num=int(input("Enter num: "))
    res=prime(num)
    if res==False:
        print("Not prime number")
    else:
        print("Prime number")
    
if __name__=="__main__":
    main()