#!/usr/bin/env python3
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# PARTIALLY CHATGPT GENERATED CODE (modified)

repeaters = {}

def find_repeating_part(numerator, denominator):
	k = 1
	while True:
		candidate = 10**k - 1
		if candidate % denominator == 0:
			repeating_part = (candidate // denominator) * numerator
			return repeating_part
		elif k > denominator:
			return None  # No repeating part found, it's a terminating decimal
		k += 1

# Example usage:
numerator = 1
for denominator in range(1, 1000):
	repeating_part = find_repeating_part(numerator, denominator)
	if repeating_part is not None:
		repeaters[denominator] = repeating_part

print(max(repeaters, key=repeaters.get))