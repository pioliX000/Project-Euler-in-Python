#!/usr/bin/env python3
# What is the 10001st prime number?

from sympy import isprime

primes = []

for i in range(1, 1000000):
	if isprime(i):
		primes.append(i)

print(primes[10000])