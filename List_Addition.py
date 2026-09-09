def add(lst_val):
    sum=0
    for i in lst_val:
        sum=sum+i
    return sum

def main():
    lst=[1,2,3,4,5]
    ret=add(lst)
    print("sum= ",ret)


if __name__=="__main__":
    main()