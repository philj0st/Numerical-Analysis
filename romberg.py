# -*- coding: utf-8 -*-
import math
from functools import lru_cache
from time import time
from scipy.integrate import  romberg

def rombergMethod(f,a,b,m):

    # trapezoidal rule for f in [a,b] and a given j (interval division factor)
    def trapezoidal(j):
        # interval width
        hj = (b-a)/2**j
        # intervals
        nj = 2**j

        sum = (f(a)+f(b))/2
        # 1..nj-1 terms
        for i in range(1,nj):
            xi = a+i*hj
            sum += f(xi)
        
        return hj * sum
        
    @lru_cache(maxsize=None)
    def T(j,k):
        # base case: use trapezoidal
        if k==0: return trapezoidal(j)
        
        # otherwise recurse
        return (4**k * T(j+1,k-1) - T(j,k-1))/(4**k -1)

    # return root of the recursion
    return T(0,m)

f = lambda x: math.cos(x**2)
t0 = time()
task2 = rombergMethod(f,0,math.pi,16)
print("time",time()-t0)

# check task 2:
# intermediate results were compared while debugging
print(task2) # correct

# cross validate with reference implementation
print("abs err: ",task2-romberg(f,0,math.pi))