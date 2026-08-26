def star(val):
    for i in range(1,val+1):
        print("*", end=" ")
    
    
def main():
    num=int(input("Enter number :"))

    star(num)
    
if __name__=="__main__":
    main()