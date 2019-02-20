lower,upper=map(int,input().split())
lower=int(lower)
upper=int(upper)
for j in range(lower+1,upper):
    if(j%2==0):
        print(j,end=" ")
