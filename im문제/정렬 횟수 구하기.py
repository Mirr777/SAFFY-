def sort_count(arr_list, n):
    answer = 0
    new = sorted(arr_list)
    if arr_list == new: return 0

    while True:
        for i in range(2):
            for j in range((n-i)//2):
                if arr_list[2 * j + i] > arr_list[2 * j +1 + i]:
                    a = arr_list[2 * j + i]
                    b = arr_list[2 * j + 1 + i]
                    arr_list[2 * j + 1 + i] = a
                    arr_list[2 * j + i] = b
            c = sorted(arr_list)
            if c == arr_list:
                return answer + 1
            else:
                answer += 1
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{tc} {sort_count(arr, N)}")