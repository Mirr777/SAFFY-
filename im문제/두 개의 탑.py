def tower(arr_list, m, n, k):
    arr_split = []
    arr_list.sort(reverse=True)   #받은 array 오름차순으로 정렬
    answer = 0
    if n < k:
        for i in range(n):
            arr_split.append(arr_list[i*2])   # array 오름차순 기준으로 step 두번째 인덱스마다 탑에 세우기
    else:
        for i in range(k):
            arr_split.append(arr_list[i*2])

    arr_list = list(set(arr_list)-set(arr_split))   #split 리스트에는 낮은 탑 기준, arr 리스트에는 높은 탑에 들어갈 숫자 넣기
    arr_list.sort(reverse=True) # set 함수 떄문에 바뀐 순더 다시 오름차순으로 정렬
    for idx,j in enumerate(arr_list): # 높은 탑에 들어갈 숫자 계산
        answer += j * (idx+1)

    for idx, k in enumerate(arr_split): # 낮은 탑에 들어갈 숫자 계산
        answer += k * (idx+1)

    return answer
 


N = int(input())  # 입력 예제 받기
for i in range(N):
    a, b, c = map(int,input().split())
    arr = []
    arr = list(map(int,input().split()))
    print(f"#{i+1} {tower(arr, a, b, c)}")