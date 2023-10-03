#!/usr/bin/env python3
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

temp = []
temp2 = []

for i in range(1, 100000000):
	for x in range(1, 7):
		temp.append([int(y) for y in str(i*x)])

	for s in temp:
		temp2.append(sorted(s))

	if all(c == temp2[0] for c in temp2):
		print(i)
		break

	temp = []
	temp2 = []
