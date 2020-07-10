#optimal merge

n=int(input("Enter the number of lists : "))
l=[]
for i in range(n):
    x=input("Enter List Vales separated by  comma : ",)
    l.append(x.split(','))

def Sorting(lst):
    lst.sort(key=len)
    return lst

while len(l)>2:
    Sorting(l)
    res=sorted(l[0]+l[1])
    del(l[0])
    del(l[0])
    l.append(res)

print(sorted(l[0]+l[1]))
