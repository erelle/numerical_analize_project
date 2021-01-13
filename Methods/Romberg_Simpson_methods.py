from __future__ import division

import numpy as np


def trapezcomp(f, a, b, n):

    h = (b - a) / n
    x = a

    In = f(a)
    for k in range(1, n):
        x  = x + h
        In += 2*f(x)

    return (In + f(b))*h*0.5


def romberg(f, a, b, n):

    print("\n>>>>>>>>>>>>>> Romberg >>>>>>>>>>")

    R = np.zeros((n, n))
    for k in range(0, n):
        R[k, 0] = trapezcomp(f, a, b, 2**k)
        print(f"\niteration number => {k+1}")
        for j in range(0, k):
            R[k, j+1] = (4**(j+1) * R[k, j] - R[k-1, j]) / (4**(j+1) - 1)
        print(R[k,0:k+1])
    print(f"\nNumber of iteration is : {k+1}")

    print(f"\nThe solution of Romberg is : {R[n - 1][n - 1]}")

    return R[n - 1][n - 1]



def simpson(f,a, b, n):
    print("\n>>>>>>>>>>>>>> Simpson >>>>>>>>>>")
    sum = 0
    inc = (b - a) / n
    for k in range(n + 1):
        x = a + (k * inc)
        summand = f(x)
        print(f"\niteration number => {k+1}")
        if (k != 0) and (k != n):
            summand *= (2 + (2 * (k % 2)))
            sum += summand
        print(sum)
    result=((b - a) / (3 * n)) * sum
    print(f"\nNumber of iteration is : {k+1}")
    print(f"\nThe solution of Simpson is : {result}")

    return result
