n=int(input("Enter No of Jobs : "))
l=[]
for i in range(n):
     j=int(input(" Enter Job Number : "))
     d=int(input(" Enter Respective Job Deadline : "))
     p=int(input(" Enter Respective Job Profit : "))
     l.append((j,d,p))
l.sort(key = lambda x: x[2],reverse=True)

s = [dl[1] for dl in l]
x=[]
for i in range(max(s)+1):
    x.append('0')

for i in s:
    pos=i
    if x[pos-1]=='0':
        x[pos-1]=i
    else:
        while pos>=1:
            pos=pos-1
            if x[pos-1]=='0':
                x[pos-1]=i
            break
        continue
print(x[0:-1])
print(l)
