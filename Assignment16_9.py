def even(val):
    for i in range(1,val+1):
        if i%2==0:
            print(i,end=" ")
    
    
def main():
    num=20
    even(num)
    
    
if __name__=="__main__":
    main()