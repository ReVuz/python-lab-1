
import math

def read_tri():
    print("First Triangle")
    a=int(input("Enter first side "))
    b=int(input("Enter second side "))
    c=int(input("Enter third side "))
    print("\nSecond Triangle")
    p=int(input("Enter first side "))
    q=int(input("Enter second side "))
    r=int(input("Enter third side "))
    return a,b,c,p,q,r

def area(a,b,c):
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

a,b,c,p,q,r=read_tri()
A1=area(a,b,c)
A2=area(p,q,r)
print("\nArea1 = ",A1)
print("\nArea2 = ",A2)    

print("\nTotal Area : ",A1+A2)
print("\nPercentage contribution of Area1 = ",(A1/(A1+A2))*100,"%")
print("\nPercentage contribution of Area2 = ",(A2/(A1+A2))*100,"%")
