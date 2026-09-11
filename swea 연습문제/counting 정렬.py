def counting_sort(DATA, k): #arr 값, arr 내부 최대값
    counts = [0] * (k+1) # 최대값보다 1 큰 개수만큼 0 넣기
    TEMP = [0] * len(DATA) # DATA와 같은 크기의 TEMP 리스트 만들기
    for i in range(len(DATA)): # DATA가 가지고 있는 위치에 1 더하기
        counts[DATA[i]] += 1
         
    for j in range(1, k+1): # 인덱스가 높은 순대로 count 값이 높게끔 설정
        counts[j] += counts[j-1]
        

    for l in range(len(DATA)-1, -1, -1):
        counts[DATA[l]] -= 1
        
        TEMP[counts[DATA[l]]] = DATA[l]
    return TEMP

arr = [12, 3, 9, 1, 15, 7]
print(counting_sort(arr,max(arr)))