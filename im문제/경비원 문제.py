def black_people(arr_list, n):
    police = []
    answer = n*n -1  # 경비원을 제외한 개수
    for i in range(n):
        for j in range(n):
            if arr_list[i][j] == 2:  # 경비원 위치 찾기
                police = [i,j]
            elif arr_list[i][j] == 1: # 벽 개수 찾기
                answer -= 1
    a = police[0] # 오른쪽 포인트 변수 설정
    b = police[1] # 아래쪽 포인트 변수 설정
    c = police[0] # 왼쪽 포인트 변수 설정
    d = police[1] # 위쪽 포인트 변수 설정
    while True: 
        if (a + 1 == n or arr_list[a+1][police[1]] == 1) and (b + 1 == n or arr_list[police[0]][b+1] == 1) and (c-1 == -1 or arr_list[c-1][police[1]] == 1) and (d-1 == -1 or arr_list[police[0]][d-1] == 1):
            break # 모든 포인터가 끝에 도달하거나 벽을 만나면 break
        elif (a+1) != n and arr_list[a+1][police[1]] == 0:
            answer -= 1 # 경비원 기준 오른쪽에 벽이나 끝이 아니면 숨을 곳 사라짐
            a = a+1
        elif (b+1) != n and arr_list[police[0]][b+1] == 0: 
            answer -= 1 # 경비원 기준 아래쪽에 벽이나 끝이 아니면 숨을 곳 사라짐
            b = b+1
        elif (c-1) != -1 and arr_list[c-1][police[1]] == 0: 
            answer -= 1 # 경비원 기준 왼쪽에 벽이나 끝이 아니면 숨을 곳 사라짐
            c = c-1
        elif (d-1) != -1 and arr_list[police[0]][d-1] == 0:
            answer -= 1 # 경비원 기준 위쪽에 벽이나 끝이 아니면 숨을 곳 사라짐
            d = d-1
        else:
            break
    return answer

N = int(input()) # 입력 예제 받기
for i in range(N):
    a = int(input())
    arr = []
    for j in range(a):
        arr.append(list(map(int,input().split())))
    print(f"#{i+1} {black_people(arr,a)}")