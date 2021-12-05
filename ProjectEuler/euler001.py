import itertools

def product(l):
  output = 1
  for i in l:
    output *= i
  return output

def sumMultiple(n,m):
  return m * (((n-1)//m) * (((n-1)/m)+1) // 2)

def sumIncluding(n,inclusions):
  output = 0
  for i in range(1,len(inclusions)+1):
    print("i:         {}".format(i))
    print("direction: {}".format(((-1)**(i+1))))
    print("divisors:  {}".format([product(s) for s in list(itertools.combinations(inclusions,i))]))
    print("multi:     {}".format([sumMultiple(n,j) for j in [product(s) for s in list(itertools.combinations(inclusions,i))]]))
    for j in [product(s) for s in list(itertools.combinations(inclusions,i))]:
      print("j          {}".format(j))
      print("sum        {}".format(sum([sumMultiple(n,j) for j in [product(s) for s in list(itertools.combinations(inclusions,i))]])))  
    output += (
      ((-1) ** (i+1)) * 
      ((len(list(itertools.combinations(inclusions,i-1))) - 1) if i > 1 else 1) * 
      sum([
        sumMultiple(n,j) 
        for j in [
          product(s) 
          for s in list(
            itertools.combinations(
              inclusions,
              i)
          )
        ]
      ])
    )
  return int(output)

sumIncluding(1000,[3,5])

    
