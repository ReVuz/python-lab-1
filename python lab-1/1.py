a=int(input("Enter a four digit number "))
num=a
s=num%10
num=num//10
u=num%10
num=num//10
M=num%10
num=num//10
m=num%10
num=num//10
print("Sum of ",m,"+",M,"+",u,"+",s," is = ",s+u+M+m)
print("Reverse of ",a," is: ",s,u,M,m)
p1=s*M
p2=u*m
print("Difference between the product of the digits at the odd and the product of digits at even is ",p2-p1)

