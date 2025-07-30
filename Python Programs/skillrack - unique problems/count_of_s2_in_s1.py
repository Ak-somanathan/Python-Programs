a=input()
b=input()
a=list(a)
count=0
for i in range(0,len(a)+1):
    if i<len(a)-1:
        c=a[i]+a[i+1]
        if b==c:
            count+=1
print(count)
