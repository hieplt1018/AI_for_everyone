import glob

#Lấy tất cả path cho các file có đuôi là py
list_of_path = glob.glob('W3/*.py')
print(list_of_path)
