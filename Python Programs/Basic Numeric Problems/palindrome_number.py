n=int(input())
org=n
rev=""
while(n>0):
    d=n%10
    rev+=str(d)
    n=n//10
if org==int(rev):
    print("{} is palindrome num".format(org))
else:
    print("{} is not a palindrome num".format(org))


    
    
#without datatype conversion
n=int(input())
org=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10 + d
    n=n//10
if org==rev:
    print("{} is palindrome num".format(org))
else:
    print("{} is not a palindrome num".format(org))
