def facts(no):
    fixed=no
    sum=0
    for i in range(1,no):
        if fixed%i==0:
           sum=sum+i
    return sum
                  
    
            
    
    
def main():
    num=int(input("Enter num: "))
    ret=facts(num)
    print(f"Addition of all factors of {num} is :- {ret}")
    
    
if __name__=="__main__":
    main()