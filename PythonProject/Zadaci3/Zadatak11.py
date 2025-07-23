from sympy import *

def prost_broj(a,b):
    for broj in range(a,b):
        if(isprime(broj)):
            yield broj
    return


for broj in prost_broj(1,10):
    print(broj)

