def get_count(arr_list, n):
    answer = 0
    for i in arr_list:
        if i == n:
            answer +=1


    return answer


arr = [5, 2, 5, 7, 3]
N = int(input())
print(get_count(arr, N))