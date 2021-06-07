#106
#1 - решка, 0 - герб
n = int(input())
pos = []
for i in range(n):
   pos.append(int(input()))
a = 0
b = 0
for i in range(n):
   if pos[i] == 0:
      a += 1
   else:
      b += 1
print(min(a,b))
