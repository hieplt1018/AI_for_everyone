from PIL import Image

im = Image.open("img/Sydney-Opera-House.jpg") #Đọc ảnh
print(im.format, im.size, im.mode) #in ra thuộc tính của ảnh
# format: loại file ảnh, size: tuple chứa chiều rộng và cao, mode: RGB- dạng ảnh màu/grayscale
im.show() #Hiển thị ảnh

img = im.convert("L") #chuyển ảnh về dạng grayscale
out = im.resize((128,128)) #định dang lại kích thước ảnh
out = im.rotate(45) #xoay ảnh
out.show()
