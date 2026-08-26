def numCheck(val):
    if val>0:
        print("Positive number")
    elif val ==0:
        print("Zero")
    else:
        print("Negative number")
    
    
def main():
    num=int(input("Enter number :"))
    numCheck(num)
    
    
if __name__=="__main__":
    main()