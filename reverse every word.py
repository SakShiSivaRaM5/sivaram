s=input()
k=list(s.split())
q=[]
s=''
for j in range(len(k)):
	s+=k[j][::-1]+' '
print(s)
