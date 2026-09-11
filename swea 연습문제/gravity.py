def gravity(arr_list, a):
    max_value = 0
    answer = 0
    for i in range(a-1): #최댓값 직전까지 범위로 i 값 설정
        answer = 0 #낙차 값 초기화
        for j in range(i+1, a): # i값보다 하나 큰 값에서부터 최댓값까지 범위로 j 값 설정
            if arr_list[i] > arr_list[j]: # 같은 블럭이 없으므로 해당 조건일 때 낙차가 1씩 생김
                answer += 1
        if max_value < answer: #기존 값보다 낙차가 클 경우 정답 바뀜
            max_value = answer


    return max_value

N = int(input()) # 입력 예제
for i in range(N):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f"#{i+1} {gravity(arr,n)}")

