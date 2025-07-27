n=list(map(str,input().split()))
count=0
for i in n:
    hh,mm=i.split(':')
    if (int(hh)==10 and int(mm)>00) or (int(hh)>10):
            count+=1
print(count)
