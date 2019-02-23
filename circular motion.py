def pro_23():
    s=input()
    st=list(s)
    m,e,s,w=(0,1,2,3)
    dir=m
    z,v=0,0
    for move in st:
        if(move == 'L'):
            dir=(dir+1)%4
        elif(move == 'R'):
            dir=(4+dir-1)%4
        else:
            if(dir==m):
                v+=1
            elif(dir==e):
                z+=1
            elif(dir==w):
                z-=1
            elif(dir==s):
                v-=1
    if(z==0 and v==0):
        print("yes")
    else:
        print("no")
pro_23()
