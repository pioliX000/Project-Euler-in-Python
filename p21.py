#!/usr/bin/env python3
# Evaluate the sum of all the amicable numbers under 10000.

amicables = []

def divisors(n):
	divs = []
	for i in range(1, n+1):
		if n % i == 0:
			divs.append(i)
	return divs

def amicable(num):
	return sum(divisors(num)[:-1])

for i in range(1, 10000):
	if amicable(amicable(i)) == i and amicable(i) != i:
		print(i)
		amicables.append(i)	

print(sum(amicables))