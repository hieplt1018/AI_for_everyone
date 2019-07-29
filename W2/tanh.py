import math

def tanh_fuc(data):
  result = []
  for d in data:
    result.append((2/(1+math.exp(-2*d)))-1)
  return result

tanh_fuc([1,5,-4,3,-2])

# x thuoc R, y thuoc [-1,1]
