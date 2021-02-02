#685
a = list(map(int, input("Please enter your values: ").split()))
a.sort()
b = list(map(int, input("Please enter your values: ").split()))
b.sort()
print(a[2]*b[2]+a[1]*b[1]+a[0]*b[0])
