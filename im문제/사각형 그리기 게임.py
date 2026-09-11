def square(matrix, N):
    square_list = []
    answer = []
    count = 0
    for i in range(1,21):
        square_list = []  # 문제에서 주어진 값 범위가 20까지이므로 해당 범위 내에서 설정
        
        for j in range(N):
            for k in range(N):
                if matrix[j][k] == i:
                    square_list.append([j,k]) # 
        if square_list != []:
            for i in range(len(square_list)):
                    for j in range(i+1, len(square_list)):
                        answer.append((square_list[j][0]-square_list[i][0] + 1) * (square_list[j][1]-square_list[i][1] + 1))
    answer.sort()
    count = answer.count(answer[-1])
    return count

K = int(input())
for i in range(K):
    T= int(input())
    arr = []
    for a in range(T):
        arr.append(list(map(int,input().split())))
    print(f"#{i+1} {square(arr,T)}")