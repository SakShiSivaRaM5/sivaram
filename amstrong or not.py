e=int(input(""))
temp=e
i=0
while temp>0:
    num=temp%10
    i=i+num**3
    temp=temp//10
if(i==e):
    print("Yes")
else:
    print("No")
