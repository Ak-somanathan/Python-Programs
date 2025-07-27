n=int(input())
a,b=0,1
for i in range(1,n+1):
    if n==i:
        print(a)
    else:
        a,b=b,a+b
