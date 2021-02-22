#637
n = int(input("Please, enter the num of universities: "))
a = [int(n) for n in input("Please, enter how many teams arrived: ").split()]
k = int(input("Please, enter how many rooms we got: "))
summ = 0
for i in range(n):
  summ += min(k, a[i])
print(summ)
