#!/usr/bin/env python3
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

print(int("".join([str(i) for i in [x for x in permutations("0123456789")][999999]])))