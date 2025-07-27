n=int(input())
res=""
for i in range(1,n+1):
    if i*i==n:
        res="perfect"
else:
    if res!="perfect":
        print("{} is not a perfect square".format(n))
    else:
        print("{} is a perfect square".format(n))




#using math
        
import math
n=int(input())
sq=math.sqrt(n)
if sq*sq==n:
    print("{} is a perfect square".format(n))
else:
    print("{} is not a perfect square".format(n))
