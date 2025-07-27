n=int(input())
l=[]
max=0
for i in range(0,n):
    tot=0
    name,m,p,c=input().split(":")
    l.append(name)
    tot=int(m)+int(p)+int(c)
    l.append(tot)
else:
    for i in range(1,(n*2)+1,2):
        if l[i]>max:
            max=l[i]
print(l[l.index(max)-1])
