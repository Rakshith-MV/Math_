from math import *
import lagrange as le
import matplotlib.pyplot as plt
from  sympy import *
from numpy import *
def f(n):
    return 1/n**2

seq = []
sum = []
a = 0
A = [i for i in range(1,10)]
for i in A:
    b = float(f(i))
    seq.append(b)
    a += b
    sum.append(a)
# plt.plot(A,seq)
# plt.plot(A,sum)
# plt.legend(["sequence","summation"])
# plt.show()
n = var('n')
limit = le.lag_inter(A,sum,n)
print(limit)