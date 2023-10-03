#!/usr/bin/env python3
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

x = 0
y = 1

for i in range(1, 100000):
	z = x + y
	x = y
	y = z

	if len(str(x)) == 1000:
		print(i)
		break 