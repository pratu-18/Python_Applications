def fact(no):
    mul=1
    for i in range(1,no+1):
        mul= mul*i
    return mul

        
        
    
    
def main():
    num=int(input("Enter num: "))
    res= fact(num)
    print(f"Factorial of {num} is -:  {res}")
    
    
if __name__=="__main__":
    main()