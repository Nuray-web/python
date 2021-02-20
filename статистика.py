#005
n = int(input("Please, enter the number of days: "))
a = [int(n) for n in input("Please, enter the days in one line: ").split()]
nechet = 0
chet = 0
ne = []
c = []
for i in a:
    d = i
    if d%2 == 1:
        ne.append(d)
        nechet += 1
    else:
        c.append(d)
        chet += 1
    i -= 1
print(*ne)
print(*c)
if nechet > chet:
    print("No")
elif nechet<chet:
    print("Yes")
else:
    print("Error")
