def English(arr_list, m, n, l):
    answer = -1
    max_val = max(arr_list)
    min_val = min(arr_list)
    t1 = 0
    t2 = 0
    t3 = 0
    min_answer = float("inf")
    for i in range(min_val,max_val):
        for j in range(i+1,max_val+1):
            t1 = 0
            t2 = 0
            t3 = 0
            for k in arr_list: #주어진 조건에 맞게끔 t1, t2, t3 신입사원 수 구하기
                if k < i:
                    t1 += 1
                elif i <= k < j:
                    t2 += 1
                elif k >= j:
                    t3 += 1
            if max(t1, t2, t3) <= l and min(t1, t2, t3) >= n: #제약 조건 중 주어진 최소 최대 인원에 맞을 때만 값 구하기
                answer = max(t1, t2, t3) - min(t1, t2, t3)
                min_answer = min(answer, min_answer)
    if min_answer == float("inf"): #제약 조건에 의해 계산되지 않을 때에(답이 없을 경우) -1 return 하기
        min_answer = -1
    return min_answer

N =int(input())
for i in range(N):
    a, b, c = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f"#{i+1} {English(arr, a, b, c)}")