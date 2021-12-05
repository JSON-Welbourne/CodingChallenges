# Problem #214
# Easy Expressions
# Find the value of the following summation
# 10^12
#   ∑ (x2+x+1)∗x!
#  x=1
# x! denotes factorial of x.
# Give your answer modulo 3^20

import math
m = 3 ** 20

def f(x):
	return (x**2 + x + 1) * math.factorial(x)

def s(x):
	sum = 0
	for i in range(1,x+1):
		sum += f(i)
	return sum

for i in range(1000):
	print("{}: {}".format(i,s(i)%m))
