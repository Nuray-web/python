#81
a = []
n = int(input("Пожалуйста, введите количество арбузов: "))
for i in range(n):
    a.append(int(input()))

mini = a[0]
maxi = a[0]

for i in range(n):
  if a[i] < mini:
    mini = a[i]
  if a[i] > maxi:
    maxi = a[i]

print(mini, maxi)
