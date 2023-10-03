#!/usr/bin/env python3
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = 0
sundays = 0
days_done = 0

for x in range(1900, 2000):
	for y in range(1, 13):
		if y in (1, 3, 5, 7, 8, 10, 12):
			days = 31
		elif y in (4, 6, 9, 11):
			days = 30
		elif x % 4 == 0 or x % 400 == 0:
			days = 29
		else:
			days = 28

		if days_done % 7 == 0:
			sundays += 1

		days_done += days
		
print(sundays)	

