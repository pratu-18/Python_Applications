def patternLess(no):
    increment=no+2
    for i in range(1,no+1):
        for j in range(1,increment-i):
            print(j,end=" ")
        print()
    
def main():
    num=int(input("Enter num: "))
    patternLess(num)
    
if __name__=="__main__":
    main()