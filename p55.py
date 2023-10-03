#!/usr/bin/env python3
# How many Lychrel numbers are there below ten-thousand?

lychrel = [] 

def next_num(a):
	return a + int(str(a)[::-1])

for i in range(1, 10000):
	orig_i = i
	for x in range(1, 51):
		if next_num(i) != int(str(next_num(i))[::-1]):
			i = next_num(i)
		else:
			break

		if x >= 50:
			lychrel.append(orig_i)

print(len(lychrel))