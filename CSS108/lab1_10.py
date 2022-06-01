#10
n = int(input("Please enter the number of elements: "))
a = [int(n) for n in input("Please enter some integers: ").split()] 
a.reverse()
print(*a)
