def add(val1,val2):
    return val1+val2
    
    
def main():
    print("Enter num1")
    no1=int(input())
    
    print("Enter num1")
    no2=int(input())
    
    ret=add(no1,no2)
    print(f"Addition is {ret}")
if __name__=="__main__":
    main()
