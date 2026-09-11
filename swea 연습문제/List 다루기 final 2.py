arr = []
a, b = map(int,input().split())
for i in range(3):
    arr.append(a)
for j in range(2):
    arr.append(b)
for k in range(3):
    arr.append(a+b)
print(*arr)