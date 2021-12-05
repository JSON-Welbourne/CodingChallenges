import primefac
import timeit
maximumQty = 123456789123456789
maximumRoot = int(maximumQty ** (1/3)) + 2

def f(n):
	return int(n * (n+1) / 2)

def main(n):
	debug = False
	sum = f(n)
	if debug: print("Adding All Integers: {}".format(sum))
	maximumRoot = int(n ** (1/3)) + 2
	for i in [i for i in range(2,maximumRoot+1) if primefac.isprime(i)]:
		if debug: print("Removing Multiples of {}".format(i**3))
		sum -= (i ** 3) * f(n // (i ** 3))
		if i > 2:
			for j in [j for j in range(2,i) if primefac.isprime(j)]:
				if debug: print("Adding Multiples of {}".format((i*j)**3))
				sum += ((i*j) ** 3) * f(n // ((i*j) ** 3))
	return sum

for i in [10,10**2,10**3,10**4,10**5,10**9,10**10,123456789,1234567891,12345678912,123456789123,123456789123456789]:
	starttime = timeit.default_timer()
	main(i)
	print("{} : {}".format(i,timeit.default_timer() - starttime))
