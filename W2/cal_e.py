import math

def factorial(n):
  factorial = 1
  for i in range(1, n+1):
    factorial *= i
  return factorial

def cal_e(n):
  e = 1
  for i in range(1, n+1):
    e += 1/factorial(i)
  return e

cal_e(10)
