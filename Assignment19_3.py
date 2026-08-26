from functools import reduce

compare= lambda num:  num>=70 and num<=90
        
        
imcrement= lambda num: num+10
product= lambda num1, num2: num1*num2
def main():
    lst=[4,34,36,76,68,24,89,23,86,90,45,70]
    print(f"Input list = {lst}")
    res=list(filter(compare,lst))
    print(f"List after Filter = {res}")
    res2=list(map(imcrement,res))
    print(f"List after map = {res2}")
    
    final=int(reduce(product,res2))
    print(f"Output of reducec = {final}")
    
    
if __name__=="__main__":
    main()
        
    