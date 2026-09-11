def fly(arr_list, m, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    dz = [1, 1, -1, -1]
    dw = [1, -1, -1, 1]
    answer1 = 0
    answer2 = 0
    max_answer1 = 0
    max_answer2 = 0
    for i in range(m): # 십자가 모양 스프레이
        for j in range(m):
            answer1 = arr_list[i][j]
            for k in range(1,n):
                for l in range(4):
                    if 0 <= i+dy[l]*k <= m-1 and 0 <= j+dx[l]*k <= m-1:
                        answer1 += arr_list[i+dy[l]*k][j+dx[l]*k]
            max_answer1 = max(answer1, max_answer1)
    for i in range(m): #대각선 모양 스프레이
        for j in range(m):
            answer2 = arr_list[i][j]
            for k in range(1, n):
                for l in range(4):
                    if 0 <= i + dz[l] * k <= m - 1 and 0 <= j + dw[l] * k <= m - 1:
                        answer2 += arr_list[i + dz[l] * k][j + dw[l] * k]

            max_answer2 = max(answer2, max_answer2)
    return max(max_answer1, max_answer2)

N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    arr = []
    for j in range(a):
        arr.append(list(map(int,input().split())))
    print(f"#{i+1} {fly(arr,a,b)}")
