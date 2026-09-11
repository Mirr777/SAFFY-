def coffee_time(arr,N):
    arr.sort()
    max_answer = 0
    for i in range(N):
        answer = 0
        time = 0
        for j in range(i,N):
            if arr[j][0] >= time:
                answer +=1
                time = arr[j][1]
        max_answer = max(answer, max_answer)
    return max_answer

N = int(input())
arr = []
for i in range(N):
    a, b = map(int,input().split())
    arr.append([a,b])
print(coffee_time(arr,N))