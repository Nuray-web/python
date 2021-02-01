#755
x = int(input("Маша сорвала ягод: "))
y = int(input("Миша сорвал ягод: "))
z = int(input("Количество ягод, что они съели: "))
a = (x+y)-z
if a>0:
    print("Количество оставшихся ягод: " + str(a))
else:
    print("Impossible")
