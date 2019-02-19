n=int(input())
l=input().split()
k=[]
s=[]
for x in l:
    k.append(int(x))
for x in range(0,len(k)):
    s1=0
    s2=0
    d1=0
    d2=0
    for y in range(x+1,len(k)):
        s1=s1+k[y]
        d1=d1+1
    if(d1>0):
        s1=int(s1/(d1))
    for z in range(0,x+1):
        s2=s2+k[z] 
        d2=d2+1
    if(d2>0):
        s2=int(s2/(d2))
    if(s1==s2):
        print("yes")
        break
else:
    print("no")
