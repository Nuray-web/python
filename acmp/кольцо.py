#894
import math
s, r1 = map(float, input("Please, enter the values for matrix: ").split())
a = math.pi * (r1**2) - s
r2 = math.sqrt(a/math.pi)
print(r2)
