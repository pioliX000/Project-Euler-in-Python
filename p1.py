#!/usr/bin/env python3
# Find the sum of all the multiples of 3 or 5 below 1000.

nums =[]

for i in range(1, 1000):
	if i not in nums:
		if i % 3 == 0:
			nums.append(i)
	if i not in nums:
		if i % 5 == 0:
			nums.append(i)

print(sum(nums))