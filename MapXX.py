
CheckEven= lambda no: (no%2==0)

Increment= lambda no: no+1

def main():
    data =[13,12,8,10,11,20]#4 even and 2 odd
    print("Input data is :",data)

    FData=list(filter(CheckEven,data))
    print("data after filter :",FData)

    MData=list(map(Increment,FData))#typecasting list type mde ghenr he 
    print("Data after map:",MData)





if __name__=="__main__":
    main()