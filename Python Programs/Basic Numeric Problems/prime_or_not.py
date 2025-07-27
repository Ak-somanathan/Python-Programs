from sympy import isprime
n=int(input())
if isprime(n):
    print("{} is prime".format(n))
else:
    print("{} is not a prime".format(n))
