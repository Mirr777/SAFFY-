arr = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x = 2
y = 1
answer = 0
for i in range(4):
    answer += arr[y+dy[i]][x+dx[i]]
print(answer)