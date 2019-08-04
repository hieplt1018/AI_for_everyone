#Correlation coeffient: Hệ số tương quan tuyến tính
import numpy as np
from PIL import Image
from io import BytesIO
import requests

def cal_corr(x,y):
  n = len(x)
  prod = []
  for xi,yi in zip(x,y):
    prod.append(xi*yi)
  print(prod)

  sum_prod = sum(prod)
  sum_x = sum(x)
  sum_y = sum(y)

  square_sum_x = sum(x)**2
  square_sum_y = sum(y)**2

  square_x = []
  for xi in x:
    square_x.append(xi**2)
  x_square_sum = sum(square_x)

  square_y = []
  for yi in y:
    square_y.append(yi**2)
  y_square_sum = sum(square_y)

  numerator = n*sum_prod-sum_x*sum_y
  denominator_term1 = (n*x_square_sum-square_sum_x)**0.5
  denominator_term2 = (n*y_square_sum-square_sum_y)**0.5
  corr = numerator/(denominator_term1*denominator_term2)
  return corr

req1 = requests.get('https://www.dropbox.com/s/vfe090qo24t3v46/img1.png?raw=1')
req2 = requests.get('https://www.dropbox.com/s/vtz8ik7mb1e1is7/img2.png?raw=1')
req3 = requests.get('https://www.dropbox.com/s/auxezlf6ijoejwo/img3.png?raw=1')
req4 = requests.get('https://www.dropbox.com/s/w5oc29l57f77arp/img4.png?raw=1')

image1 = Image.open(BytesIO(req1.content))
image2 = Image.open(BytesIO(req2.content))
image3 = Image.open(BytesIO(req3.content))
image4 = Image.open(BytesIO(req4.content))

image1_list = np.asarray(image1).flatten().tolist()
image2_list = np.asarray(image2).flatten().tolist()
image3_list = np.asarray(image3).flatten().tolist()
image4_list = np.asarray(image4).flatten().tolist()

print(cal_corr(image1_list,image2_list))
print(cal_corr(image1_list,image3_list))
print(cal_corr(image1_list,image4_list))
