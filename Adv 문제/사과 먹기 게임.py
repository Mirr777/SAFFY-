def find_apple(arr,n,m): # 사과 위치 찾는 함수
    for i in range(n):
        for j in range(n):
            if arr[i][j] == m:
                return (i,j)

def apple(arr,n):
    mode = 1
    point = (0, 0)
    answer = 0
    for i in range(1,12):
        if find_apple(arr,n,i) is None:
            return answer
        else:
            if mode == 1: # 로봇이 오른쪽을 바라볼 때 사과의 위치에 따라 횟수 더하고 로봇 방향 바꾸기
                if find_apple(arr,n,i)[0] == point[0] and find_apple(arr,n,i)[1] > point[1]:
                    point = find_apple(arr,n,i)
                elif find_apple(arr,n,i)[0] > point[0] and find_apple(arr,n,i)[1] >= point[1]:
                    answer += 1
                    point = find_apple(arr,n,i)
                    mode = 2
                elif find_apple(arr,n,i)[0] >= point[0] and find_apple(arr,n,i)[1] < point[1]:
                    answer += 2
                    point = find_apple(arr,n,i)
                    mode = 3
                else:
                    answer += 3
                    point = find_apple(arr,n,i)
                    mode = 4
            elif mode == 2: # 로봇이 아래를 바라볼 떄 사과의 위치에 따라 횟수 더하고 로봇 방향 바꾸기
                if find_apple(arr,n,i)[1] == point[1] and find_apple(arr,n,i)[0] > point[0]:
                    point = find_apple(arr,n,i)
                elif find_apple(arr,n,i)[1] < point[1] and find_apple(arr,n,i)[0] >= point[0]:
                    answer += 1
                    point = find_apple(arr,n,i)
                    mode = 3
                elif find_apple(arr,n,i)[1] <= point[1] and find_apple(arr,n,i)[0] < point[0]:
                    answer += 2
                    point = find_apple(arr,n,i)
                    mode =4
                else:
                    answer += 3
                    point = find_apple(arr,n,i)
                    mode = 1
            elif mode == 3: #로봇이 왼쪽를 바라볼 떄 사과의 위치에 따라 횟수 더하고 로봇 방향 바꾸기
                if find_apple(arr,n,i)[0] == point[0] and find_apple(arr,n,i)[1] < point[1]:
                    point = find_apple(arr,n,i)
                elif find_apple(arr,n,i)[0] < point[0] and find_apple(arr,n,i)[1] <= point[1]:
                    answer += 1
                    point = find_apple(arr,n,i)
                    mode = 4
                elif find_apple(arr,n,i)[0] <= point[0] and find_apple(arr,n,i)[1] > point[1]:
                    answer += 2
                    point = find_apple(arr,n,i)
                    mode = 1
                else:
                    answer += 3
                    point = find_apple(arr,n,i)
                    mode = 2
            elif mode == 4: #로봇이 위를 바라볼 떄 사과의 위치에 따라 횟수 더하고 로봇 방향 바꾸기
                if find_apple(arr,n,i)[1] == point[1] and find_apple(arr,n,i)[0] < point[0]:
                    point = find_apple(arr,n,i)
                elif find_apple(arr,n,i)[1] > point[1] and find_apple(arr,n,i)[0] <= point[0]:
                    answer += 1
                    point = find_apple(arr,n,i)
                    mode = 1
                elif find_apple(arr,n,i)[1] >= point[1] and find_apple(arr,n,i)[0] > point[0]:
                    answer += 2
                    point = find_apple(arr,n,i)
                    mode = 2
                else:
                    answer += 3
                    point = find_apple(arr,n,i)
                    mode = 3

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    print(f"#{tc} {apple(arr,n)}")