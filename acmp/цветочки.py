n = int(input())
s = ['G', 'C', 'V']
for i in range(n):
    s[2], s[1] = s[1], s[2]
    s[0], s[1] = s[1], s[0]
print(s[0]+s[1]+s[2])
