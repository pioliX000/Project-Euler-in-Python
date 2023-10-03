#!/usr/bin/env python3
# tₙ = 1/2n(n+1)
# a 16K text file containing nearly two-thousand common English words, how many are triangle words?

f = open("p42_words.txt", "r")

summ = 0
words = eval(f.read())
triangles = []
count = 0

for n in range(100):
	triangle = 1/2*n*(n+1)
	triangles.append(int(triangle))

for word in words:
	for char in word.lower():
		summ += ord(char) - 96 

	if summ in triangles:
		count += 1
	summ = 0

print(count)