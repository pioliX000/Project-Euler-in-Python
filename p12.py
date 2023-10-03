#!/usr/bin/env python3
# What is the value of the first triangle number to have over five hundred divisors?
# (n)(n + 1) / 2

from sympy import divisor_count

divisors = 0

for x in range(1, 100000):
	print(x)
	tri = int(x*(x+1)/2)

	if divisor_count(tri) >= 500:
		print(tri)
		break
