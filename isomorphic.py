p,r=map(str,input().split())
d=0
for x in range(0,len(p)):
    if((ord(p[x])-ord(p[x-1]))!=(ord(r[x])-ord(r[x-1]))):
         d=d+1
if(d>0):
      print ("no")
else:
     print ("yes")
