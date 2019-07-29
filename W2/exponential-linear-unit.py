import math
def exponential_linear_unit(data):
  result = []
  for d in data:
    if d < 0:
      result.append(0.1*(math.exp(d)-1))
    else:
      result.append(d)
  return result

exponential_linear_unit([1,5,-4,3,2])
