n=int(input())
s=[]
for x in range(0,2**n):
    s.clear()
    s.append(format(x,"b"))
    k="".join(map(str,s))
    while(len(k)!=n):
        k='0'+k
    if(x!=(2**n)-1):
        print(k+"\t")
    else:
        print(k)
