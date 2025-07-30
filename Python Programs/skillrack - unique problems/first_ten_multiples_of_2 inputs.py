n=list(map(int, input().split()))
n.sort()
a=set([n[0]*i for i in range(1,11) ])
b=set([a.add(n[1]*i) for i in range(1,11) ])
a=sorted(a)
for i in range(0,10):
    print(a[i],end=" ")
