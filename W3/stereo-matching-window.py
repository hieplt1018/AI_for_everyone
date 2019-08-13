#simple stereo matching using pixel-wise
import numpy as np
from PIL import Image
import os

def stereo_matching(left_img, right_img, kernel_size, disparity_range):
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

  kernel_half = int((kernel_size-1)/2)
  scale = 255 / disparity_range

  for y in range(kernel_half, height-kernel_half):
    print(".", end=" ")
    for x in range(kernel_half, width-kernel_half):
      #tìm j tại đó cost có giá trị min
      disparity = 0
      cost_min = 65534

      for j in range(disparity_range):
        ssd = 0
        ssd_temp = 0

        for v in range(-kernel_half, kernel_half):
          for u in range(-kernel_half, kernel_half):
            ssd_temp = 255 ** 2
            if (x+u-j) >= 0:
              ssd_temp = (int(left[y+v, x+u]) - int(right[y+v, (x+u) - j]))**2
            ssd += ssd_temp
        if ssd < cost_min:
          cost_min = ssd
          disparity = j

          #đã tìm được j (lưu ở biến disparity) để cost min
          #gán j vào disparity map
          # nhân cho scale để nhìn thấy rõ ràng
          depth[y,x] = disparity * scale

  #chuyển dữ liệu từ nparray sang kiểu Image và lưu xuống file
  Image.fromarray(depth).save('../img/Tsukuba/disparity_map.png')

if __name__ == '__main__':
  disparity_range = 16 # cho cặp ảnh Tsukuba
  print(os.getcwd())
  check1 = os.path.exists("../img/Tsukuba/left.png")
  print(check1)
  kernel_size = 5
  stereo_matching("../img/Tsukuba/left.png", "../img/Tsukuba/right.png", kernel_size, disparity_range)
