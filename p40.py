#!/usr/bin/env python3
# 0.123456789101112131415161718192021
# If d represents the nth digit of the fractional part, find the value of the following expression. 
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

fraction = "0."
num = 1
temp = 1
for i in range(1, 200000):
	fraction += str(i)

for x in range(1, 8):
	num *= int(fraction[temp+1])
	temp *= 10

print(num)	
