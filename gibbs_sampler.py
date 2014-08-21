# -*- coding: utf-8 -*-
"""
Gibbs sampler
"""
from numpy.random import gamma, normal 
from timeit import timeit


def pyGibbs(N = 10000, thin = 500):
    x = 0
    y = 0
    mat = []
    for i in range(1, N + 1):
        for j in range(1, thin + 1):
        # Note that scale = 1/rate. The R implementation uses rate
            rate = y*y + 4
            x = gamma(shape = 3, scale = 1/float(rate))
            y = normal(loc = 1/(x + 1), scale = 1/np.sqrt(2*(x + 1)))
        mat.append([x, y])
    return mat
    

print(timeit(pyGibbs, number =1))

#vals = pyGibbs(10000,500)
#X, Y = zip(*vals)
#min(X)
#mean(X)
#max(X)
#min(Y)
#mean(Y)
#max(Y)


