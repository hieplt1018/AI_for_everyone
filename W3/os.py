import os

#os.getcwd() trả về thư mục hiện hành
print(os.getcwd())

#os.path.join() nối string
print(os.path.join('/images/', 'img1.png'))

#split() tách path và filename
pathname = '/home/hieplt/Documents/MachineLearning/AI_for_everyone/os.py'
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)
