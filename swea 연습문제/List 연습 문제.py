arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9, 12]
N = len(arr)
for i in range(1<<N):
    s = 0
    for j in range(N):
        if i & (1<<j):
            s += arr[j]
    if s == 0:
        ans = "Y"
        print(arr[j])
        break
print(ans)
