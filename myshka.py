#907
w = int(input("Please enter the width value: "))
h = int(input("Please enter the height value: "))
r = int(input("Please enter the radius value: "))
Sr = w*h
Sc = r*r*3.14
if Sr<Sc:
    print("NO")
elif Sr == Sc:
    print("YES")
else:
    print("NO")
