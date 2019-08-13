import numpy as np

#Tạo 1 numpy array 1 chiều
a = np.array([1,2,3])

print(type(a)) #class numpy.array
print(a.shape) #kich thuoc mang a
print(a[0], a[1], a[2])

a[1] = 7
print(a)

b = np.array([[1,2,3], [4,5,6]])
print(b.shape) #kich thuoc mang b (2,3)

#tao 1 mang 2 chieu kieu unsigned in 8 bit
width = 300
height = 200
img = np.zeros((width, height), np.uint8)
print(img)
