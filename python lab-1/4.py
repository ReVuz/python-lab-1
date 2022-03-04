a = int(input("Enter a number "))
def is_happy(a):
    num = a
    for i in range(100):
        s = 0
        while num!= 0:
            r = num%10
            s += r*r
            num = num//10
        num = s
        if s == 1:
           return True
    return False
if is_happy(a) == True:
    print("Happy")
else:
    print("Sad")
def h_range():
    r1=int(input("\nEnter starting range: "))
    r2=int(input("Enter end range: "))
    print("\nHappy numbers from ",r1," to ",r2," are: ")
    for i in range(r1,r2+1):
        if is_happy(i)==True:
           print(i)
h_range()

def n_happy():
    n = int(input("\nEnter how many happy numbers do you want to print: "))
    print("First ",n," happy numbers are: ")
    i=0
    while n != 0:
        i += 1
        if is_happy(i) == True:
            n -= 1
            print(i)
n_happy()
