#simple stereo matching using pixel-wise
import numpy as np
from PIL import Image
import os

def stereo_matching(left_img, right_img, disparity_range):
  # đọc ảnh trái phải rồi chuyển sang dạng grayscale
  left_img = Image.open(left_img).convert('L')
  left = np.asarray(left_img)

  right_img = Image.open(right_img).convert('L')
  right = np.asarray(right_img)

  #chiều rộng và chiều cao ảnh cho trước
  height = 288
  width = 384

  # tạo disparity map
  depth = np.zeros((height,width), np.uint8)
  scale = 255/ disparity_range

  for y in range(height):
    for x in range(width):
      #tìm j tại đó cost có giá trị min
      disparity = 0
      cost_min = (int(left[y, x]) - int(right[y,x]))**2

      for j in range(1, disparity_range):
        cost = 255**2 if (x-j) < 0 else (int(left[y, x]) - int(right[y,x-j]))**2

        if cost < cost_min:
          cost_min = cost
          disparity = j

          #đã tìm được j (lưu ở biến disparity) để cost min
          #gán j vào disparity map
          # nhân cho scale để nhìn thấy rõ ràng
          depth[y,x] = disparity * scale

  #chuyển dữ liệu từ nparray sang kiểu Image và lưu xuống file
  Image.fromarray(depth).save('../img/Tsukuba/disparity_map_pixel.png')

if __name__ == '__main__':
  disparity_range = 16 # cho cặp ảnh Tsukuba
  print(os.getcwd())
  check1 = os.path.exists("../img/Tsukuba/left.png")
  print(check1)
  stereo_matching("../img/Tsukuba/left.png", "../img/Tsukuba/right.png", disparity_range)
