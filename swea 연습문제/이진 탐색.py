def binary_search(arr_list1, arr_list2, a):
    answer = 0
    arr_list1.sort()
    for i in arr_list2:
        l = 0
        r = a - 1
        k = 0
        while l <= r:
            m = (l + r) // 2

            if arr_list1[m] == i:
                answer += 1
                break  # 원소를 찾았으므로 다음 숫자로 이동
            elif arr_list1[m] < i:
                if k == 1:
                    break
                l = m + 1  # 오른쪽 구간 탐색
                k = 1
            else:
                if k == 2:
                    break
                r = m - 1  # 왼쪽 구간 탐색
                k = 2
    return answer


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print(f"#{tc} {binary_search(arr1, arr2, N)}")