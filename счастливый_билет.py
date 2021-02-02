#52
n = str(input("Please enter your number: "))
a = list(n)
print(a)
b = int(a[0])+int(a[1])+int(a[2])
c = int(a[3])+int(a[4])+int(a[5])
if b == c:
  print("YES")
else:
  print("NO")
