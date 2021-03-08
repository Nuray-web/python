#817
n, m, d, k = map(int, input("Please, enter your values: ").split())
res = ((n + m) * d * k) - (d * d * n * m)
print(res)
