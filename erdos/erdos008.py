# Problem #8
# Summation of Primes
# Find the sum of digits of all prime numbers below 10^9.

import primefac
max = 9

def sumDigits(n):
  return sum([int(c) for c in str(n)])

def sumDigitsOfPrimes(n):
  return sum([sumDigits(i) for i in range(n+1) if primefac.isprime(i)])

def main():
  print("i  10^i sumDigits(10^i)  sumDigitsOfPrimes(10^i)")
  for i in range(max+1):
    print("{}, {}, {}, {}".format(
      i,
      10**i,
      sumDigits(10**i),
      sumDigitsOfPrimes(10**i)))

main()
