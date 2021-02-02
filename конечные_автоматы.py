#035
k = int(input("Please enter your value: "))
#k - количество автоматов
#kol - регулировка количества автоматов для лупа (НЕ УБИРАТЬ)
kol = 0
d = 0
while kol < k:
  n, m = map(int, input("Please enter the n and m values: ").split())
  d = 19*m + (n + 239)*(n + 366)//2
  print(d)
  kol += 1 #прибавляет значение для кола, чтобы луп не был вечным
