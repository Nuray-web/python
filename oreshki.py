#766
n = int(input("Введите количество шишек: "))
m = int(input("Введите количество орешков: "))
k = int(input("Введите количество орешков, нужное белке на зиму: "))
res = n*m
if res > k:
    print("YES")
elif res == k:
    print("YES")
else:
    print("NO")
