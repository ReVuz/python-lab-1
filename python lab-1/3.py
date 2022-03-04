name=input("Enter name of the Employee: ")
code=int(input("Enter Employee code: "))
BP=float(input("Enter the basic pay of the Employee: "))
def GS(pay):
    if pay<10000 :
        DA=(pay*5)/100
        HRA=(pay*2.5)/100
        MA=500
    elif pay<30000 and pay>10000 :
        DA=(pay*7.5)/100
        HRA=(pay*5)/100
        MA=2500
    elif pay<50000 and pay>30000 :
        DA=(pay*11)/100
        HRA=(pay*7.5)/100
        MA=5000
    else :
        DA=(pay*25)/100
        HRA=(pay*11)/100
        MA=7000

    gs=pay+DA+HRA+MA
    return gs
def deduct(pay):
    IT=0
    if pay<10000 :
        PF=(pay*8)/100
        PT=20
    elif pay<30000 and pay>10000 :
        PF=(pay*8)/100
        PT=60
    elif pay<50000 and pay>30000 :
        PF=(pay*11)/100
        PT=60
        IT+=(pay*11)/100
    else :
        PT=80
        PF=(pay*12)/100
        IT+=(pay*20)/100

    d=PT+PF+IT
    return d

def net_sal(pay):
    sal=GS(pay)-deduct(pay)
    return sal

print("Gross Salary(GS) = ",GS(BP))
print("Deduction(D) = ",deduct(BP))
print("Net Salary = ",net_sal(BP))
