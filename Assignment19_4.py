from functools import reduce
even=lambda num : num%2==0
square=lambda num: num*num

sum=lambda num1, num2:num1+num2

def main():
    limit=10
    l1=[]
    print("Enter list elements: ")
    for i in range(0,limit):
        elements=int(input())
        l1.append(elements)
        
    print(f"Input list = {l1}")
    Fdata=list(filter(even,l1))
    print("List after filter: ",Fdata)
    
    Mdata=list(map(square,Fdata))
    print(f"List after Map = {Mdata}")
        
    Rdata=int(reduce(sum,Mdata))
    print(f"Output of reducec = {Rdata}")
    
    
if __name__=="__main__":
    main()

