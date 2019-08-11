import matplotlib.pyplot as plt
import numpy as np

x = np.arange (-8, 10, 0.97)
y = x ** 3

plt.title('Hàm y = x^3') #Đặt tên cho figure
plt.xlabel('Trục x') #Đặt tên cho trục x
plt.ylabel('Trục y') #Đặt tên cho trục y

plt.grid() #Vẽ biểu đồ dưới dạng lưới

plt.plot(x, y, label='y=x^3') #vẽ đồ thị với giá trị trục x so với trục y
plt.legend() #hiển thị chú thích cho đồ thị
plt.show()

#Vẽ nhiều hình trên 1 figure
#plt(nrows,ncols,plot_number)
plt.subplot(1, 2, 1) # 1 dòng, 2 cột, vị trí 1
plt.plot(x, y, 'red')

plt.subplot(1, 2, 2)
plt.plot(x, y, 'green')

plt.show()

fig = plt.figure() #Khởi tạo figure trống
plt.show()

fig = plt.figure()
fig.add_subplot(111)

ax = fig.add_axes([0, 0.5, 0.5, 0.5], facecolor='#BECDAF')
ax.plot(x, y, 'red')
ax.set_title('Hình 1') #Đặt tên cho axes
ax.set_xlabel('Trục x') #Đặt tên cho trục x
ax.set_ylabel('Trục y') #Đặt tên cho trục y

ax2 = fig.add_axes([0.5, -0.1, 0.5, 0.5], facecolor='#BECDAF')
x = np.linspace(0, 2, 100)
ax2.plot(x, x, label='linear')
ax2.plot(x, x**2, label='quadratic')
ax2.plot(x, x**3, label='cubic')
#Tạo thêm 1 linear cungf figure
ax2.set_xlabel('Trục x')
ax2.set_ylabel('Trục y')
ax2.set_title('Hình thứ 2')
ax2.legend()

plt.show()

# Khởi tạo nhanh Figure và Axes -> plt.subplots()
fig, ax = plt.subplots(figsize=(10,5))

x = np.linspace(0, 2, 100)
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')

ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')
ax.set_title('Hình thứ 2')
ax.legend()

plt.show()

# Lưu figure cùng thư mục với code
fig.savefig('img/my_figure.png')

import matplotlib.image as mpimg

# Hiển thị hình ảnh lưu trong máy
plt.imshow(mpimg.imread('img/my_figure.png'))

# Chỉnh lại trục toạ độ

fig, ax = plt.subplots(figsize=(10,6))
x = np.arange(-10., 10., 0.2)
y = np.sin(x)

# Biến đường biên bên trên và bên phải -> vô hình
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Di chuyển đường bên dưới vào giữa  & ở vị trí y = 0
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

# Di chuyển đường bên trái vào giữa & ở vị trí x = 0
ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# Hoặc thay ('data', 0) thành 'center'
ax.spines['left'].set_position('center')

ax.plot(x, y)
plt.show()

#Vẽ đồ thị kiểu điểm
t = np.arange(0., 10., 0.5)

plt.plot(t, t**2, 'X')
plt.show()

#Vẽ mmột vài điểm trên đường
x = [1, 2, 3, 5]
y = [4, 5, 6, 7]

plt.plot(x, y, linestyle='--', marker='o', color='b')

# Một cách ngắn hơn
plt.plot(x, y, '--bo')
plt.show()

#hoặc

x = np.linspace(-np.pi, np.pi, 30)
y = np.sin(x)
markers_on = [0, 19, 12, 5]
plt.plot(x, y, '-gD', markevery=markers_on)
plt.show()
