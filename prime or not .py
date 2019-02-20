p=int(input(""))
t=0
for x in range(1,p+1):
   if(p%x==0):
    t=t+1
if(t==2):
    print("yes")
else:
    print("no")
