#!/usr/bin/env python
# Consider quadratic Diophantine equations of the form: 
# x² - Dy² = 1
# Find the value of D <= 1000 in minimal solutions of for which the largest value of is obtained.

import sympy

x = sympy.Symbol('x')
eq2 = 1

for D in range(1, 1000):
	for y in range(1, 1000):
		eq1 = x**2-D*y**2
		print(sympy.solve(sympy.Eq(eq1, eq2)))