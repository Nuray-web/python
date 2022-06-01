#324
s = str(input("Please enter your 4-bit num: "))
list(s)
if s[0] == s[3] and s[1] == s[2]:
  print("YES")
else:
  print("NO")
