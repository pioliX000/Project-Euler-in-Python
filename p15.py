#!/usr/bin/env python3
# How many such routes are there through a 20x20 grid?

from sympy import factorial

n = 4

print((factorial(n)*factorial(n))/(factorial(n)+factorial(n)))