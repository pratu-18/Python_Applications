
from Marvellous2 import Addition,Substraction
#from Marvellous2 import Substraction or *




def main():
    print("enter 1st no ")
    value1=int(input())
    print("enter 2nd no ")
    value2=int(input())

    ret=Addition(value1,value2)
   
    print("addition is ",ret)
    ret=Substraction(value1,value2)
    print("Substraction is ",ret)


if __name__=="__main__":#starter,code starts from here
    main() 