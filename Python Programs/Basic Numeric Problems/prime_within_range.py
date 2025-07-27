start=int(input())
end=int(input())
for i in range(start, end+1):
    for j in range(2,i+1):
        if i%j==0:
            print(i, end=" ")
