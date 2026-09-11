def palindrome(case, m, n):
    answer = ""
    for i in range(m):
        for j in range(m-n+1):
            if case[i][j:j+n+1] == case[i][j:j+n+1][::-1]:
                answer = case[i][j:j+n+1]
                return answer
            else:
                answer = ""
                for k in range(n):
                    if case[j+k][i] != case[j+n-1-k][i]:
                        break
                    else:
                        answer += case[j+k][i]
                else:
                    return answer

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    c = []
    for i in range(a):
        c.append(input())
    print(f"#{tc} {palindrome(c,a,b)}")