# Problem #34
# Jewish Factorials
# Find in how many ways can we write 100! as a sum of two or more consecutive positive numbers.
# Give the answer mod(1000000009)

import math
number = math.factorial(100)
modulo = 10**9+1

def sumBetween(a,b):
  return int((b*(b+1)//2) - (a*(a-1)//2))

for i in range(2,number):
  for j in range(10):
    print("{}: {}".format(
      i,
      sumBetween((number//i)+j,(number//i)+j+(i-1)) ))
  

