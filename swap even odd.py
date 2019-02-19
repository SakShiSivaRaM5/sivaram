try:
	p=0
	n=str(input())
	c=[]
	k=str()
	for i in range (0,len(n)):
		c.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(p!=j):
		t=c[p]
		c[p]=c[p+1]
		c[p+1]=t
		p=p+2
	for i in range (0,len(c)):
		k=k+c[i]
	print (k)
except:
	print ("Invalid")
