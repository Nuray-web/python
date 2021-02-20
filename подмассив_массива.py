#284
n = int(input("Please, enter the number of elements in array: "))
a = [int(n) for n in input("Please enter some integers: ").split()] 
m = int(input("Please, enter the number of subarrays: "))
while m>0:
    m -= 1
    j, k = map(int, input("Please, enter elements: ").split())
    for i in range(j-1, k):
      print(a[i], end = ' ')
    print('')
