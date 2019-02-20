lower,upper=map(int,input().split())
lower=int(lower)
upper=int(upper)
for i in range(lower+1,upper):
    if(i%2==0):
        print(i,end=" ")
