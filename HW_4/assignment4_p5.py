# Exercise 7-3

#def estimate_pi():
import math

def fact(a):
    """
    Uses recursion for factorials
    """
    if a == 0:
        return 1
    else:
        a_1 = fact(a-1)  # actual recursion happens here
        a_ex = a * a_1  # multiplied numbers
        return a_ex

def big_function(k):
    """
    condenses the big formula into a function that can be called
    """
    n = fact(4 * k) * (1103 + 26390 * k) / (fact(k) ** 4 * 396**(4*k))
    return n

def estimate_pi():
    """
    used to estimate pi
    :return: an estimate of pi
    """
    k = 0
    k_past = 1
    while abs(k-k_past) > 1e-15:
        k_past = 9801/(8**(1/2)) / (big_function(k)+k)
        k = k_past
    return k

print(estimate_pi())