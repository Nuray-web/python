#794
n, m, k = map(int, input("Please, enter the number of your badges: ").split())
r = m//k
w = min(k-1, m)
allof = (r+w)*n
print(allof)
