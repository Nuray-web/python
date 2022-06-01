#023 
n = int(input("Please enter the number: ")) 
a = 0 
for i in range(1, n+1): 
    if n %i == 0: 
        a += i 
print(a) 
