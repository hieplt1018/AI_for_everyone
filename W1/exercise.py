#example build-in func in math module
import math
#ceil(x) trả về số nguyên nhỏ nhất lớn hơn hoặc bằng x
ceil_ex = math.ceil(3.2)
print(ceil_ex)
print(type(ceil_ex))

#copysign(x,y) trả về  giá trị của x với dấu của y
copysign_ex1 = math.copysign(1.2, -3)
print(copysign_ex1)
print(type(copysign_ex1))

copysign_ex2 = math.copysign(- 1.2, 3)
print(copysign_ex2)
print(type(copysign_ex2))

#factorial(x) trả về giai thừa của x
factorial_ex1 = math.factorial(5)
print(factorial_ex1)
print(type(factorial_ex1))

#floor(x) trả về giá trị nguyên lớn nhất nhỏ hơn hoặc bằng x
floor_ex1 = math.floor(-4.5)
print(floor_ex1)
print(type(floor_ex1))

#fmod(x,y) trả về phần dư của phép chia số thực x/y
fmod_ex1 = math.fmod(3.4, 0.5) #tuong duong 34 % 5
print(fmod_ex1)
print(type(fmod_ex1))

#frexp(x) trả về phần định trị (mantissa) và số mũ của x dưới dạng (m, e) sao cho x == m*2**e
frexp_ex1 = math.frexp(20)
print(frexp_ex1)
print(type(frexp_ex1))

#fsum(iterable) trả về tổng của 1 mảng
arr = [1.1, 4, 6] 
print(math.fsum(arr)) 
print(type(math.fsum(arr)))

#gcd(x, y) trả về UCLN 
print(math.gcd(60, 48))
print(type(math.gcd(60, 48)))

#isclose(a, b, rel_tol = 1e-09, abs_tol 0.0) trả về true nếu x = y +- abs_tol
print(math.isclose(2.005, 2.125, abs_tol = 0.25)) 
print(math.isclose(2.547, 2.0048, abs_tol = 0.5)) 
print(math.isclose(2.005, 2.005)) #abs = 0
print(math.isclose(2.005, 2.004)) 

