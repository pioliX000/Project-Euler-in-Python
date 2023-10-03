#!/usr/bin/env python3
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

nums = []

a = 0
b = 1

while sum(nums) < 4000000:
	z = a + b
	a = b
	b = z

	if a % 2 == 0:
		nums.append(a)
		
print(sum(nums))