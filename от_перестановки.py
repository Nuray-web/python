#907
a = int(input("Please enter the value: "))
b = int(input("Please enter the value: "))
c = int(input("Please enter the value: "))
if a+b == c:
    print("YES")
elif a+c == b:
    print("YES")
elif b+c == a:
    print("YES")
else:
    print("NO")
