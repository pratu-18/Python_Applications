#             List              tuple
#____________________________________________-
#ordered      yes                yes 
#Indexed      yes                yes
#mutable      yes                No
#heterogenious yes               yes 

def main():
   Data1=[10,3.14,True,"Pune"] #list #hetrogenious-kuthlya type cha data accept krto kahi lihu shkto
   Data2=(10,3.14,True,"Pune") #tuple

   print(Data1)
   print(Data2)
   print(Data1[0])
   print(Data2[0])





if __name__=="__main__":
    main()