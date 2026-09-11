def waiting(N):
    N.sort()
    n = len(N)
    answer = 0
    for i in range(n):
        answer += (n-i-1) * N[i]
    return answer
N = list(map(int,input().split()))

print(waiting(N))
