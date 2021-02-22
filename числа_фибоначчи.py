#844
n = int(input("Please, enter the num of element in Fibonacci sequence: "))
a = 0
b = 1
if n == 0:
  print(a)
elif n == 1:
  print(b)
else:
  for i in range(2, n+1):
    b = a+b
    a = b-a
  print(b)
