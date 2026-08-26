#prime
def prime(no):
  #prm=None
  for i in range(2,no):
     if no%i==0:
       return False
  return True

#Count 
def lengthX(no):
    cont=0
    while no!=0:
       rem=no%10
       cont=cont+1
       no=no//10
    return cont


#sum 
def sum(no):
    sum=0
    while no!=0:
       rem=no%10
       sum=rem+sum
       no=no//10
    return sum


#reverse
def reverse(no):
    rev=0
    while no>0:
        rem=no%10
        rev=rev*10+rem
        no=no//10
    return rev

#Palindrom
def palindrom(num):
    rev=0
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if rev==temp:
        return True
    return False
