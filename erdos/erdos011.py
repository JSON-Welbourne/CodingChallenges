# Problem #11
# Factorial
# Find 1000000008!
# Give the answer modulo 1000000009.

import math

def factmod(n):
  return math.factorial(n) % (n+1)

def main():
  for i in range(100):
    print("{}: {}".format(
      i,
      factmod(i)))

main()
