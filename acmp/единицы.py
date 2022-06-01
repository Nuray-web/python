#022
n = int(input("Please, enter the value of the decimal number: "))
c = 0
while n>0:
  if n%2 == 1:
    n = n//2
    c += 1
  else:
    n = n//2
print(c)
