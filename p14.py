#!/usr/bin/env python3
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n →→ 3n+1 (n is odd)
# Which starting number, under one million, produces the longest chain?

count = 0
nums = {}

for i in range(1, 1000000):
	x = i
	while i != 1:
		if i % 2 == 0:
			i = i/2
		elif i % 2 != 0:
			i = 3*i+1

		count += 1	

	nums[str(x)] = count
	count = 0

print(max(nums, key=nums.get))