
arr = [["_"]*5 for i in range(4)]
dx = [-1, -1, -1 , 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(2):
    x, y = map(int,input().split())
    for i in range(8):
        if 0 <= y+dy[i] <= 3 and 0 <= x+dx[i] <= 4:
            arr[y+dy[i]][x+dx[i]] = "#"
for i in range(4):
    print(*arr[i])