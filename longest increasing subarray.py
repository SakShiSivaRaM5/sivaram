n=int(input())
arr=list(map(int,input().split()))
q = 1
l = 1
for i in range(1, n) :
    if (arr[i] > arr[i-1]) :
        l =l + 1
    else :
        if (q < l)  :
            q = l
        l = 1
if (q < l) :
    q = l
print(q)
