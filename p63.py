#!/usr/bin/env python3
# How many b-digit positive integers exist which are also an nth power?

nums = []

for i in range(1,10):
	for x in range(1, 25):
		if len(str(i**x)) == x:
			nums.append(i)

print(len(nums))