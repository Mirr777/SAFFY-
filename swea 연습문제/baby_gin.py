
arr = list(map(int,input().split()))

N = max(arr)
arr_list = [0] * (N+1)
answer = 0


for i in arr:
    arr_list[i] += 1

for i in range(N+1):
    if arr_list[i] >= 3:
        answer += 1
        arr_list[i] -= 3

for j in range(N-1):
    if arr_list[j] == 1 and arr_list[j+1] == 1 and arr_list[j+2] == 1:
        answer += 1
        arr_list[j] -= 1
        arr_list[j+1] -= 1
        arr_list[j+2] -= 1
if answer == 2:
    print("Yes")
else:
    print("No")