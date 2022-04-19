s=str(input("Enter a string "))
def st(s):
	l=len(s)
	print("\nSubstrings of ",s," are : ")
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			substring=s[i:j]
			print(substring)

st(s)
k=int(input("Enter length of substring : "))
def len_k(s,k):	
	l=len(s)
	print("\nSubstrings of length ",k," : ")
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			substring=s[i:j]
			if len(substring)==k:
				print(substring)
len_k(s,k)
n=int(input("Enter the number of distinct characters : "))
def dist(s,k,n):
	l=len(s)
	print("Distinct substring: ")
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			substring=s[i:j]
			sett=set(substring)
			if (len(substring)==n):
				if(len(sett)==n):
					print(substring)
dist(s,k,n)
def max_len(s,n):
	l=len(s)
	sub_store=[]
	print("Distinct substring with maximum length : ")
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			substring=s[i:j]
			sett=set(substring)
			if(len(sett)==n):
					sub_store.append(substring)
	find_max=len(max(sub_store, key=len))
	for k in range(len(sub_store)):
		if(len(sub_store[k])==find_max):
			print(sub_store[k])
			print("Length of substring : ",find_max)
max_len(s,n)
def pal(s):
	l=len(s)
	print("Palindrome substrings are : ")
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			substring=s[i:j]
			slic_e=substring[::-1]
			if(slic_e==substring):
				print(slic_e)
pal(s)
