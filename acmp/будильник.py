#777
a, b = map(int, input("Please, enter your values: ").split())
#a - лег спать
#b - установил будильник
if b>a:
  print(b-a)
else:
  print(12-a+b)
