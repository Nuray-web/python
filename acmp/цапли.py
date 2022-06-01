#850
a, b = map(int, input("Please, enter the number of Petya and Masha: ").split())
maxa = a
mina = a//2
maxb = b
minb = b//2
print(max(mina, minb), min(maxa, maxb))
