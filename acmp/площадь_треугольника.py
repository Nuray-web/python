x1, y1, x2, y2, x3, y3 = map(int, input("Please enter the values: ").split())

a = x1 - x3
b = x2 - x3
c = y1 - y3
d = y2 - y3

S = (a*c - b*d) / 2
if S<0:
    print(-S)

print(S)
