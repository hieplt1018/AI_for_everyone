#Phương sai (variance): Đánh giá mức độ phân tán của dữ liệu so với giá trị trung bình

def cal_mean(nums):
  s = sum(nums)
  n = len(nums)
  mean = s/n
  return mean

def cal_variance(nums):
  mean = cal_mean(nums)

  diff = []
  for num in nums:
    diff.append(num-mean)

  square_diff = []
  for d in diff:
    square_diff.append(d**2)
    sum_square_diff = sum(square_diff)

  variance = sum_square_diff/len(nums)
  return variance

point = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
print("Variance: ", cal_variance(point))
print("Độ lệch chuẩn: ", cal_variance(point)**0.5)
