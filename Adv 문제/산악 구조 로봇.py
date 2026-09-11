def mountain(arr, turnel, a, b):


    return

T = int(input())
for tc in range(1,T+1):
    a, b = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(a)]
    turnel = [list(map(int,input().split())) for _ in range(b)]
    print(f"#{tc} {arr,turnel,a,b}")