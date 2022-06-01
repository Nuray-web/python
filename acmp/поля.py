#844
import math
a, b = map(int, input("Please, enter the stats of your rectangle: ").split())
S = a*b
c = math.sqrt(S)
if c - int(c) == 0:
  print(int(math.sqrt(S)))
else:
  print('0')
