from collections import Counter

point = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6,1, 10, 6, 6]

def calculate_mode(nums):
  c = Counter(nums)
  nums_feq = c.most_common()
  max_count = nums_feq[0][1]
  modes = []
  for feq in nums_feq:
    if feq[1] == max_count:
      modes.append(feq[0])
    else:
      break
  return modes

print('Modes point: ', calculate_mode(point))
