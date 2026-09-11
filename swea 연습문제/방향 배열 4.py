x, y = map(int, input().split())

arr = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]
dx = [-1, 1, 0, 1]
dy = [0, 0, 1, 1]

answer = 0
max_answer = 0
for i in range(4):
    if 0 <= y+dy[i] <=3 and 0 <= x+dx[i] <= 4:
        answer = arr[y+dy[i]][x+dx[i]]
        max_answer = max(max_answer, answer)
print(max_answer)