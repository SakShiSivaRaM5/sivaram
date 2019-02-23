n=int(input())
s=[]
for x in range(0,2**n):
    s.clear()
    s.append(format(x,"b"))
    j="".join(map(str,s))
    while(len(j)!=n):
        j='0'+j
    if(x!=(2**n)-1):
        print(j+"\t")
    else:
        print(j)
