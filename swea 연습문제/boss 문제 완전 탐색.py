
path = []
count = 0
def dice(lev, n):
    global count
    if lev == n:
        if sum(path) <= 10:
            count += 1
        return
    for i in range(1, 7):
        path.append(i)
        dice(lev+1, n)
        path.pop()

N = int(input())

dice(0, N)
print(count)