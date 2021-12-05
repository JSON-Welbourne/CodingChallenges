#	Problem #30
#	Respect My Authoritah!
#	The wizard Cartman decides to color a torus with colors. Let the minimum number of colors required to color the n-holed torus be m(n). 
#	He has a cube of iron. He asks the blacksmith token to cut it (as in a laser plane is passing through the cube) n times. 
#	Let the number of different parts of the cube generated be x(n). 
#	But he loves to work with prime numbers and so wants x(n)−k and x(n)+k to be prime. 
#	Let the smallest k required to accomplish it be f(n). 
#	Your task is to find out ∑15n=2[(m(n)∗f(n))]n
import math
import primefac

def m(n):
	return math.floor((7+((1+48*n)**(1/2)))/2)

def x(n):
	return 2**n

def f(n):
	searching = True
	xv = x(n)
	k = 0
	while searching:
		if primefac.isprime(xv + k) and primefac.isprime(xv - k):
			searching = False
		else:
			k += 1
	return k

sum = 0
for i in range(2,16):
	xv = x(i)
	mv = m(i)
	fv = f(i)
	element = (mv * fv) ** i
	sum += element
	print("{}: ( {} {} {} ) {} += {}".format(i,mv,xv,fv,element,sum))
