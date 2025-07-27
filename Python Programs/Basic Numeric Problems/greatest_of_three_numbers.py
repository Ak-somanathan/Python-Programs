n1,n2,n3 = map(int, input().split())
if n1>n2 and n1>n3:
    print("{} is greater than {} and {}".format(n1,n2,n3))
elif n2>n1 and n2>n3:
    print("{} is greater than {} and {}".format(n2,n1,n3))
else:
    print("{} is greater than {} and {}".format(n3,n1,n2))
