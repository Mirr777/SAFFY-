def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                m = a[j]
                n = a[j+1]
                a[j] = n
                a[j+1] = m
    return a
a = [12, 3,9, 1, 15, 7]

result = BubbleSort(a, len(a))
print(*BubbleSort(a, 6))