file_path = 'W3/Iris.csv'
file_handle = open(file_path, 'r')

lines = file_handle.readlines()
data_list = []

for i in range(1, len(lines)):
  data = lines[i].split(',')

  sepal_length = float(data[1].strip())
  sepal_width = float(data[2].strip())
  pedal_length = float(data[3].strip())
  pedal_width = float(data[4].strip())

  species = 0
  if data[5].strip() == 'Iris-versicolor':
    species = 1
  elif data[5].strip() == 'Iris-virginica':
    species = 2

  data_list.append([sepal_length, sepal_width, pedal_length, pedal_width, species])
file_handle.close()

def cal_mean(data):
  s = sum(data)
  l = len(data)
  mean = s/l
  return mean

def cal_standard_deviation(nums):
  mean = cal_mean(nums)

  diff = []
  for num in nums:
    diff.append(num-mean)

  square_diff = []
  for d in diff:
    square_diff.append(d**2)
    sum_square_diff = sum(square_diff)

  variance = sum_square_diff/len(nums)
  standard_deviation = variance ** 0.5
  return standard_deviation

def get_col(data, nums_col):
  col_data = []
  for i in range(1, len(data)):
    col_data.append(data[i][nums_col])
  return col_data

def get_number_each_species(speciec_num, data):
  sum = 0
  for i in range(1, len(data)):
    if(data[i][4]) == speciec_num:
      sum += 1
  return sum

# print(data_list[50])
# print(type(data_list[50]))
# print(data_list[50][1])
col_data = get_col(data_list, 1)
print(col_data[50])
print('Min sepal_length: ', min(col_data))
print('Max sepal_length: ', max(col_data))
print('Mean sepal_length: ', cal_mean(col_data))
print('Standard Deviation sepal_length: ', cal_standard_deviation(col_data))
print('Numbers of Iris-versicolor flower: ', get_number_each_species(1, data_list))
