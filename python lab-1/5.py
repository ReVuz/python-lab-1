"""Develop a program to read a string and perform the following
operations:
• Print all possible substring
• Print all possible substrings of length K
• Print all possible substrings of length K with N distinct
characters
• Print all palindrome substrings"""

s=str(input("Enter a string "))
def st(s):
    l=len(s)
    print("\nSubstring : ")
    for i in range(0,l+1):
        for j in range(i+1,l+1):
            substring=s[i:j]
            print(substring)

st(s)
k=int(input("Enter length "))
def len_k(s,k):
    l=len(s)
    for i in range(0,l+1):
        for j in range(i+1,l+1):
            substring=s[i:j]
            if len(substring)==k:
                print(substring)
len_k(s,k)
def dist(s,k):
    l=len(s)
    print("Distinct substring: ")
    for i in range(0,l+1):
        for j in range(i+1,l+1):
            substring=s[i:j]
            sett=set(substring)
            if len(substring)==k:
                if(len(sett)==k):
                    print(substring)
dist(s,k)
def pal():
    l=len(s)
    print("Palindrome substrings are : ")
    for i in range(0,l+1):
        for j in range(i+1,l+1):
            substring=s[i:j]
            slic_e=substring[::-1]
            if(slic_e==substring):
                    print(slic_e,end=",")
pal()

