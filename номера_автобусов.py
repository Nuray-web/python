#691
n = int(input("Please, enter the number of the bus sign: "))
for i in range(n):
    s = str(input("Please, enter the sign of the bus: "))
    sh = 'ABCEHKMOPTXY'
    if len(s) != 6:
        print("No")
    if s[1] < '0' or s[1]>'9':
        if s[2] < '0' or s[2]>'9': 
          if s[3] < '0' or s[3]>'9':
           print("No")
    if sh.find(s[0]) != -1:
        if sh.find(s[4]) != -1:
          if sh.find(s[5]) != -1:
            print("Yes")
          else:
            print("No")
        else:
          print("No")
    else:
      print("No")
