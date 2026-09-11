def portal(arr_list, m):
    a = 0 # 첫 포인트 잡기
    answer = 0
    b = [] # visit 포인트 저장하는 list
    while True:
        if a == m-1: # 마지막 포탈에 도달시 return answer
            return answer
        elif arr_list[a] == 0: # 항상 0에 시작할 때마다 a와 answer 1씩 올리기
            a = a + 1
            answer = answer +1
        elif arr_list[a] != 0 and a not in b: #한 번도 방문을 안할 때에는 해당 지점 저장후, 해당 포탈보다 1 적은 곳으로 이동하기
            b.append(a)
            a = arr_list.index(arr_list[a] - 1)
            answer += 1
        elif arr_list[a] != 0 and a in b: # 한 번 방문했을 때에는 a와 answer 1씩만 올리기
            a = a + 1
            answer += 1

N = int(input()) # 예제 입력 받기
for i in range(1,N+1):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f"#{i} {portal(arr,n)}")