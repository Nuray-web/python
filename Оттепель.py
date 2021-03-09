#264
n = int(input("Please, enter the given period: "))
a = [int(n) for n in input("Please, enter the results: ").split()]
temp = 0
count = 0
for i in range(n):
    if a[i]>0:
        temp += 1
    else:
        temp = 0
    if temp > count:
        temp = count
print(count)
