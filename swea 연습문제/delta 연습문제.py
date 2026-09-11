N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += arr[i][i]
    ans += arr[i][N-i-1]
ans -= arr[N//2][N//2]
if N % 2:
    print(ans)