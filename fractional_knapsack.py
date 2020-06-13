#fractional_knapsack
M=float(input("Enter maximum Weight : "))
n=int(input("Enter No of Objects : "))
ww=[]
vv=[]
vw=[]
for i in range(n):
     a=float(input(" Enter Object Weight : "))
     b=float(input(" Enter Respective Object Value : "))
     ww.append(a)
     vv.append(b)

for i in range(n):
    div=vv[i]/ww[i]
    vw.append(div)

sortvw = sorted(vw)
sortvw.reverse()

x=[]
for i in range(n):
    x.append('0')

w=[]
v=[]

for i in sortvw:
    pos = vw.index(i)
    w.append(ww[pos])
    v.append(vv[pos])

weight=0
z=0

while z<n and weight<M:
    if weight+w[z]<=M:
        x[z]=1
    else :
        x[z]=(M-weight)/w[z]

    weight=weight+(x[z]*w[z])
    z=z+1

ans=0

for i in range(n):
    ans=ans+(x[i]*vv[i])

print("Maximum value is:",ans)
