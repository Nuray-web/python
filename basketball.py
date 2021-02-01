#61
print("Please, enter the points first team got: ")
l = []
a = int(input())
l.append(a)
b = int(input())
l.append(b)
c = int(input())
l.append(c)
d = int(input())
l.append(d)

print("Please, enter the points second team got: ")
s = []
e = int(input())
s.append(e)
f = int(input())
s.append(f)
g = int(input())
s.append(g)
h = int(input())
s.append(h)

i = a+b+c+d
j = e+f+g+h
if i>j:
    print("Won: 1")
elif i<j:
    print("Won: 2")
else:
    print("DRAW")
