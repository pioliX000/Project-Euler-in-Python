#!/usr/bin/env python3
# What is the largest 1 to 9 pandigital 9-digit number that can 
# be formed as the concatenated product of an integer with (1, 2..., n) where n > 1?

def is_pandigital(x):
	return len(set(x)) == len(x) and len(x) == 9 and "0" not in x

pandigitals = []
num = ""

for i in range(1, 10000):
	for n in range(1, 10000):
		num += str(i*n)
		if len(num) >= 9:
			if is_pandigital(num):
				pandigitals.append(num)
				num = ""
				break
			else:
				num = ""
				break
	else:
		continue

print(max(pandigitals))