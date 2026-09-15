class Base:
        
    def fun(self):
        print("Inside base fun")
 

class Derived(Base):
    def sun(self):
        print("Inside derived sun")
    
    
bobj=Derived()
bobj.fun()#child can access this
bobj.sun()