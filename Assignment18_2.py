def listN(lst):
    max=0
    for i in lst:
        max=i>max
    print(max) 
        
    
    
    
def main():
    num=int(input("Enter limit of list: "))
    l1=list()
    print("Enter values: ")
    
    for i in range(0,num):
        value=int(input())
        l1.append(value)
        
    print(l1)
    
    res=listN(l1)
    print(f" maximum number is :{res}")
        
    
    
if __name__=="__main__":
    main()