#coin exchange

coins=[10,7,54,60,33,4,5]
total_value=100
result=[]
while total_value>0:
    m=max(coins)
    if max(coins)<=total_value:
        total_value=total_value-m
        result.append(m)
    else:
        i=coins.index(m)
        coins.pop(i)
        continue

print('Exchanged coins are :',result)
