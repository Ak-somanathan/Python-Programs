m,n=map(int,input().split())
hh,mm=input().split(":")
mem=list(map(str,input().split()))
c=0
for i in mem:
    h,mi=i.split(":")
    if (int(h)<int(hh)) or (int(h)==int(hh) and (int(mi)==int(mm) or int(mi)<int(mm))):
        c+=1
if c==n or c>n:
    print("no")
else:
    print("yes")
