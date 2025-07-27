n=int(input())
a=str(n)
sum=0
for i in a:
    fact=1
    for j in range(1,int(i)+1):
        fact*=j
    sum+=fact
if sum==n:
    print("{} is a strong num".format(n))
else:
    print("{} is not a strong num".format(n))
