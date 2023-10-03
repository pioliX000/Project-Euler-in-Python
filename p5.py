#!/usr/bin/env python3
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

for i in range(1, 1_000_000_000):
	for x in check_list:
		if i % x == 0:
			if x == 20:
				print(i)
			continue
		else:
			break