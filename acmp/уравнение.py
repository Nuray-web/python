#010
a,b,c,d = map(int, input("Please, enter the coefficients: ").split())
for i in range(-100,100):
    if a*i*i*i + b*i*i + c*i + d == 0:
        print(i, end = ' ')
