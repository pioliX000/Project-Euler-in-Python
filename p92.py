#!/usr/bin/env python3

# A number chain is created by continuously adding the square of the digits
# in a number to form a new number until it has been seen before.
# How many starting numbers below ten million will arrive at 89?

res = []

for i in range(10_000_000):
	seen = []
	current = []

	temp_i = i

	while temp_i not in seen:
		seen.append(temp_i)
		temp_i = sum([int(x)**2 for x in str(temp_i)])

		if temp_i == 89:
			res.append(i)
			break

print(len(res))

Solution to Project Euler problem 92
Copyright (c) Project Nayuki. All rights reserved.

https://www.nayuki.io/page/project-euler-solutions
https://github.com/nayuki/Project-Euler-solutions
