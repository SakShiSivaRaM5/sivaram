from itertools import permutations 
h=list(input()) 
p = permutations(h) 
d=[]  
for i in list(p):
  r='' 
  for j in i:
    r+=j
  if r not in d:
    d.append(r)
    print(r)
