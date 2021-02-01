#892
n = int(input("Please enter the number of season: "))
if n == 1 or n == 2 or n == 12:
    print("WINTER")
elif n == 3 or n == 4 or n == 5:
    print("SPRING")
elif n == 6 or n == 7 or n == 8:
    print("SUMMER")
elif n == 9 or n == 10 or n == 11:
    print("AUTUMN")
else:
    print("ERROR")
