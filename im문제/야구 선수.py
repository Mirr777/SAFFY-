def baseball(arr_list, m, n):
    answer = 0
    max_answer = 0
    for i in range(m):
        answer = 0
        for j in range(m):
            if arr_list[i] <= arr_list[j] <= arr_list[i] + n:
                answer += 1
        max_answer = max(max_answer, answer) # 모아진 팀 중 최댓값 구하기

    return max_answer

N = int(input()) # 입력 예제 받기
for i in range(N):
    a, b = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f"#{i+1} {baseball(arr, a, b)}")