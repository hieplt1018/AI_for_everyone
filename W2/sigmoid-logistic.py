import math
def sigmoid_fuc(data):
  result = []
  for d in data:
    result.append(1/(1+math.exp(-d)))
  return result

sigmoid_fuc([1,5,-4,3,-2])
