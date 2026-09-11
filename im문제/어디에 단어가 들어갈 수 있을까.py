def findword(arr_list, n, m):
    answer = 0
    count = 0
    for i in range(n):
        answer = 0  # 줄이 바뀔 경우 answer 초기화
        for j in range(n):
            if arr_list[i][j] == 1:  #흰색바탕일 때 값 하나씩 늘리기
                answer += 1
            elif arr_list[i][j] == 0: #검은색 바탕일 때 이전 길이가 주어진 길이와 같다면 개수 추가
                if answer == m:
                    count +=1
                answer = 0
        if answer ==m: # 줄이 바뀔 경우 이전 값이 주어진 값과 같다면 count 올리기
            count += 1

    for i in range(n): # 이번에는 세로줄 찾기
        answer = 0  # 줄이 바뀔 경우 answer 초기화
        for j in range(n):
            if arr_list[j][i] == 1:  #흰색바탕일 때 값 하나씩 늘리기
                answer += 1
            elif arr_list[j][i] == 0: #검은색 바탕일 때 이전 길이가 주어진 길이와 같다면 개수 추가
                if answer == m:
                    count +=1
                answer = 0
        if answer == m: # 줄이 바뀔 경우 이전 값이 주어진 값과 같다면 count 올리기
            count += 1

    return count

N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    arr = []
    for _ in range(a):
        arr.append(list(map(int,input().split())))
    print(f"#{i+1} {findword(arr, a, b)}")