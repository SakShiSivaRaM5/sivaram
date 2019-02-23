n=int(input())
r=[]
for x in range(0,2**n):
    r.clear()
    r.append(format(x,"b"))
    k="".join(map(str,r))
    while(len(k)!=n):
        k='0'+k
    if(x!=(2**n)-1):
        print(k+"\t")
    else:
        print(k)
