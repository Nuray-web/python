#327
k = int(input("Please, enter the number of tests: "))
for i in range(k):
    s = str(input("Please, enter the number of the ticket: "))
    a = int(s[0])+int(s[1])+int(s[2])
    b = int(s[3])+int(s[4])
    c = int(s[5])+1
    d = int(s[5])-1
    if b + c == a:
        print("Yes")
    elif b + d == a:
        print("Yes")
    else:
        print("No")
