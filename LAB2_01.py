#1
s = str(input("Please enter your string: "))
print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])
print(s[0::2])
for i in range(len(s)):
    if i%2 == 1:
        print(s[i], end = '')
print("\n" + s[::-1])
a = s[0::2]
print(a[::-1])
print(len(s))
