#4
a = list(map(int, input("Please enter the elements of list: ").split()))
n = int(input("Please enter Petya's height: "))
a.append(n)
a.sort(reverse = True)
i = a.index(n)
print(i+1)
