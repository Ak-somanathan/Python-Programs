n=list(map(int, input().split()))
u_f=n[0]%10
u_s=n[1]%10
if u_f<u_s:
    print(n[0],n[1])
elif u_f==u_s:
    n.sort()
    print(n[0],n[1])
else:
    print(n[1],n[0])
