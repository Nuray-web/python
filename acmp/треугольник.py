#606
x, y, z = map(int, input("Please enter your values: ").split())
if x+y >= z and x+z >= y and y+z >= x:
  print("YES")
else:
  print("NO")
