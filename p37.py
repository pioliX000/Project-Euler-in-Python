#!/usr/bin/env python3
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from sympy import isprime

truncatables  = []
truncatable = False

for i in range(23, 1000000):
	if isprime(i):
		left_i = i
		right_i = i

		while len(str(left_i)) > 1:
			left_i = int(str(left_i)[1::])
			right_i = int(str(right_i)[::-1][1::][::-1])

			if isprime(left_i) and isprime(right_i):
				truncatable = True
			else:
				truncatable = False
				break

	if truncatable:
		truncatables.append(i)
		truncatable = False

print(truncatables)
print(sum(truncatables))