start=int(input())
end=int(input())
for i in range(start, end+1):
    sum=0
    a=str(i)
    for j in a:
        sum+=int(j)**len(a)
    if i==sum:
        print(i,end=" ")
