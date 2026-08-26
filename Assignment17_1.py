from Arithmatic_Module  import *

def main():
    
    num1=int(input("Enter num 1: "))
    num2=int(input("Enter num 2: "))
    ret1=add(num1,num2)
    ret2=sub(num1,num2)
    ret3=mul(num1,num2)
    ret4=div(num1,num2)
    
    print(f"Addition is :{ret1} ")
    print(f"Substraction is :{ret2} ")
    print(f"Multiplication is :{ret3} ")
    print(f"Division is :{ret4} ")
    
    
if __name__=="__main__":
    main()