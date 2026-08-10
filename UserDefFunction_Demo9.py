#bigbazar fun amul fun la hide krtay it's called abstraction , bigbazar call kelya shivy amul call krta yet nhi 
def BigBazar():
    print("Inside bigbazar")

    def Amul():#inner function 
        print("Inside ice cream parlor")

    Amul()
    Amul()
    



def main():
    BigBazar()#1st we need to call outer fun then we call inner fun from outer fun
    

if __name__=="__main__":
    main()