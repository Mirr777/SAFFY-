arr = []
for _ in range(4):
    arr.append(list(map(int,input().split())))

for i in range(4):
    for j in range(4):
        print(arr[3-i][3-j], end = " ")
    print()