a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
e,f = list(map(int,input().split()))
g,h = list(map(int,input().split()))
if (a+c+e+g)>(b+d+f+h):
    print(1)
elif (a+c+e+g)<(b+d+f+h):
    print(2)
else:
    print("DRAW")
