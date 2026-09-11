def mountain(arr_list, m):
    answer = 0
    max_answer = 0
    min_list = float("inf")
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    inf_list = [[float("inf")]*(m+2) for _ in range(m+2)]
    for a in range(1, m+1): # 테두리면 무한으로 설정해서 최솟값 찾기 편하게 만들기
        for b in range(1, m+1):
            inf_list[a][b] = arr_list[a-1][b-1]

    for i in range(1, m+1):
        for j in range(1, m+1):
            answer = 1
            a = i # i와 j를 쓸 경우 오류가 나기에 while 문 밖에서 a와 b 변수 설정
            b = j
            while True:
                min_list = min(inf_list[a][b], inf_list[a+1][b], inf_list[a-1][b], inf_list[a][b+1], inf_list[a][b-1])
                if inf_list[a][b] == min_list: #최솟값이 어디 있는지 찾은 후 최솟값 위치에 따라 설정하기
                    break
                elif inf_list[a+1][b] == min_list:
                    a = a+1
                    answer += 1
                elif inf_list[a-1][b] == min_list:
                    a = a-1
                    answer += 1
                elif inf_list[a][b+1] == min_list:
                    b = b+1
                    answer += 1
                elif inf_list[a][b-1] == min_list:
                    b = b-1
                    answer += 1
            max_answer = max(answer, max_answer) #가장 긴 등산로 찾기
    return max_answer

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {mountain(arr,N)}")
