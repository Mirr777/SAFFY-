path = []
def dice(lev,N):
    if lev == N:
        print(*path)
        return
    else:
        for i in range(1,7):
            if i >= max(path, default=0):
                path.append(i)
                dice(lev+1,N)
                path.pop()

N = int(input())
dice(0,N)