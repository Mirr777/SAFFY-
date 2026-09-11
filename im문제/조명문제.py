def light(arr_list, m):
    new_list = []
    second_list = []
    minimum_number = 0
    if arr_list[0] == 0:   # 첫번째 불이 0일 때에는 따로 조명을 안 켜도 되므로 초기 0에서 시작
        answer = 0
    elif arr_list[0] == 1: # 첫번째 불이 1일 때에는 조명을 한 변 켜야 되므로 초기 1에서 시작
        answer = 1

    for idx, ele in enumerate(arr_list):
        if ele != arr_list[0]:
            new_list.append(idx+1)    # 첫번째 불과 다른 조명 위치 찾기
    while True:
        print(new_list)
        if new_list == []:
            return answer    # new_list에 별도의 조명이 없으면(바꿀 게 없으면) 그대로 값을 return
        for j in range(2, m+1):
            minimum_number = new_list[0]             # 
            if j % minimum_number == 0:
                if j not in new_list:     
                    second_list.append(j)    # 조명을 바꿀 때 껴져 있던 것을 키므로 해당 값 second_list에 저장
        for i in new_list:
            if i % minimum_number !=0:   
                second_list.append(i)       # 조명을 바꿀 때 해당 범위 내에 있지 않은 값 second_list에 저장
        answer += 1
        second_list.sort()  # second_list의 값이 순서 없이 있으므로 해당 값 오름차순으로 저장
        new_list = second_list

        second_list = [] # second_list 값 초기화

N = int(input())
for i in range(N):
    a = int(input())
    arr = list(map(int,input().split()))
    print(f"#{i+1} {light(arr,a)}")