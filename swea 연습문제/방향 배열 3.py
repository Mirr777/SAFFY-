a, b = map(int, input().split())

arr = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]
dx = [0, 1, 1, -1, -1]
dy = [0, 1, -1, 1, -1]

answer = 1

for i in range(5):
    if 0 <= b+dy[i] <=4 and 0 <= a + dx[i] <= 4:
        answer *= arr[b+dy[i]][a+dx[i]]
print(answer)