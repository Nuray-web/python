#818
a = []
n = int(input("Пожалуйста, введите количество розеток: "))
for i in range(n):
    a.append(int(input("Пожалуйста, введите ваше значение: ")))
b = sum(a)
print("Максимальное число чайников: ", b - n + 1)
