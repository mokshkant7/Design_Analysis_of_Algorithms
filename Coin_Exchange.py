a=[10,7,54,60,33,4,5]
x=100
result=[]
while x>0:
    m=max(a)
    if max(a)<=x:
        x=x-m
        result.append(m)
    else:
        i=a.index(m)
        a.pop(i)
        continue

print(result)
