#21
a = int(input("Введите значение зарплаты первого работника: "))
b = int(input("Введите значение зарплаты второго работника: "))
c = int(input("Введите значение зарплаты третьего работника: "))

if (a<b) and (a<c):
    if (b<c):
        print("Их разница равна "+ str(c-a))
    else:
        print("Их разница равна "+ str(b-a))
if (b<a) and (b<c):
    if(a<c):
        print("Их разница равна "+ str(c-b))
    else:
        print("Их разница равна "+ str(a-b))
if (c<a) and (c<b):
    if (a<b):
        print("Их разница равна "+ str(b-c))
    else:
        print("Их разница равна "+ str(a-c))
if (a==c) and (a==b):
    print ("Их разница равна 0")
