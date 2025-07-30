import sympy
s=int(input())
for i in range(s+1,999999):
    if sympy.isprime(i):
        print(i)
        break
