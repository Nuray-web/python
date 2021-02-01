#106
#1 - решка, 0 - герб
n = int(input("Введите количество монеток: "))
pos = list(map(int,input("Какой расклад монет: ").split()))
a = 0
b = 0
for i in range(1, n):
    c = pos[i]
    if c == 0:
        a += 1
    else:
        b += 1
if a < b:
    print(a)
else:
    print(b)
