#496
n = int(input("Please, enter the value: "))
a = [int(n) for n in input("Please, enter the results: ").split()]
s = [a[i-2] + a[i-1] + a[i] for i in range(n)]
print(max(s))
