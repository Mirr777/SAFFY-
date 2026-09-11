def block(arr, N):
    arr.sort()
    sum = 0
    for i in range(N):
        sum += arr[i]
        if sum > 100:
            return i
    return N

N = int(input())
arr = list(map(int,input().split()))
print(block(arr,N))