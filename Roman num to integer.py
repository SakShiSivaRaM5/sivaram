val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
p = str(input())
p = p.upper()
k = 0
while p:
    if len(p) == 1 or val[p[0]] >= val[p[1]]:
        k += val[p[0]]
        p = p[1:]
    else:
        k += val[p[1]] - val[p[0]]
        p = p[2:]
print (k)
