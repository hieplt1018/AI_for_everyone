file_path = 'W3/helloworld.txt'
file_handle = open(file_path, 'w')

text1 = 'Hihi \n'
file_handle.write(text1)

text2 = 'Lucky to you \n'
file_handle.write(text2)

file_handle.close()
