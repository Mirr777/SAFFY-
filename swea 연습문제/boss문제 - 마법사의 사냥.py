def wizard(arr_list, a, b):
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    answer = 0
    max_answer = 0
    for i in range(a):
        for j in range(a):
            answer = 0
            for k in range(1, b+1):
                for x in range(4):
                    if 0 <= i+dy[x]*k <= N-1 and 0 <= j+dx[x]*k <= N-1:
                        answer += arr_list[i+dy[x]*k][j+dx[x]*k]
            max_answer = max(answer, max_answer)
    return max_answer

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
M = int(input())
print(f"{wizard(arr,N,M)}")