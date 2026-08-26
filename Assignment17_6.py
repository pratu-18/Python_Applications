def pattern(no):
    for i in range(0,no):
        for j in range(0,no-i):
            print("*", end=" ")
        print()
    
def main():
    num=int(input("Enter num: "))
    pattern(num)
    
    
if __name__=="__main__":
    main()