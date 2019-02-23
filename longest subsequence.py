num=int(input())
q=list(map(int,input().split()))
s=0
l=[]
for i in range(0,len(q)-1):
	if int(q[i+1])>=int(q[i]):
		s=s+1
	else:
		l.append(s)
		s=0
print(max(l)+1)
