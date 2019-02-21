m1,m2=map(int,input().split())
for m2 in range(m1+1,m2):
	for l in range(2,m2):
		if(m2%l==0):
		   break
	else:
		print(m2,end=' ')
