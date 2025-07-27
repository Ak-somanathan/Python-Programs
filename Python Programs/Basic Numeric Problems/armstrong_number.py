n=int(input())
a=str(n)
sum=0
for i in a:
    sum+= int(i)**len(a)
if n==sum:
    print("{} is an armstrong number".format(n))
else:
    print("{} is not an armstrong number".format(n))
