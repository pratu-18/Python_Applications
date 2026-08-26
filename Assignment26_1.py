class Demo:
    value=10
    
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
        
    def fun(self):
       
        print("value of  no1 from fun= ",self.no1)
        print("value of  no1 from fun= ",self.no2)
        print("-"*25)
    
        
    def gun(self):
        
        print("value of  no1 from gun= ",self.no1)
        print("value of  no1 from gun= ",self.no2)
        print("-"*25)
        
obj1=Demo(11,12)
obj2=Demo(51,101)
obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
