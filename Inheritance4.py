class Base:
    
        
    def fun(self):
        print("Inside base fun")
 

class Derived(Base):
    pass
    
    
bobj=Derived()
bobj.fun()#child can access this