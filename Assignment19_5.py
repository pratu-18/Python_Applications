from functools import reduce
def prime(value):
    if value<=1:
        return False
    for i in range(2,value):
        if value%i==0:
            return False
    return True
        
mul=lambda num:num*2


def max(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
    
    
   
def main():
    l1=[]
    limit=8
    print("Enter emlements :")
    
    for value in range(1, limit+1):
        elements=int(input())
        l1.append(elements)
    print("Input List: ",l1)
    
    Fdata=(list(filter(prime,l1)))
    print("List after Filter: ",Fdata)
    
    Mdata=list(map(mul,Fdata))
    print("List after map : ",Mdata)
    
    Final=int(reduce(max,Mdata))
    
    print("List after reduce :",Final)
    
    
    
        
if __name__=="__main__":
    main()
    
        
     
 