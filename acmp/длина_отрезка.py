#529
import math
x1, y1, x2, y2 = map(int, input("Please, enter your values: ").split())
ab = (x2-x1)**2 + (y2-y1)**2
print(int(math.sqrt(ab)))
