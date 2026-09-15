#consutructor fixed name  - __init__
#descructor fixed name-  __del__
class Demo:
    def __init__(self):
       print("Inside constructor")#object chi memory geli
    
    def __del__(self):
        print("Inside destructor")#object chi memeory last la jate 
        

obj1=Demo()
obj=Demo()
print("End of application")
    