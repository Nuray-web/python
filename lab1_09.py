#09 

n = int(input("Please enter the number of elements: ")) 

a = [int(n) for n in input("Please enter some integers: ").split()]  

b = a[n-1] 

for i in range(n - 1, 0, -1):  

    a[i] = a[i - 1]    

a[0] = b   

print(*a) 
