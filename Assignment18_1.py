def Nlist(lst):
    sum=0
    for element in lst:
        sum=sum+element
    return sum
    
    
def main():
    num=int(input("Enter limit of list: "))
    l1=list()
    print("Enter values: ")
    
    for i in range(0,num):
        value=int(input())
        l1.append(value)
        
    print(l1)
    
    res=Nlist(l1)
    print(f" addition is :{res}")
        
    
    
if __name__=="__main__":
    main()