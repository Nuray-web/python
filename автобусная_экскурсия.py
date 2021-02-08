#233
a = []
n = int(input("Пожалуйста, введите количество мосты: "))
for i in range(n):
    a.append(int(input()))
c = a[i]
if c > 437:
  print("NO CRASH")
  i += 1
else:
  print("CRASH", a.index(c))
