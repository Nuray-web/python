#678
s = str(input("Please enter your chess square position: "))
a = 1
b = 0
c = 0
for i in range(0, len(s), 1):
    if s[i] == 'A':
        a, b = b, a
    if s[i] == 'B':
        b, c = c, b
    if s[i] == 'C':
        a, c = c, a
if a == 1:
    print('1')
elif b == 1:
    print('2')
else:
    print('3')
