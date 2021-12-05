# Problem #13
# Pandigital Primes
# A number is said to be pandigital if it contains each of the digits from 0 to 9 (and whose leading digit must be nonzero).
# Find the smallest pandigital prime number.

import primefac
s = 1234567890

def possibleStrings(strings,characters):
  if len(characters) == 0:
    return strings
  else:
    newStrings = []
    for i in range(len(characters)):
      newStrings = newStrings + possibleStrings([s+characters[i] for s in strings],characters[:i]+characters[i+1:])
    return newStrings

def smallestPandigitalPrime(n):
  lowest = None
  for i in range(len(str(n))+1):
    ps = [
      p for p in [
        int(p) for p in possibleStrings([''],str(n) + (str(n)[i-1] if i > 0 else '')) 
        if p[0] != '0'] 
      if primefac.isprime(p)]
    if len(ps) > 0 and (lowest == None or min(ps) < lowest):
      lowest = min(ps)
      print("{}: {}".format(i,lowest))
    else:
      print(i)
  return lowest

smallestPandigitalPrime(s)
