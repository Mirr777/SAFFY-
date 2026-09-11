def farming(arr, a, b):





T = int(input())
for tc in range(1,T+1):
    a, b = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(a)]
    print(f"#{tc} {farming(arr,a,b)}")