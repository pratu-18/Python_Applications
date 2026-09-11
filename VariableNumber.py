#4th type of parameter 

def Display(*Data):#variable number of
    print(Data)
    print(type(Data))

def main():
    Display(10,20,40,50,70,55.90,"Pune",False)#mnje *Data yacha arth kiti pn parameter gheu shkto 
    Display(18,67)

if __name__=="__main__":
    main()