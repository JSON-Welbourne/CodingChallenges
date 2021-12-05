#	Ricket Numbers
#
#	Rick is working on an important mission but Beth has asked him to look after Morty. Rick doesn't want to be disturbed so he wants to keep Morty busy. He knows how much Morty loves challenges and how much he hates numbers, so he asks Morty to "help" him by counting all the rickety numbers upto 12345678.
#
#	A number N is said to be Ricket if and only if it is composite and there exists a way to permute all its divisors (except 1) onto a circle
#	such that the GCD of any two adjacent elements is greater than 1.
#	Contributed by Anmol Agarwal
#	Solved by 46 users

import primefac
import math

def mulPerm(l):
	if all([i > 1 for i in gcdList(l)]):
		print("{}{}".format("SUCCESS",l))
		return l 
	elif len(l) < 2:
		print("{}{}".format("FAIL   ",l))
		return l
	else:
		for i in range(len(l)):
			output = mulPerm([l[0]*l[i]] + l[1:i] +l[i+1:])
			if all([i2 > 1 for i2 in gcdList(output)]):
				print("{}{}".format("SUCCESS",output))
				return output
		print("{}{}".format("FAIL   ",l))
		return l

def gcdList(l):
	return [math.gcd(l[i],l[(i+1)%len(l)]) for i in range(len(l))]

count = 0
for i in range(1,12345678):
	f = [l for l in primefac.primefac(i)]
	if len(f) > 1:
		if len(list(set(f))) < len(f):
			print("{}: {}".format(i,f))
			count += 1

print(count)

# Notes:
#	What does permute mean?
#	It seems initially that the only number list permutations that meet these criteria are numbers with only 
#	one prime factor repeated multiple times
#	16 = 2x2x2x2
#	for example
#		if len(f) > 1 and len(list(set(f))) == 1: # There is only one factor repeated multiple times
#	603
#		if lef(f) > 1 and len(list(set(f))) < len(f): # First part is unneccesary, There was atleast one factor eliminated
#	4840391
#	Since neither of those worked, now I am thinking permute means multiplying combinations of factors to produce a ring 
#	meeting the criteria
#	[2,2,2,3,3,3] => [2,6,3,6]
#		distribution = {v: len([True for v2 in f if v2 == v]) for v in f}
#