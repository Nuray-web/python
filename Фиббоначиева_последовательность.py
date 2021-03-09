#949
n,an1,an2 = map(int, input("Please, enter the coefficients: ").split())
an0 = 0
if n == 1:
    print(an1, an2)
while n>1:
    an0 = an2-an1
    an2 = an1
    an1 = an0
    n-=1
print(an0, an1)
