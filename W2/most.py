from collections import Counter

point = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
def calculate_mode(nums):
  c = Counter(nums)
  mode = c.most_common(1)
  return mode[0][0]

print('Mode point: ', calculate_mode(point))
