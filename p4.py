#!/usr/bin/env python3
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []

for x in range(100, 1000):
	for y in range(100, 1000):
		if x*y == int(str(x*y)[::-1]):
			palindromes.append(x*y)

print(max(palindromes))
