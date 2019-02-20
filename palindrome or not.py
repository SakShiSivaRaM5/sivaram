m=int(input(""))
d=m
x=0
while m>0:
    i=m%10
    m=m//10
    x=str(x)+str(i)
x=int(x)-int(x[0])
if x==d:
    print("yes")
else:
    print("no")
