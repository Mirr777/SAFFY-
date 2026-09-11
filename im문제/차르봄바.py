def bomb(bomb_list, m, n):
    answer = 0
    max_answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(m):
        for j in range(m):
            answer = bomb_list[i][j] #중앙을 포함하므로 해당 지역 값 미리 설정해두기
            for k in range(1,n+1): # 1부터 n범위까지 설정
                for l in range(4): # dx, dy 길이가 4이므로 4번 돌리기
                    if 0 <= i+dx[l]*k <= m-1 and 0 <= j+dy[l]*k <= m-1: #리스트 밖 범위를 벗어나는 것 제외시키기
                        answer += bomb_list[i+dx[l]*k][j+dy[l]*k] #폭탄 범위 내 값들 모두 더하기
            max_answer = max(max_answer,answer) # 최대값 구하기
    return max_answer

N = int(input()) # 입력 예제 받기
for _ in range(N):
    a, b = map(int,input().split())
    arr = []
    for u in range(a):
        arr.append(list(map(int,input().split())))
    print(f"#{_+1} {bomb(arr,a,b)}")
