import math
 
list_2 = []
list_1 = []
answer = []
result = []
N = int(input())
for i in range(N):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(T+1)]
    list_1 = []
    for i in range(T+1):
        for j in range(T+1):
            if arr[i][j] == 2:
                list_2 = [i,j]
            elif arr[i][j] == 1:
                list_1.append([i,j])
    answer = []
    for i in list_1:
        answer.append(abs(i[0]-list_2[0])**2 + abs(i[1] - list_2[1])**2)
    result.append(math.ceil(math.sqrt(max(answer))))

 
 
for idx, ele in enumerate(result):
    print(f"#{idx+1} {ele}")
