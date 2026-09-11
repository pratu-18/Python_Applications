def add(*val):
    add=0
    for i in val:
        
        add=i+add
    return add

    
def main():
    res=add(10,20,30,40)
    print(res)


if __name__=="__main__":
    main()