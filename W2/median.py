def calculate_median(numbers):
  l = len(numbers)
  numbers.sort()
  if l % 2 == 0:
    m1 = l/2
    m2 = l/2 + 1
    m1 = int(m1) - 1
    m2 = int(m2) - 1
    median = (numbers[m1] + numbers[m2])/2
  else:
    m = int((l+1)/2)
    median = numbers[m]
  return median

donations = [100,200,40,322222,4000,123330,44030]
calculate_median(donations)
