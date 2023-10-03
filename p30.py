#!/usr/bin/env python3
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

matches = []

for i in range(2, 1000000):
	if i == sum([int(x)**5 for x in str(i)]):
		matches.append(i)

print(sum(matches))