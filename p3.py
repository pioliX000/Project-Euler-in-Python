#!/usr/bin/env python3
# What is the largest prime factor of the number 600851475143?

i = 2
number = 600851475143

while number > 1:
	if number % i == 0:
		number /= i
	print(number)
	else:
		i += 1

print(i)
