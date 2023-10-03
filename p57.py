#!/usr/bin/env python3
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

nums = []
numer = 0
denom = 1

for i in range(1000):
	numer, denom = denom, denom * 2 + numer

	if len(str(numer + denom)) > len(str(denom)):
		nums.append((numer + denom)/denom)

print(len(nums))

