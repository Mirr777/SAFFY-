def square(matrix, N):
    square_list = []
    answer = 0
    for i in range(N):
        for j in range(N): # 이중 for문까지는 이차원 배열 순서대로 
            for m in range(i,N):
                for n in range(j,N): # 왼쪽 상단보다 오른쪽 하단이 같거나 커야 하므로 범위 조절하기 
                    if matrix[i][j] == matrix[m][n]: # 왼쪽 상단과 오른쪽 하단 값이 같은 경우
                        square_list.append((m-i+1)*(n-j+1)) # 넓이 구해서 리스트에 담기
    square_list.sort() # 오름차순으로 정렬하기
    answer = square_list.count(square_list[-1]) # 가장 마지막(최댓값) 개수 찾은 후 반환하기
    return answer 
 
K = int(input())
for i in range(K):
    T= int(input())
    arr = []
    for a in range(T):
        arr.append(list(map(int,input().split())))
    print(f"#{i+1} {square(arr,T)}")
