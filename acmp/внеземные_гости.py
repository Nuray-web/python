#597
r1 = int(input("Please enter the radius of field: "))
r2 = int(input("Please enter the radius of plate: "))
r3 = int(input("Please enter the radius of plate: "))
Sc1 = r1*r1*3.14
Sc2 = r2*r2*3.14
Sc3 = r3*r3*3.14
if Sc2+Sc3 < Sc1:
    print("YES")
elif Sc2+Sc3 == Sc1:
    print("YES")
else:
    print("NO")
