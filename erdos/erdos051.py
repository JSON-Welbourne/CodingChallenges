# Problem #51
# Probability of Squares
# Two numbers are chosen at random from 1 to 10^16.
# Let p be the probability that their sum is a perfect square. 
# Find integral part of 10^16∗p.

import math

def squaresBetween(a,b):
  return math.floor(b**(1/2)) - math.floor((a-1)**(1/2))

def probabilityOfSquares(minI,maxI,slices):
  if slices == 1:
    return squaresBetween(minI,maxI) / (maxI - minI + 1)
  elif slices == 2:
    return sum([
     ((2 * i) - 1) * squaresBetween(i**2+minI,i**2+maxI) 
     for i in range(minI,maxI+1)]) / ((maxI - minI + 1) ** 2)
    return len([i+j for i in range(minI,maxI+1) for j in range(minI,maxI+1) if (i+j)**(1/2) == int((i+j)**(1/2))])/((maxI-minI+1) ** 2)
    
