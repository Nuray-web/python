#148
a, b = map(int, input("Please enter your Natural numbers: ").split())
i = a
nod = 0
while i>0:
    if a%i == 0 and b%i ==0:
        nod = i
        break
    i -= 1
print(nod)
