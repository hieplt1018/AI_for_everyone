import random
import math

def cal_Pi(n):
  n_t = 0
  for _ in range(n):
    num_x = random.random()*2 - 1;
    num_y = random.random()*2 - 1;
    #round equaltion: (x-a)**2 + (y-b)**2 = R**2
    if math.sqrt((num_x) ** 2 + (num_y) ** 2) <= 1 :
      n_t += 1;
  return 4 * (n_t/n)

cal_Pi(100000)
