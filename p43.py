#!/usr/bin/env python3
# Consider d to be a 0-9 pandigital number (i.e. 1234567890) and dₙ to be the digit
# d₂d₃d₄ % 2; d₃d₄d₅ % 3; d₄d₅d₆ % 5; d₅d₆d₇ % 7; d₆d₇d₈ % 11; d₇d₈d₉ % 13; d₈d₉d₁₀ % 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

primes = [2,3,5,7,11,13,17]
passed = False
permutations = [x for x in permutations("1234567890") if x[0] !=0]
ans = []

for i in permutations:
	for y in range(1,8):
		if int(i[y]+i[y+1]+i[y+2]) % primes[y-1] == 0:
			passed = True
		else:
			passed = False
			break
	if passed:
		ans.append(int("".join(i)))
	else:
		continue

print(sum(ans))