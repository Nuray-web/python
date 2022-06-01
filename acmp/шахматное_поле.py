#935
x1, y1, x2, y2 = map(int, input("Please, enter the stats: ").split())
if x1 == 1 or x1 == 3 or x1 == 5 or x1 == 7:
    if int(y1)%2 == 1:
        a = 'b'
    elif y1 == 1:
        a = 'b'
    else:
        a = 'w'
else:
    if int(y1)%2 == 1:
        a = 'w'
    elif y1 == 1:
        a = 'w'
    else:
        a = 'b'  
if x2 == 1 or x2 == 3 or x2 == 5 or x2 == 7:
    if int(y2)%2 == 1:
        b = 'b'
    elif y2 == 1:
        b = 'b'
    else:
        b = 'w'
else:
    if int(y2)%2 == 1:
        b = 'w'
    elif y2 == 1:
        b = 'w'
    else:
        b = 'b'  
if a == b:
  print('yes')
else:
  print("no")
