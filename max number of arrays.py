x=int(input())
b=[]
b=list(map(int,input().split()))
q1=b[::2]
q2=b[1::2]
q3=b[1::3]
if(sum(q1)>sum(q2) and sum(q1)>sum(q3)):
	print(sum(q1))
elif(sum(q3)>sum(q1) and sum(q3)>sum(q2)):
	print(sum(q3))
else:
	print(sum(q2))
