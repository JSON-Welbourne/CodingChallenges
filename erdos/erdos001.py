# Problem #1
# Minimum Value
# Let there be a set of N natural numbers 1,2,3,4...N. 
# We are allowed to insert + or − sign in front of each number and add all the resultant numbers. 
# The minimum non-­negative value obtained is denoted as D(N).
# Find the value of D(1)+D(2)+...+D(19216812112)

def D(n):
  return min([
    sum([i if "{0:b}".format(j).zfill(n)[i-1] == '1' else -i  for i in range(1,n+1)]) 
    for j in range(2**n) 
    if sum([i if "{0:b}".format(j).zfill(n)[i-1] == '1' else -i  for i in range(1,n+1)]) > -1])

def s(n):
  return sum([D(i) for i in range(n+1)])

def main():
  for i in range(1,1000):
    print("{}, {}, {}".format(i,D(i),s(i)))

main()
