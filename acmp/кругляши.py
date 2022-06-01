#297
s = str(input("Please, enter your number: "))
c = 0
for i in range(len(s)):
    if s[i] == '0' or s[i] == '6' or s[i] == '9':
        c+=1
    elif s[i] == '8':
        c+=2
print(c)
