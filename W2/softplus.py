import math

def soft_plus(data):
  result = []
  for d in data:
    result.append(math.log(1+math.exp(d)))
  return result

soft_plus([1,5,-4,3,2])
