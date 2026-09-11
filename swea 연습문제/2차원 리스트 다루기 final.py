arr =[]
for i in range(5):
    arr.append(list(map(int,input().split())))

answer = 0
max_val = float("-inf")
min_val = float("inf")
answer_2 = 0

for i in range(5):
    for j in range(5):
        if arr[i][j] == 2:
            answer += 1
        if arr[i][j] > max_val:
            max_val = arr[i][j]
        if arr[i][j] < min_val:
            min_val = arr[i][j]
        if i == j:
            answer_2 += arr[i][j]

print(answer)
print(max_val, min_val)
print(answer_2)