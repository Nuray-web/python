#62
s = str(input("Please enter your chess square position: "))
if s[0] == 'A' or s[0] == 'C' or s[0] == 'E' or s[0] == 'G':
    if int(s[1])%2 == 1:
        print("Black")
    else:
        print("White")
else:
    print("White")
