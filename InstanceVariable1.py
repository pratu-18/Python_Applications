class Marvellous:
    #class variable both
    no1=11
    no2=12
    
    def __init__(self):
        self.value1=21#instance variable
        self.value2=51#instance variable
     
print(Marvellous.no1)   
print(Marvellous.no2)
  
#object or instance creation
mobj1=Marvellous()
mobj2=Marvellous()
mobj3=Marvellous()

print(mobj1.value1)
print(mobj2.value1)
        