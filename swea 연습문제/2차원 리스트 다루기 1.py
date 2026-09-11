arr = [[0]* 4 for _ in range(4)]

arr[0][0] = 7
arr[1][3] = 1
arr[2][1] = 3
arr[3][3] = 9

for x in arr:
    print(*x)