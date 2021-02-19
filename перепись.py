n = int(input("Please, enter the number of the dweller: "))

for i in range(n):
  v, s = map(int, input("Please enter their age and gender: ").split())

old = 0
ind = -1

for i in range(1, n+1):
  if s == 1 and v > old:
    old, ind = v, i+1
print(ind)
