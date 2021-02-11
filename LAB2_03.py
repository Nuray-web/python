#3
a = list(map(int, input("Please enter the elements of list: ").split()))
l = len(a)
for i in range(1, l):
    if a[i] > a[i-1]:
        print(a[i], end=' ')
