a,b,c = list(map(int, input().split()))
print(max(max(a,b),c) - min(min(a,b),c))
