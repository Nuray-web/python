#754
m1 = int(input("Введите массу первого толстяка: "))
m2 = int(input("Введите массу второго толстяка: "))
m3= int(input("Введите массу третьего толстяка: "))

if 94 > m1 or 94 > m2 or 94 > m3 or 727 < m1 or 727 < m2 or 727 <m3 :
   print("Error")
elif m1 > m2 and m1 >  m3:
   print(m1)
elif m2 > m1 and m2 > m3:
   print(m2)
elif m3 > m1 and m3 > m2:
   print(m3)
else:
   print(m1)
