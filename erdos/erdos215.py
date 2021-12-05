# Problem 215
# Go for Gold
# Sparky is yet again being accused of being a robot. He needs to solve this question to prove his innocence.
# Given a number x and has defined the following functions:
# p(x)=x!
# s(x)=1+2+3+...+x
# Find the value of p(x) mod s(x) for x=109+6
# Hint: 10^9+7 is a prime number
import math

def p(x):
	return math.factorial(x)

def s(x):
	return int(x*(x+1)/2)

def f(x):
	vp = p(x)
	vs = s(x)
	return [vp,vs,vp%vs]

for i in range(1,1000):
	l = f(i)
	print("i: {}, p: {}, s: {}: p%s: {}".format(i,str(l[0])[:50],l[1],l[2]))
