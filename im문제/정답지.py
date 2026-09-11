def total_sum(p): # 정답 계산법에 맞게끔 산출하는 함수
    if p <= 1:
        return p
    else:
        return (p + total_sum(p-1)) 
def answer(student, teacher, m, n):
    final_answer = 0
    answer = 0
    result = []
    for i in range(m):
        final_answer = 0
        for j in range(n):
            if student[i][j] == teacher[j]:   # 정답지와 학생들의 답 비교하여 맞으면 answer 값 더하기
                answer +=1
            elif student[i][j] != teacher[j]:
                a = total_sum(answer)
                final_answer += a  # 오답일 경우, 계산법에 맞게 계산하기.
                answer = 0 # answer 초기화
        if answer != 0:
            b = total_sum(answer)
            final_answer += b
            answer = 0 # 마지막 답안이 정답일 경우, 처리하기
        result.append(final_answer) # 다 더한 값, result 리스트에 넣기
    return max(result) - min(result) # 최댓값 - 최솟값 return 하기



N = int(input())  # 입력예제 받기
for _ in range(N):
    a, b = map(int,input().split())
    right = list(map(int,input().split()))
    arr = []
    for i in range(a):
        arr.append(list(map(int,input().split())))
    print(f"#{_+1} {answer(arr,right,a,b)}")