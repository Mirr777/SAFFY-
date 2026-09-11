def fo(arr, N): #초기 포의 위치 찾는 함수
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return (x,y)

def kill(arr, N, a, b): # 포가 쫄을 잡아 먹는 함수
    answer1 = 0
    answer2 = 0
    answer3 = 0
    answer4 = 0
    answer = 0
    for y in range(N):
        if y > b:
            if arr[y][a] == 1:
                answer1 += 1
        else:
            if arr[y][a] == 1:
                answer2 += 1
    if answer1 >= 2:
        answer += 1
    if answer2 >= 2:
        answer += 1
    for x in range(N):
        if x > a:
            if arr[b][x] == 1:
                answer3 += 1
        else:
            if arr[b][x] == 1:
                answer4 += 1
    if answer3 >= 2:
        answer += 1
    if answer4 >= 2:
        answer += 1
    return answer

def route(arr, N, a, b): # 포가 움직일 수 있는 위치 찾는 함수
    space = []
    answer1 = 0
    for y in range(b,-1,-1):
        if arr[y][a] == 1:
                answer1 += 1
        elif arr[y][a] == 0 and answer1 == 1:
            space.append([a,y])
    answer1 = 0
    for y in range(b+1,N):
        if arr[y][a] == 1:
            answer1 += 1
        elif arr[y][a] == 0 and answer1 == 1:
            space.append([a, y])
    answer1 = 0
    for x in range(a,-1 , -1):
        if arr[b][x] == 1:
            answer1 += 1
        elif arr[b][x] == 0 and answer1 == 1:
            space.append([x, b])
    answer1 = 0
    for x in range(a+1, N):
        if arr[b][x] == 1:
            answer1 += 1
        elif arr[b][x] == 0 and answer1 == 1:
            space.append([x, b])
    return space

def go(arr, N):
    a = fo(arr, N)[0]
    b = fo(arr, N)[1]
    answer = kill(arr, N, a, b)
    c = 0
    d = 0
    for j in range(len(route(arr, N, a, b))):
        c = route(arr,N,a,b)[j][0]
        d = route(arr,N,a,b)[j][1]
        print(answer)
        answer += kill(arr, N, c, d)
    for k in range(len(route(arr,N,c,d))):
        e = route(arr, N, c, d)[k][0]
        f = route(arr, N, c, d)[k][1]
        print(answer)
        answer += kill(arr, N, e, f)
    return answer



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f"#{tc} {go(arr,N)}")