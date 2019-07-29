import math
#change degree to radian
degree = float(input("Input your degree: "))
radian = degree * (math.pi / 180)
print(radian)

#change radian to degree
radian2 = float(input("Input your radian: "))
degree = (radian2 * 180) / math.pi
print(degree)

#check right-angled triangle
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
answer = not bool(((a**2+b**2-c**2) * (a**2+c**2-b**2) * (c**2+b**2-a**2)))
print("This triangle is right-angled?", answer)

#change C temp to F temp
temp_c = float(input("Input C temp:"))
temp_f = temp_c * (9/5) + 32
print(temp_f)

#change F temp to C temp
temp_f = float(input("Input F temp:"))
temp_c = (temp_f - 32) / (9/5) 
print(temp_f)