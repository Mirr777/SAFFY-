def cal(arr_list, n):
    answer = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            answer += arr_list[i] % arr_list[j]
    return answer



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{tc} {cal(arr,N)}")