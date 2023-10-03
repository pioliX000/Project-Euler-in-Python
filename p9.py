#!/usr/bin/env python3
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for x in range(1, 1000):
	for y in range(1, 1000): 
		z = 1000 - x - y
		if x < y < z and x**2 + y**2 == z**2:
			if x + y + z==1000:
				print(x * y * z)
				break
