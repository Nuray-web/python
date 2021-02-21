#263
n, i, j = map(int, input("Please, enter your nums: ").split())
if i>j:
    i,j = j,i
a = j-i-1
b = n-j+i-1
print(min(a,b))
