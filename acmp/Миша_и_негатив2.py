#715
n,m = map(int,input("Please, enter the stats of the photo: ").split())
a = []
b = []
count = 0
#изначальная версия
for i in range(n):
    s = str(input("Please, enter your line: "))
    a.append([])
    for j in range(len(s)):
        a[i].append(s[j])
print(*a)
      
#версия программы Миши
for i in range(n):
    s = str(input("Please, enter your line: "))
    b.append([])
    for j in range(m):
        b[i].append(s[j])
print(*b)

for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1

print(count)
