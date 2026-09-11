def is_exist(arr1_list, arr2_list):
    answer = []
    for i in arr1_list:
        if i in arr2_list:
            answer.append("O")
        else:
            answer.append("X")
    return answer



arr1 = [5, 7, 5, 4, 2, 9]
arr2 = [5, 4, 2, 5, 6]

print(*is_exist(arr1, arr2))