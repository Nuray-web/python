all = [] 
#1000000003 
for i in range(0, 1000000003): 
  if i%3==0: 
    if i%10 != 4 and i%10 != 7: 
      all.append(i) 
    else: 
      pass 
print(sum(all))
