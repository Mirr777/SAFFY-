N = int(input())
def change(N):
    answer = 0
    while True:
        if N >= 500:
            answer += N//500
            N = N % 500
        elif N >= 100:
            answer += N // 100
            N = N % 100
        elif N >= 50:
            answer += N // 50
            N = N % 50
        elif N >= 10:
            answer += N // 10
            N = N % 10
        elif N == 0:
            break
    return answer
print(change(N))