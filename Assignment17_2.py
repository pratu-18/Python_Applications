def pattern(no):
    for i in range(0,no):
        for value in range(0,no):
            print("*", end=" ")
        print()
    
    
def main():
    num=int(input("Enter num: "))
    pattern(num)
    
if __name__=="__main__":
    main()