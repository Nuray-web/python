#943
n, m, y, x = map(int, input("Please, enter the values for matrix: ").split())
a = (y-1)*m + (x-1)
if y%2 == 1:
    print(a)
a = y*m - x
if y%2 == 0:
    print(a)
