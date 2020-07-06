#fractional_knapsack
M=float(input("Enter maximum Weight : "))
n=int(input("Enter No of Objects : "))
l=[]
x=[]
for i in range(n):
    x.append('0')

for i in range(n):
     w=float(input(" Enter Object Weight : "))
     v=float(input(" Enter Respective Object Value : "))
     l.append((w,v))
l.sort(key = lambda x: x[1]/x[0],reverse=True)
#print(l)
z=0
weight=0
res = [w[0] for w in l]
res2 = [v[1] for v in l]

while z<n and weight<=M:
    if weight+res[z]<=M:
        x[z]=1.0
    else:
        x[z]=float((M-weight)/res[z])

    weight=weight+(x[z]*res[z])
    z=z+1
#print(res2)
#print(x)
sum=0
q=0
while q<n:
    sum=sum+(float(x[q])*float(res2[q]))
    q=q+1
print(sum)
